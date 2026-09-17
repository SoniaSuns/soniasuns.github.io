import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import http from 'node:http';
import { createApp } from './server.mjs';
import { makePrompt, extract } from './codex.mjs';

const token = 'a'.repeat(64);
const papers = [{ id: 'P161', title: 'Test paper', sha256: 'b'.repeat(64), pages: 2, abstract_zh: 'Paper summary' }];
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function started(t, options = {}) {
  const dataDir = options.dataDir || fs.mkdtempSync(path.join(os.tmpdir(), 'literature-chat-test-'));
  const app = createApp({ papers, token, dataDir, extractor: async () => [], runner: async () => 'An answer [P161, summary]', ...options });
  await new Promise(resolve => app.server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${app.server.address().port}`;
  t.after(() => app.stop());
  const call = async (route, method = 'GET', body, headers = {}) => {
    const response = await fetch(base + '/api/' + route, { method, headers: { Authorization: 'Bearer ' + token, Origin: base, ...(body ? { 'Content-Type': 'application/json' } : {}), ...headers }, body: body ? JSON.stringify(body) : undefined });
    return { status: response.status, data: response.status === 204 ? null : await response.json(), headers: response.headers };
  };
  return { app, base, call, dataDir };
}

test('auth, exact origins, Host, validation and private file boundaries', async t => {
  const { call, base } = await started(t);
  assert.equal((await call('status', 'GET', null, { Authorization: '' })).status, 401);
  assert.equal((await call('status', 'GET', null, { Origin: 'https://evil.example' })).status, 403);
  const badHost = await new Promise(resolve => {
    http.get(base + '/api/status', { headers: { Host: 'evil.example', Authorization: 'Bearer ' + token } }, response => { response.resume(); resolve(response.statusCode); });
  });
  assert.equal(badHost, 403);
  assert.equal((await call('status', 'GET', null, { Origin: 'null' })).status, 403);
  const allowed = await call('status', 'GET', null, { Origin: 'https://soniasuns.github.io' });
  assert.equal(allowed.status, 200);
  assert.equal(allowed.headers.get('access-control-allow-origin'), 'https://soniasuns.github.io');
  assert.equal((await call('sessions', 'POST', { paper_ids: ['P999'] })).status, 400);
  assert.equal((await call('sessions', 'POST', { paper_ids: ['P161', 'P161'] })).status, 400);
  assert.equal((await call('sessions', 'POST', { paper_ids: ['P161'] }, { Origin: '' })).status, 403);
  assert.equal((await fetch(base + '/.literature-chat/history.json')).status, 404);
  assert.equal((await call('papers/P999/text')).status, 404);
});

test('durable multi-turn histories, rename, export, delete and restart', async t => {
  const { call, app, dataDir } = await started(t);
  const created = await call('sessions', 'POST', { title: 'First', paper_ids: ['P161'] });
  assert.equal(created.status, 201);
  const id = created.data.id;
  assert.equal((await call(`sessions/${id}/messages`, 'POST', { text: 'Question', paper_ids: ['P161'] })).status, 202);
  while (app.active) await pause(10);
  let session = (await call('sessions/' + id)).data;
  assert.equal(session.messages.length, 2);
  assert.equal(session.messages[1].status, 'complete');
  assert.equal((await call(`sessions/${id}/messages`, 'POST', { text: 'Follow-up', paper_ids: ['P161'] })).status, 202);
  while (app.active) await pause(10);
  await call('sessions/' + id, 'PATCH', { title: 'Renamed' });
  assert.equal((await call('export')).data.sessions[0].messages.length, 4);
  app.stop();
  const restored = await started(t, { dataDir });
  session = (await restored.call('sessions/' + id)).data;
  assert.equal(session.title, 'Renamed');
  assert.equal(session.messages[2].text, 'Follow-up');
  assert.equal((await restored.call('sessions/' + id, 'DELETE')).status, 200);
  assert.equal((await restored.call('sessions/' + id)).status, 404);
});

test('one active answer, stop, failure and interrupted-question retention', async t => {
  let finish;
  const { call, app, dataDir } = await started(t, { runner: () => new Promise(resolve => { finish = resolve; }) });
  const id = (await call('sessions', 'POST', { paper_ids: ['P161'] })).data.id;
  const turns = await Promise.all([call(`sessions/${id}/messages`, 'POST', { text: 'Q1', paper_ids: ['P161'] }), call(`sessions/${id}/messages`, 'POST', { text: 'Q2', paper_ids: ['P161'] })]);
  assert.deepEqual(turns.map(result => result.status).sort(), [202, 409]);
  assert.equal((await call('sessions/' + id, 'DELETE')).status, 409);
  await call(`sessions/${id}/cancel`, 'POST', {});
  finish('Cancelled output');
  while (app.active) await pause(10);
  assert.equal((await call('sessions/' + id)).data.messages[1].status, 'cancelled');
  app.stop();
  const stored = JSON.parse(fs.readFileSync(path.join(dataDir, 'history.json')));
  stored.sessions[0].messages[1].status = 'generating';
  fs.writeFileSync(path.join(dataDir, 'history.json'), JSON.stringify(stored));
  const restarted = await started(t, { dataDir, runner: async () => { throw new Error('Login failed'); } });
  assert.equal((await restarted.call('sessions/' + id)).data.messages[1].status, 'interrupted');
  await restarted.call(`sessions/${id}/messages`, 'POST', { text: 'Retry', paper_ids: ['P161'] });
  while (restarted.app.active) await pause(10);
  const session = (await restarted.call('sessions/' + id)).data;
  assert.equal(session.messages[2].text, 'Retry');
  assert.equal(session.messages[3].status, 'failed');
});

test('invalid history fails closed rather than erasing content', () => {
  const dataDir = fs.mkdtempSync(path.join(os.tmpdir(), 'literature-bad-history-'));
  fs.writeFileSync(path.join(dataDir, 'history.json'), '{broken');
  assert.throws(() => createApp({ dataDir, papers, runner: async () => '' }));
  assert.equal(fs.readFileSync(path.join(dataDir, 'history.json'), 'utf8'), '{broken');
});

test('Q&A uses extracted files without a PDF, keeps page numbers, and labels missing text', async () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'literature-text-first-'));
  fs.mkdirSync(path.join(root, 'literature-corpus/text'), { recursive: true });
  fs.writeFileSync(path.join(root, 'literature-corpus/text', papers[0].sha256 + '.json'), JSON.stringify({ sha256: papers[0].sha256, pages: [{ page: 1, text: 'Persisted text without any PDF.' }, { page: 2, text: 'Second page evidence.' }] }));
  const output = await extract(root, root, papers, '第2页', () => {});
  assert.equal(output[0].read_from, 'extracted_text');
  assert.equal(output[0].pages[1].page, 2);
  const absent = await extract(root, root, [{ ...papers[0], sha256: 'c'.repeat(64) }], 'Q', () => {});
  assert.equal(absent[0].source, 'summary');
  assert.equal(absent[0].pages.length, 0);
  const prompt = makePrompt(papers, output, [{ role: 'user', text: 'Explain this', paper_ids: ['P161'], status: 'complete' }]);
  assert.match(prompt, /Persisted text without any PDF/);
  assert.match(prompt, /Explain this/);
});
