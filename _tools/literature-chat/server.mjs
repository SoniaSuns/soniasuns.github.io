import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { locateCodex, extract, makePrompt, runCodex, stopChild } from './codex.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const defaultRoot = path.resolve(here, '../../..');
const publicOrigin = 'https://soniasuns.github.io';
const uuid = /^[a-f0-9-]{36}$/;
const json = (response, status, value) => {
  response.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8' });
  response.end(JSON.stringify(value));
};

function readBody(request) {
  return new Promise((resolve, reject) => {
    if (!request.headers['content-type']?.startsWith('application/json')) return reject(Object.assign(new Error('需要 JSON 请求。'), { status: 415 }));
    let size = 0;
    const chunks = [];
    request.on('data', chunk => {
      size += chunk.length;
      if (size <= 65536) chunks.push(chunk);
    });
    request.on('end', () => {
      if (size > 65536) return reject(Object.assign(new Error('请求过长。'), { status: 413 }));
      try {
        const value = JSON.parse(Buffer.concat(chunks).toString('utf8'));
        if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error('Invalid body');
        resolve(value);
      }
      catch { reject(Object.assign(new Error('JSON 格式无效。'), { status: 400 })); }
    });
    request.on('error', reject);
  });
}

export function createApp(options = {}) {
  const root = options.root || defaultRoot;
  const dataDir = options.dataDir || path.join(root, '.literature-chat');
  const preview = path.join(root, 'literature-review');
  const records = options.papers || fs.readdirSync(path.join(root, 'website/_data/literature_review'))
    .filter(file => /^papers_.*\.json$/.test(file))
    .flatMap(file => JSON.parse(fs.readFileSync(path.join(root, 'website/_data/literature_review', file), 'utf8')));
  const papers = new Map(records.map(paper => [paper.id, paper]));
  fs.mkdirSync(dataDir, { recursive: true });
  const worker = path.join(dataDir, 'worker');
  fs.mkdirSync(worker, { recursive: true });
  const historyFile = path.join(dataDir, 'history.json');
  let state = { version: 1, sessions: [] };
  if (fs.existsSync(historyFile)) {
    state = JSON.parse(fs.readFileSync(historyFile, 'utf8'));
    if (state.version !== 1 || !Array.isArray(state.sessions) || state.sessions.some(session => !uuid.test(session.id) || typeof session.title !== 'string' || !Array.isArray(session.messages) || !Array.isArray(session.paper_ids) || session.messages.some(message => !uuid.test(message.id) || !['user', 'assistant'].includes(message.role) || typeof message.text !== 'string'))) {
      throw new Error('历史文件格式无效，已停止启动以保护原有记录。请检查 history.json 或其 .bak 备份。');
    }
  }
  const token = options.token || crypto.randomBytes(32).toString('hex');
  const executable = options.runner ? null : locateCodex();
  let active = null;
  let storageError = false;
  function persist() {
    try {
      const temporary = historyFile + '.tmp';
      fs.writeFileSync(temporary, JSON.stringify(state, null, 2), { mode: 0o600 });
      if (fs.existsSync(historyFile)) fs.copyFileSync(historyFile, historyFile + '.bak');
      fs.renameSync(temporary, historyFile);
    } catch {
      storageError = true;
      throw Object.assign(new Error('本机历史保存失败。请检查磁盘空间和文件权限；先导出当前记录。'), { status: 507 });
    }
  }
  let recovered = false;
  for (const session of state.sessions) for (const message of session.messages) {
    if (message.status === 'generating') { message.status = 'interrupted'; message.error = '本机服务已重启，上一轮回答中断。'; recovered = true; }
  }
  if (recovered) persist();
  const listing = () => state.sessions.map(({ id, title, updated_at, paper_ids, messages }) => ({ id, title, updated_at, paper_ids, count: messages.length, busy: active?.session.id === id })).sort((a, b) => b.updated_at.localeCompare(a.updated_at));
  const selected = value => {
    if (!Array.isArray(value) || value.length < 1 || value.length > 4 || new Set(value).size !== value.length || value.some(id => !papers.has(id))) throw Object.assign(new Error('请选择 1 至 4 篇资料库中的论文。'), { status: 400 });
    return value;
  };
  const find = id => {
    const session = state.sessions.find(item => item.id === id);
    if (!session) throw Object.assign(new Error('会话不存在。'), { status: 404 });
    return session;
  };

  async function answer(job) {
    try {
      const contextPapers = job.session.paper_ids.map(id => papers.get(id));
      const extracted = await (options.extractor || extract)(root, path.join(dataDir, 'pdf-cache'), contextPapers, job.question, child => { job.child = child; if (job.cancelled) stopChild(child); });
      if (job.cancelled) return;
      job.message.sources = contextPapers.map(paper => {
        const source = extracted.find(item => item.id === paper.id);
        return { id: paper.id, title: paper.title, source: source?.source || 'summary', pages: source?.pages.map(item => item.page) || [], total_pages: source?.total_pages || paper.pages, truncated: !!source?.pages.some(item => item.truncated) };
      });
      const prompt = makePrompt(contextPapers, extracted, job.session.messages.filter(item => item.id !== job.message.id));
      const text = await (options.runner || runCodex)({ executable, cwd: worker, prompt, onChild: child => { job.child = child; if (job.cancelled) stopChild(child); }, onMessage: text => { job.message.text = text; } });
      if (!job.cancelled) { job.message.text = text; job.message.status = 'complete'; }
    } catch (error) {
      if (!job.cancelled) { job.message.status = 'failed'; job.message.error = String(error.message).slice(0, 1000); }
    } finally {
      if (job.cancelled) { job.message.status = 'cancelled'; job.message.error = '已停止回答。'; }
      job.session.updated_at = new Date().toISOString();
      try { persist(); } catch { job.message.error = '回答尚未保存到磁盘，请导出当前记录。'; }
      if (active === job) active = null;
    }
  }

  const staticFiles = new Map([
    ['/', ['index.html', 'text/html; charset=utf-8']],
    ...['literature-review.js', 'literature-notes.js', 'literature-chat.js'].map(file => ['/assets/js/' + file, ['assets/js/' + file, 'text/javascript; charset=utf-8']]),
    ['/assets/css/literature-review.css', ['assets/css/literature-review.css', 'text/css; charset=utf-8']],
    ['/assets/data/literature-review.json', ['assets/data/literature-review.json', 'application/json; charset=utf-8']],
    ['/assets/data/literature-review.md', ['assets/data/literature-review.md', 'text/plain; charset=utf-8']],
  ]);
  const server = http.createServer(async (request, response) => {
    response.setHeader('Cache-Control', 'no-store');
    response.setHeader('X-Content-Type-Options', 'nosniff');
    response.setHeader('Referrer-Policy', 'no-referrer');
    response.setHeader('X-Frame-Options', 'DENY');
    const port = server.address().port;
    const localOrigin = `http://127.0.0.1:${port}`;
    if (request.headers.host !== `127.0.0.1:${port}`) return json(response, 403, { error: 'Host not allowed' });
    const origin = request.headers.origin;
    if (origin && origin !== publicOrigin && origin !== localOrigin) return json(response, 403, { error: 'Origin not allowed' });
    if (origin) {
      response.setHeader('Access-Control-Allow-Origin', origin);
      response.setHeader('Vary', 'Origin');
    }
    if (request.method === 'OPTIONS') {
      if (!origin) return json(response, 403, { error: 'Origin required' });
      response.setHeader('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE');
      response.setHeader('Access-Control-Allow-Headers', 'Authorization, Content-Type');
      response.setHeader('Access-Control-Allow-Private-Network', 'true');
      response.writeHead(204); response.end(); return;
    }
    try {
      const url = new URL(request.url, localOrigin);
      if (!url.pathname.startsWith('/api/')) {
        const file = staticFiles.get(url.pathname);
        if (request.method !== 'GET' || !file) return json(response, 404, { error: 'Not found' });
        const content = fs.readFileSync(path.join(preview, file[0]));
        response.setHeader('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self' http://127.0.0.1:*; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'");
        response.writeHead(200, { 'Content-Type': file[1] }); response.end(content); return;
      }
      const auth = request.headers.authorization || '';
      const supplied = Buffer.from(auth.startsWith('Bearer ') ? auth.slice(7) : '');
      const expected = Buffer.from(token);
      if (supplied.length !== expected.length || !crypto.timingSafeEqual(supplied, expected)) return json(response, 401, { error: '配对令牌无效，请重新连接本机服务。' });
      if (request.method !== 'GET' && !origin) return json(response, 403, { error: 'Origin required' });
      if (request.method !== 'GET' && storageError) return json(response, 507, { error: '磁盘保存异常，请先导出记录并重启服务。' });
      if (url.pathname === '/api/status' && request.method === 'GET') return json(response, 200, { connected: true, storage_error: storageError, busy_session: active?.session.id || null, papers: papers.size });
      if (url.pathname === '/api/export' && request.method === 'GET') return json(response, 200, { format: 'literature-chat-history', exported_at: new Date().toISOString(), ...state });
      const paperMatch = url.pathname.match(/^\/api\/papers\/(P\d{3,6})\/text$/);
      if (paperMatch && request.method === 'GET') {
        const paper = papers.get(paperMatch[1]);
        if (!paper) return json(response, 404, { error: '论文不存在。' });
        const source = path.join(root, 'literature-corpus/text', paper.sha256 + '.json');
        if (!fs.existsSync(source)) return json(response, 404, { error: '尚无全文提取文件，请先运行本地全文提取。' });
        const extracted = JSON.parse(fs.readFileSync(source, 'utf8'));
        return json(response, 200, { id: paper.id, title: paper.title, ...extracted });
      }
      if (url.pathname === '/api/sessions' && request.method === 'GET') return json(response, 200, { sessions: listing(), storage_error: storageError });
      if (url.pathname === '/api/sessions' && request.method === 'POST') {
        const body = await readBody(request);
        const paper_ids = selected(body.paper_ids);
        if (state.sessions.length >= 1000) return json(response, 409, { error: '会话过多，请先导出并整理旧会话。' });
        const session = { id: crypto.randomUUID(), title: typeof body.title === 'string' ? body.title.trim().slice(0, 80) || '新对话' : '新对话', paper_ids, created_at: new Date().toISOString(), updated_at: new Date().toISOString(), messages: [] };
        state.sessions.push(session); persist(); return json(response, 201, session);
      }
      const match = url.pathname.match(/^\/api\/sessions\/([a-f0-9-]{36})(?:\/(messages|cancel))?$/);
      if (!match) return json(response, 404, { error: 'Not found' });
      const session = find(match[1]);
      const action = match[2];
      if (!action && request.method === 'GET') return json(response, 200, { ...session, busy: active?.session.id === session.id, storage_error: storageError });
      if (!action && request.method === 'PATCH') {
        const body = await readBody(request);
        if (typeof body.title !== 'string' || !body.title.trim() || body.title.length > 80) return json(response, 400, { error: '会话名称须为 1 至 80 个字符。' });
        session.title = body.title.trim(); persist(); return json(response, 200, session);
      }
      if (!action && request.method === 'DELETE') {
        if (active?.session.id === session.id) return json(response, 409, { error: '请先停止回答，再删除会话。' });
        state.sessions = state.sessions.filter(item => item !== session); persist(); return json(response, 200, { deleted: true });
      }
      if (action === 'cancel' && request.method === 'POST') {
        if (active?.session.id === session.id) { active.cancelled = true; stopChild(active.child); }
        return json(response, 200, { stopping: true });
      }
      if (action === 'messages' && request.method === 'POST') {
        if (active) return json(response, 409, { error: '本机正在回答另一问题，请等待完成或停止该回答。' });
        const body = await readBody(request);
        if (active) return json(response, 409, { error: '本机正在回答另一问题，请稍后重试。' });
        if (typeof body.text !== 'string' || !body.text.trim() || body.text.length > 12000) return json(response, 400, { error: '问题须为 1 至 12,000 个字符。' });
        if (session.messages.length >= 1000) return json(response, 409, { error: '本会话较长，请开启新对话。原记录仍保留。' });
        session.paper_ids = selected(body.paper_ids);
        const now = new Date().toISOString();
        session.updated_at = now;
        session.messages.push({ id: crypto.randomUUID(), role: 'user', text: body.text.trim(), paper_ids: [...session.paper_ids], status: 'complete', created_at: now });
        const message = { id: crypto.randomUUID(), role: 'assistant', text: '', paper_ids: [...session.paper_ids], status: 'generating', created_at: now, sources: [] };
        session.messages.push(message);
        persist();
        active = { session, message, question: body.text, child: null, cancelled: false };
        void answer(active);
        return json(response, 202, { ...session, busy: true });
      }
      return json(response, 405, { error: 'Method not allowed' });
    } catch (error) {
      if (!response.headersSent) json(response, error.status || 500, { error: error.status ? error.message : '本机服务请求失败，历史文件未主动清空。' });
      else response.end();
    }
  });
  server.requestTimeout = 15000;
  server.headersTimeout = 10000;
  return { server, token, dataDir, stop: () => { if (active) { active.cancelled = true; stopChild(active.child); } server.close(); }, get active() { return active; } };
}

async function main() {
  const stateDir = path.join(defaultRoot, '.literature-chat');
  fs.mkdirSync(stateDir, { recursive: true });
  const lock = path.join(stateDir, 'server.lock');
  if (fs.existsSync(lock)) {
    const pid = Number(fs.readFileSync(lock, 'utf8'));
    if (!Number.isInteger(pid) || pid <= 0) throw new Error('Invalid server lock; inspect .literature-chat/server.lock before restarting.');
    let running = true;
    try { process.kill(pid, 0); } catch (error) { if (error.code === 'ESRCH') running = false; }
    if (running) throw new Error('A local paper-chat service is already running. Use the launcher to reconnect.');
    fs.unlinkSync(lock);
  }
  fs.writeFileSync(lock, String(process.pid), { flag: 'wx', mode: 0o600 });
  process.on('exit', () => { try { if (fs.readFileSync(lock, 'utf8') === String(process.pid)) fs.unlinkSync(lock); } catch {} });
  const app = createApp();
  const requested = Number(process.env.LITERATURE_PORT || 8765);
  if (!Number.isInteger(requested) || requested < 1024 || requested > 65525) throw new Error('Invalid port');
  for (let port = requested; port < requested + 10; port++) {
    try {
      await new Promise((resolve, reject) => {
        const error = error => { app.server.off('listening', listening); reject(error); };
        const listening = () => { app.server.off('error', error); resolve(); };
        app.server.once('error', error).once('listening', listening).listen(port, '127.0.0.1');
      });
      fs.writeFileSync(path.join(app.dataDir, 'connection.json'), JSON.stringify({ pid: process.pid, port, token: app.token, started_at: new Date().toISOString() }), { mode: 0o600 });
      console.log(`Literature chat: http://127.0.0.1:${port}/ (loopback only)`);
      process.on('SIGTERM', () => app.stop());
      process.on('SIGINT', () => app.stop());
      return;
    } catch (error) { if (error.code !== 'EADDRINUSE') throw error; }
  }
  throw new Error('No available local port');
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main().catch(error => { console.error(error.message); process.exitCode = 1; });
