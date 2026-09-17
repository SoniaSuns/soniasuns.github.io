(function () {
  "use strict";
  var root = document.getElementById("literature-review");
  if (!root || !document.getElementById("lr-chat")) return;
  var get = function (id) { return document.getElementById(id); };
  var cards = new Map(Array.from(root.querySelectorAll(".lr-paper")).map(function (card) { return [card.dataset.id, card]; }));
  var selected = new Set();
  var connection = null;
  var connected = false;
  var activeId = "";
  var busy = false;
  var posting = false;
  var epoch = 0;
  var signature = "";
  var sessions = [];
  var drafts = {};
  var poll;
  var question = get("lr-chat-question");
  var messages = get("lr-chat-messages");
  var select = get("lr-chat-sessions");
  var buttons = new Map();
  var icons = {
    plus: ["M5 12h14", "M12 5v14"],
    pencil: ["M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z", "m15 5 4 4"],
    "arrow-up": ["m5 12 7-7 7 7", "M12 19V5"],
    x: ["M18 6 6 18", "m6 6 12 12"],
    "message-circle": ["M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"],
    download: ["M12 15V3", "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4", "m7 10 5 5 5-5"],
    trash: ["M10 11v6", "M14 11v6", "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6", "M3 6h18", "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"]
  };
  function node(tag, className, text) {
    var element = document.createElement(tag);
    if (className) element.className = className;
    if (text) element.textContent = text;
    return element;
  }
  // Lucide geometry, distributed under the adjacent lucide-LICENSE.txt.
  function icon(button, name) {
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    var attrs = { viewBox: "0 0 24 24", width: "16", height: "16", fill: "none", stroke: "currentColor", "stroke-width": "2", "stroke-linecap": "round", "stroke-linejoin": "round", "aria-hidden": "true" };
    Object.keys(attrs).forEach(function (key) { svg.setAttribute(key, attrs[key]); });
    if (name === "square") {
      var rect = document.createElementNS(ns, "rect");
      Object.entries({ x: 3, y: 3, width: 18, height: 18, rx: 2 }).forEach(function (item) { rect.setAttribute(item[0], item[1]); });
      svg.appendChild(rect);
    } else (icons[name] || []).forEach(function (d) { var path = document.createElementNS(ns, "path"); path.setAttribute("d", d); svg.appendChild(path); });
    button.prepend(svg);
  }
  root.querySelectorAll("[data-lr-icon]").forEach(function (button) { icon(button, button.dataset.lrIcon); });
  function error(text) { get("lr-chat-error").textContent = text; get("lr-chat-error").hidden = !text; }
  function remember() {
    try { sessionStorage.setItem("literature-chat:ui:v1", JSON.stringify({ activeId: activeId, selected: Array.from(selected), drafts: drafts })); }
    catch (_) { get("lr-chat-save-state").textContent = "草稿未缓存 · 已发送历史仍存本机"; }
  }
  function rememberDraft() { drafts[activeId || "new"] = question.value; remember(); }
  function controls() {
    get("lr-chat-send").disabled = !connected || posting || busy || !selected.size || !question.value.trim();
    get("lr-chat-stop").hidden = !busy;
    get("lr-chat-stop").disabled = !connected || posting;
    get("lr-chat-new").disabled = posting;
    get("lr-chat-delete").disabled = !connected || !activeId || busy || posting;
    get("lr-chat-rename").disabled = !connected || !activeId || posting;
    get("lr-chat-export").disabled = !connected;
    select.disabled = posting;
    get("lr-chat-status").textContent = !connected ? "未连接本机" : busy ? "Codex 回答中" : "已连接本机";
    get("lr-chat-status").dataset.connected = String(connected);
  }
  function renderScope() {
    var container = get("lr-chat-papers");
    container.replaceChildren();
    selected.forEach(function (id) {
      var button = node("button", "", id);
      button.type = "button";
      button.title = "移除 " + cards.get(id).dataset.title;
      button.setAttribute("aria-label", "移除参考论文 " + id);
      icon(button, "x");
      button.addEventListener("click", function () { selected.delete(id); renderScope(); remember(); });
      container.appendChild(button);
    });
    buttons.forEach(function (button, id) { button.setAttribute("aria-pressed", String(selected.has(id))); });
    get("lr-chat-scope-empty").hidden = selected.size !== 0;
    controls();
  }
  function showView(view) {
    root.dataset.view = view;
    root.querySelectorAll("[data-lr-view]").forEach(function (button) { button.setAttribute("aria-pressed", String(button.dataset.lrView === view)); });
  }
  root.querySelectorAll("[data-lr-view]").forEach(function (button) { button.addEventListener("click", function () { showView(button.dataset.lrView); }); });
  cards.forEach(function (card, id) {
    var button = node("button", "lr-ask-paper", "加入问答");
    button.type = "button";
    button.title = "选择或移除参考论文 " + id;
    button.setAttribute("aria-label", "选择参考论文 " + id);
    icon(button, "message-circle");
    button.addEventListener("click", function (event) {
      event.preventDefault(); event.stopPropagation();
      if (selected.has(id)) selected.delete(id);
      else if (selected.size < 4) selected.add(id);
      else { error("每次最多选择 4 篇论文。"); showView("chat"); return; }
      error(""); renderScope(); remember();
    });
    card.querySelector("summary").appendChild(button);
    buttons.set(id, button);
    var fulltext = node("button", "lr-ask-paper lr-fulltext-button", "全文");
    fulltext.type = "button";
    fulltext.title = "查看 " + id + " 的本机提取全文";
    fulltext.addEventListener("click", async function (event) {
      event.preventDefault(); event.stopPropagation();
      if (!connected) { error("查看全文需要连接本机提取文件。请先连接本机服务。"); get("lr-chat-connection").open = true; showView("chat"); return; }
      var dialog = get("lr-fulltext-dialog");
      get("lr-fulltext-title").textContent = id + " · " + card.dataset.title;
      get("lr-fulltext-content").textContent = "";
      get("lr-fulltext-status").textContent = "正在读取提取文件…";
      dialog.showModal();
      try {
        var extracted = await api("papers/" + id + "/text");
        get("lr-fulltext-status").textContent = "PDF 文本层 · " + extracted.pages.length + " 页 · 不含图片 OCR";
        get("lr-fulltext-content").textContent = extracted.pages.map(function (page) { return "=== PDF PAGE " + page.page + " ===\n" + page.text; }).join("\n\n");
      } catch (failure) { get("lr-fulltext-status").textContent = failure.message; }
    });
    card.querySelector("summary").appendChild(fulltext);
  });
  get("lr-fulltext-close").addEventListener("click", function () { get("lr-fulltext-dialog").close(); });
  function renderList() {
    select.replaceChildren(new Option("新对话", ""));
    sessions.forEach(function (session) {
      select.add(new Option((session.busy ? "回答中 · " : "") + session.title, session.id));
    });
    select.value = activeId;
  }
  function addText(element, text) {
    var pattern = /\[(P\d{3,6})([^\]\n]{0,60})\]/g;
    var start = 0, match;
    while ((match = pattern.exec(text))) {
      element.appendChild(document.createTextNode(text.slice(start, match.index)));
      if (cards.has(match[1])) {
        var link = node("a", "", match[0]);
        link.href = "#" + match[1].toLowerCase();
        link.addEventListener("click", function () { showView("library"); });
        element.appendChild(link);
      } else element.appendChild(document.createTextNode(match[0]));
      start = pattern.lastIndex;
    }
    element.appendChild(document.createTextNode(text.slice(start)));
  }
  function renderMessages(session, force) {
    busy = !!session.busy;
    var next = JSON.stringify(session.messages);
    if (next !== signature || force) {
      var bottom = messages.scrollHeight - messages.scrollTop - messages.clientHeight < 80;
      var top = messages.scrollTop;
      messages.replaceChildren();
      if (!session.messages.length) messages.appendChild(node("p", "lr-chat-empty", "新对话"));
      session.messages.forEach(function (message) {
        var article = node("article", "lr-chat-message");
        article.dataset.role = message.role;
        var header = node("header");
        header.append(node("strong", "", message.role === "user" ? "你" : "Codex"), node("span", "", new Date(message.created_at).toLocaleString("zh-CN", { month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" })));
        var text = node("div", "lr-chat-text");
        addText(text, message.text || (message.status === "generating" ? "正在读取论文并生成回答…" : ""));
        article.append(header, text);
        if (message.error) article.appendChild(node("p", "lr-chat-warning", message.error));
        if (message.sources?.length) {
          var sources = node("details");
          sources.appendChild(node("summary", "", "本轮提供的依据"));
          message.sources.forEach(function (source) {
            sources.appendChild(node("div", "", source.id + " · " + (source.source === "pdf" ? "PDF p." + source.pages.join(", ") + " / 共 " + source.total_pages + " 页" + (source.truncated ? "（含截取页）" : "") : "仅资料库摘要，未读取 PDF 原文")));
          });
          article.appendChild(sources);
        }
        messages.appendChild(article);
      });
      signature = next;
      messages.scrollTop = force || bottom ? messages.scrollHeight : top;
    }
    if (session.storage_error) error("回答尚未保存到磁盘，请立即导出当前记录。");
    controls();
  }
  async function api(route, method, body) {
    if (!connection) throw new Error("请先连接本机服务。");
    var controller = new AbortController();
    var timer = setTimeout(function () { controller.abort(); }, 15000);
    try {
      var response = await fetch("http://127.0.0.1:" + connection.port + "/api/" + route, {
        method: method || "GET", signal: controller.signal, credentials: "omit", cache: "no-store",
        headers: Object.assign({ Authorization: "Bearer " + connection.token }, body ? { "Content-Type": "application/json" } : {}),
        body: body ? JSON.stringify(body) : undefined
      });
      var result = await response.json();
      if (!response.ok) { var failure = new Error(result.error || "本机请求失败。"); failure.status = response.status; throw failure; }
      return result;
    } catch (failure) {
      if (!failure.status || failure.status === 401) { connected = false; controls(); }
      if (!failure.status) throw new Error("未能连接本机服务。请启动本机服务并允许浏览器访问本地网络，或打开本机工作区。");
      throw failure;
    } finally { clearTimeout(timer); }
  }
  async function refreshList() {
    var currentEpoch = epoch;
    var result = await api("sessions");
    if (currentEpoch !== epoch) return;
    sessions = result.sessions; renderList();
    if (result.storage_error) error("本机磁盘保存异常，请先导出记录。");
  }
  async function loadSession(id) {
    rememberDraft();
    activeId = id; signature = ""; busy = false;
    question.value = drafts[id || "new"] || "";
    controls(); remember();
    if (!id) { renderMessages({ messages: [], busy: false }, true); renderList(); return; }
    var currentEpoch = epoch;
    try {
      var session = await api("sessions/" + id);
      if (activeId !== id || currentEpoch !== epoch) return;
      selected = new Set(session.paper_ids.filter(function (paper) { return cards.has(paper); }));
      renderScope(); renderMessages(session, true); renderList(); remember();
    } catch (failure) { error(failure.message); }
  }
  async function connect() {
    epoch += 1; var currentEpoch = epoch;
    clearTimeout(poll); error("");
    var port = Number(get("lr-bridge-port").value);
    var token = get("lr-bridge-token").value.trim();
    if (!Number.isInteger(port) || port < 1024 || port > 65535 || !/^[a-f0-9]{64}$/i.test(token)) { error("请输入有效端口和本机配对令牌。"); return; }
    connection = { port: port, token: token };
    try {
      await api("status");
      if (currentEpoch !== epoch) return;
      connected = true;
      try { sessionStorage.setItem("literature-chat:connection:v1", JSON.stringify(connection)); } catch (_) {}
      get("lr-chat-connection").open = false;
      await refreshList();
      if (activeId && sessions.some(function (session) { return session.id === activeId; })) await loadSession(activeId);
      else if (activeId) await loadSession("");
      controls(); schedulePoll();
    } catch (failure) { get("lr-chat-connection").open = true; error(failure.message); }
  }
  function schedulePoll() {
    clearTimeout(poll);
    if (!connected) return;
    poll = setTimeout(async function () {
      var id = activeId, currentEpoch = epoch;
      try {
        if (id) {
          var session = await api("sessions/" + id);
          if (activeId === id && currentEpoch === epoch) renderMessages(session, false);
        }
        await refreshList();
      } catch (failure) { error(failure.message); }
      if (currentEpoch === epoch) schedulePoll();
    }, busy ? 1000 : 5000);
  }
  get("lr-connect-form").addEventListener("submit", function (event) { event.preventDefault(); void connect(); });
  get("lr-local-workspace").addEventListener("click", function () {
    var port = connection ? connection.port : Number(get("lr-bridge-port").value);
    if (!Number.isInteger(Number(port)) || port < 1024 || port > 65535) return;
    var url = "http://127.0.0.1:" + port + "/";
    if (connection) url += "#bridge_token=" + encodeURIComponent(connection.token) + "&bridge_port=" + port;
    window.open(url, "_blank", "noopener,noreferrer");
  });
  get("lr-disconnect").addEventListener("click", function () {
    epoch += 1; connected = false; connection = null; clearTimeout(poll);
    try { sessionStorage.removeItem("literature-chat:connection:v1"); } catch (_) {}
    get("lr-bridge-token").value = ""; controls();
  });
  get("lr-chat-new").addEventListener("click", function () { error(""); void loadSession(""); });
  select.addEventListener("change", function () { error(""); void loadSession(select.value); });
  question.addEventListener("input", function () { rememberDraft(); controls(); });
  question.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !event.shiftKey && !event.isComposing) { event.preventDefault(); if (!get("lr-chat-send").disabled) get("lr-chat-form").requestSubmit(); }
  });
  get("lr-chat-form").addEventListener("submit", async function (event) {
    event.preventDefault();
    if (posting || busy || !connected || !selected.size || !question.value.trim()) return;
    var text = question.value, paperIds = Array.from(selected), currentEpoch = epoch;
    posting = true; controls(); error("");
    try {
      if (!activeId) {
        var created = await api("sessions", "POST", { title: text.trim().slice(0, 60), paper_ids: paperIds });
        if (currentEpoch !== epoch) return;
        activeId = created.id;
        drafts[activeId] = text; delete drafts.new; remember();
      }
      var id = activeId;
      var session = await api("sessions/" + id + "/messages", "POST", { text: text, paper_ids: paperIds });
      if (currentEpoch !== epoch || activeId !== id) return;
      if (question.value === text) question.value = "";
      rememberDraft(); renderMessages(session, true); await refreshList(); schedulePoll();
    } catch (failure) { error(failure.message); }
    finally { posting = false; controls(); }
  });
  get("lr-chat-stop").addEventListener("click", async function () {
    try { await api("sessions/" + activeId + "/cancel", "POST", {}); schedulePoll(); }
    catch (failure) { error(failure.message); }
  });
  get("lr-chat-rename").addEventListener("click", async function () {
    var session = sessions.find(function (session) { return session.id === activeId; });
    var title = window.prompt("会话名称", session?.title || "");
    if (!title?.trim()) return;
    try { await api("sessions/" + activeId, "PATCH", { title: title.trim() }); await refreshList(); }
    catch (failure) { error(failure.message); }
  });
  get("lr-chat-delete").addEventListener("click", async function () {
    if (!window.confirm("删除当前会话及全部提问记录？请先导出需要保留的内容。")) return;
    var id = activeId;
    try { await api("sessions/" + id, "DELETE"); delete drafts[id]; if (activeId === id) await loadSession(""); await refreshList(); }
    catch (failure) { error(failure.message); }
  });
  get("lr-chat-export").addEventListener("click", async function () {
    try {
      var backup = await api("export");
      var url = URL.createObjectURL(new Blob([JSON.stringify(backup, null, 2)], { type: "application/json;charset=utf-8" }));
      var anchor = node("a"); anchor.href = url; anchor.download = "literature-chat-" + new Date().toISOString().slice(0, 10) + ".json";
      document.body.appendChild(anchor); anchor.click(); anchor.remove(); setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
    } catch (failure) { error(failure.message); }
  });
  try {
    var previous = JSON.parse(sessionStorage.getItem("literature-chat:ui:v1") || "null");
    if (previous) {
      activeId = typeof previous.activeId === "string" ? previous.activeId : "";
      selected = new Set((Array.isArray(previous.selected) ? previous.selected : []).filter(function (id) { return cards.has(id); }).slice(0, 4));
      if (previous.drafts && typeof previous.drafts === "object") Object.entries(previous.drafts).forEach(function (item) { if (typeof item[1] === "string") drafts[item[0]] = item[1].slice(0, 12000); });
      question.value = drafts[activeId || "new"] || "";
    }
    connection = JSON.parse(sessionStorage.getItem("literature-chat:connection:v1") || "null");
  } catch (_) {}
  var params = new URLSearchParams(location.hash.slice(1));
  if (params.has("bridge_token")) {
    connection = { token: params.get("bridge_token"), port: params.get("bridge_port") || 8765 };
    history.replaceState(null, "", location.pathname + location.search);
  }
  if (connection) {
    get("lr-bridge-port").value = connection.port;
    get("lr-bridge-token").value = connection.token;
    void connect();
  }
  renderScope(); controls();
})();
