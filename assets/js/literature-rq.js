(function () {
  "use strict";
  var atlas = document.getElementById("lr-rq-atlas");
  var dataElement = document.getElementById("lr-rq-data");
  if (!atlas || !dataElement) return;
  var data;
  try { data = JSON.parse(dataElement.textContent); } catch (_) { return; }
  var papers = new Map(data.papers.map(function (p) { return [p.id, p]; }));
  var branches = new Map(data.branches.map(function (b) { return [b.id, b]; }));
  var parents = new Map(data.parents.map(function (p) { return [p.id, p]; }));
  var edges = new Map(data.edges.map(function (e) { return [e.id, e]; }));
  var state = { route: "world", view: "tree", selection: "W1b", parent: "all", query: "", collection: "all" };
  var visual = document.getElementById("rq-visual");
  var detail = document.getElementById("rq-detail");
  var search = document.getElementById("rq-search");
  var parentSelect = document.getElementById("rq-parent");
  var collectionSelect = document.getElementById("rq-collection");
  function esc(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function link(url, label) {
    if (!/^https?:\/\//i.test(url || "")) return esc(label);
    return '<a href="' + esc(url) + '" target="_blank" rel="noopener noreferrer">' + esc(label) + " ↗</a>";
  }
  function textMatch(value) {
    var text = String(value).normalize("NFKC").toLocaleLowerCase();
    return state.query.normalize("NFKC").trim().toLocaleLowerCase().split(/\s+/).filter(Boolean).every(function (q) { return text.includes(q); });
  }
  function collectionMatch(p) { return state.collection === "all" || (p.collected ? "collected" : "external") === state.collection; }
  function paperMatch(p, b) {
    var context = b ? [b.id, b.question, b.label, b.before, b.after].join(" ") : "";
    return collectionMatch(p) && textMatch([p.id, p.title, p.authors, p.summary, p.sources.join(" "), context].join(" "));
  }
  function paperButton(id, full) {
    var p = papers.get(id);
    if (!p) return "";
    return '<button type="button" class="rq-paper-button" data-paper="' + esc(id) + '" data-collected="' + p.collected + '" title="' + esc(p.title) + '">' + esc(id) + " · " + esc(full ? p.title : p.short) + (full ? '<br><small>' + esc(p.year) + " · " + (p.collected ? "已收集" : "未收集") + "</small>" : "") + "</button>";
  }
  function sourceButtons(ids) { return '<div class="rq-source-buttons">' + ids.map(function (i) { return paperButton(i, false); }).join("") + "</div>"; }
  function rqButton(id) {
    var b = branches.get(id);
    return b ? '<button type="button" class="rq-link-button" data-rq="' + esc(id) + '">' + esc(id + " " + b.label) + "</button>" : "";
  }
  function branchPapers(b) { return b.core.concat(b.support).map(function (i) { return papers.get(i); }).filter(function (p) { return paperMatch(p, b); }); }
  function routeBranches() { return data.branches.filter(function (b) { return b.route === state.route && (state.parent === "all" || b.parent === state.parent); }); }
  function year(p) { var match = p.year.match(/(?:19|20)\d\d/); return match ? Number(match[0]) : 9999; }
  function paperList(list, b) {
    return list.slice().sort(function (a, c) { return year(a) - year(c) || a.id.localeCompare(c.id); }).map(function (p) {
      var isSupport = b && b.support.includes(p.id);
      return '<div class="rq-paper-row">' + paperButton(p.id, true) + '<small>' + (isSupport ? "方法 / 场景支撑" : "直接研究 / 问题来源") + "</small><p>" + esc(p.summary) + "</p></div>";
    }).join("");
  }
  function renderSummary() {
    var r = data.routes.find(function (r) { return r.id === state.route; });
    document.getElementById("rq-route-summary").innerHTML = '<div class="rq-root"><span class="rq-id">' + r.root + ' · 核心 RQ · 综合归纳</span><h3>' + esc(r.question) + "</h3><p>" + esc(r.explanation) + "</p><p><strong>怎样判断进展：</strong>" + esc(r.metrics) + "</p>" + sourceButtons(r.anchors) + "</div>";
    atlas.querySelectorAll("[data-rq-route]").forEach(function (button) { button.setAttribute("aria-pressed", button.dataset.rqRoute === state.route); });
    atlas.querySelectorAll("[data-rq-view]").forEach(function (button) { button.setAttribute("aria-pressed", button.dataset.rqView === state.view); });
    parentSelect.innerHTML = '<option value="all">全部重要问题</option>' + data.parents.filter(function (p) { return p.route === state.route; }).map(function (p) { return '<option value="' + p.id + '">' + esc(p.id + " " + p.label) + "</option>"; }).join("");
    parentSelect.value = state.parent;
  }
  function renderTree() {
    var active = routeBranches();
    visual.innerHTML = '<div class="rq-tree">' + data.parents.filter(function (p) { return p.route === state.route && (state.parent === "all" || p.id === state.parent); }).map(function (p) {
      var rootId = state.route === "world" ? "W0" : "X0";
      return '<div class="rq-column"><div class="rq-parent"><span class="rq-id">' + rootId + " → " + p.id + ' · 重要 RQ</span><h3>' + esc(p.label) + "</h3><p>" + esc(p.question) + '</p><button type="button" class="rq-more" data-parent-source="' + p.id + '">查看问题来源 · ' + p.anchors.length + ' 篇 →</button></div><div class="rq-branch-list">' + active.filter(function (b) { return b.parent === p.id; }).map(function (b) {
        var list = branchPapers(b);
        var collected = list.filter(function (p) { return p.collected; }).length;
        var examples = b.anchors.filter(function (id) { return list.some(function (p) { return p.id === id; }); }).slice(0, 3);
        if (!examples.length) examples = list.slice(0, 3).map(function (p) { return p.id; });
        return '<div class="rq-branch-wrap"><button id="rq-' + b.id + '" type="button" class="rq-node' + (!list.length ? " rq-node-empty" : "") + '" data-rq="' + b.id + '" aria-pressed="' + (state.selection === b.id) + '"><span class="rq-id">' + b.id + '</span><strong>' + esc(b.label) + '</strong><span class="rq-node-question">' + esc(b.question) + "</span><small>" + collected + " 已收集 · " + (list.length-collected) + " 未收集</small></button>" + (list.length ? '<div class="rq-mini-papers">' + examples.map(function (i) { return paperButton(i, false); }).join("") + (list.length > examples.length ? '<button type="button" class="rq-more" data-rq="' + b.id + '">查看全部 ' + list.length + " 篇 →</button>" : "") + "</div>" : "") + "</div>";
      }).join("") + "</div></div>";
    }).join("") + "</div>";
  }
  function renderLineage() {
    var lanes = data.lanes.filter(function (l) {
      var b = branches.get(l.rq);
      return l.route === state.route && (state.parent === "all" || b.parent === state.parent) && l.papers.some(function (id) { return paperMatch(papers.get(id), b); });
    });
    visual.innerHTML = '<p class="rq-muted" style="font-size:12px">箭头从被引用论文指向引用它的论文。点击箭头看证据；为保留链条上下文，匹配路线中的中间论文会一并显示。</p>' + (lanes.length ? lanes.map(function (l) {
      return '<article class="rq-lane"><h3>' + esc(l.title) + "</h3>" + rqButton(l.rq) + '<div class="rq-lane-chain">' + l.papers.map(function (id, index) {
        var e = index ? edges.get(l.papers[index-1] + "-" + id) : null;
        return (e ? '<button type="button" class="rq-edge" data-edge="' + e.id + '" data-kind="' + e.kind + '">' + esc(e.change) + " · " + (e.kind === "citation" ? "引用已核实" : "综合 / 对照") + "</button>" : "") + paperButton(id, true);
      }).join("") + "</div></article>";
    }).join("") : '<div class="rq-overview">当前条件没有对应的承接链。可清除筛选，或在 RQ 层级图中查看这一分支全部论文。</div>');
  }
  function renderBridges() {
    visual.innerHTML = '<div class="rq-overview"><p>下面是基于已有证据提出的候选研究问题，属于本图综合。它们仍需进一步检索和实验验证，不能当作已经确认的“无人研究空白”。</p></div>' + data.bridges.map(function (b) {
      return '<article class="rq-overview"><span class="rq-id">' + b.id + ' · 候选 RQ</span><h3>' + esc(b.title) + '</h3><p><strong>' + esc(b.question) + '</strong></p><p>' + b.rqs.map(rqButton).join(" · ") + '</p><p><strong>已有工作：</strong>' + esc(b.known) + '</p><p><strong>进一步改变的条件：</strong>' + esc(b.delta) + '</p><p><strong>可验证方式：</strong>' + esc(b.test) + "</p>" + sourceButtons(b.papers) + "</article>";
    }).join("");
  }
  function renderCoverage() {
    var c = data.coverage;
    var rows = data.papers.filter(function (p) {
      return collectionMatch(p) && textMatch([p.id, p.title, p.authors, p.summary, p.sources.join(" "), p.mappings.map(function (m) { var b=branches.get(m.rq); return b.id+" "+b.question; }).join(" ")].join(" "));
    });
    visual.innerHTML = '<div class="rq-overview"><div class="rq-metric-strip"><span><strong>' + c.local_documents + '</strong>活跃本地 PDF / 全部已映射</span><span><strong>' + c.external_papers + '</strong>未收集 PDF / 外部补充</span><span><strong>' + data.branches.length + '</strong>RQ 分支</span></div><p>核对日期 ' + esc(data.updated) + "。下表覆盖所有路线；状态与搜索筛选适用于论文总表。归档重复/旧版本 " + (c.archived_duplicates || 0) + " 份不重复计数，原编号保留别名。蓝色判断基于本地文件，不基于是否读过在线摘要。</p>" + '<table class="rq-coverage-table"><thead><tr><th scope="col">文献目录</th><th scope="col">活跃 PDF</th><th scope="col">已映射文献</th></tr></thead><tbody>' + c.folders.map(function (f) { return "<tr><td>" + esc(f.name) + "</td><td>" + f.files + "</td><td>" + f.documents + "</td></tr>"; }).join("") + '</tbody></table><h3 style="margin-top:18px">辅助材料如何使用</h3>' + c.supplements.map(function (s) { return '<p><strong>' + esc(s.path) + "</strong><br>" + esc(s.use) + "</p>"; }).join("") + '</div><div class="rq-overview"><h3>逐篇落点 · ' + rows.length + ' 条</h3><div class="rq-table-scroll"><table class="rq-coverage-table"><thead><tr><th scope="col">论文 / 收集状态</th><th scope="col">RQ 分支</th></tr></thead><tbody>' + rows.map(function (p) { return '<tr><td>' + paperButton(p.id, true) + '<br><small>' + esc(p.collected ? p.sources.join("；") : "发现自 " + p.seed + " · 第 " + p.depth + " 轮") + '</small></td><td>' + p.mappings.map(function (m) { return '<div>' + rqButton(m.rq) + (m.role === "support" ? "（支撑）" : "") + '</div>'; }).join("") + '</td></tr>'; }).join("") + '</tbody></table></div></div>';
  }
  function evidenceCard(e) {
    return '<div class="rq-evidence"><span class="rq-id">' + esc(e.source + (e.kind === "citation" ? " → " : " ⇢ ") + e.target) + " · " + (e.kind === "citation" ? "引用已核实" : "综合关联 / 并行对照") + '</span><p>' + esc(e.change) + '</p><p class="rq-muted">依据：' + esc(e.evidence) + '</p>' + (e.url ? link(e.url, "查阅引用方原文") : "") + '</div>';
  }
  function renderDetail() {
    var b = branches.get(state.selection);
    var p = papers.get(state.selection);
    var e = edges.get(state.selection);
    var important = parents.get(state.selection);
    if (b) {
      var parent = parents.get(b.parent);
      var list = branchPapers(b);
      detail.innerHTML = '<span class="rq-id">' + esc((b.route === "world" ? "W0" : "X0") + " → " + b.parent + " → " + b.id) + '</span><p class="rq-muted">属于：' + esc(parent.question) + '</p><h3>' + esc(b.question) + '</h3><div class="rq-change"><span>原先的条件 / 角度</span>' + esc(b.before) + '<span>↓ 改变为</span>' + esc(b.after) + '</div><h4>问题来源</h4><p class="rq-muted">' + esc(b.rq_origin) + '。下列论文提供任务定义、方法或明确的局限：</p>' + sourceButtons(b.anchors) + '<h4>尚未跨过的边界</h4><p class="rq-gap">' + esc(b.gap) + '</p><h4>论文怎样落在这个分支 · ' + list.length + ' 篇</h4>' + (list.length ? paperList(list, b) : '<p>当前筛选下无匹配论文。重置筛选即可查看。</p>');
    } else if (important) {
      detail.innerHTML = '<span class="rq-id">' + (important.route === 'world' ? 'W0' : 'X0') + ' → ' + important.id + ' · 重要 RQ</span><h3>' + esc(important.question) + '</h3><p class="rq-muted">本图将这些工作讨论的问题综合成这一层。它是组织文献的框架，不是某一篇作者给出的统一命名。</p><h4>问题来源</h4>' + sourceButtons(important.anchors) + '<h4>进一步拆分</h4>' + data.branches.filter(function (branch) { return branch.parent === important.id; }).map(function (branch) { return '<p>' + rqButton(branch.id) + '<br>' + esc(branch.question) + '</p>'; }).join('');
    } else if (p) {
      var related = data.edges.filter(function (edge) { return edge.source === p.id || edge.target === p.id; });
      var sources = p.sources.length ? '<h4>本地文件</h4><ul>' + p.sources.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join("") + '</ul>' : '<p class="rq-provenance">从 ' + esc(p.seed) + ' 的引用/线索发现 · 第 ' + p.depth + ' 轮检索。尚未收集 PDF；在线查阅不改变这一状态。</p>';
      detail.innerHTML = '<span class="rq-badge' + (p.collected ? "" : " external") + '">' + (p.collected ? "已收集 PDF" : "未收集 PDF") + '</span><h3 class="rq-paper-title">' + esc(p.id + " · " + p.title) + '</h3><p class="rq-muted">' + esc(p.authors + " · " + p.year) + '</p>' + (p.note ? '<p><a href="#' + p.note + '">打开完整阅读笔记 ↓</a></p>' : '') + p.links.map(function (l) { return '<p>' + link(l.url,l.label) + '</p>'; }).join("") + '<h4>研究切入与实现</h4><p>' + esc(p.summary) + '</p><h4>对应 RQ 分支</h4>' + p.mappings.map(function (m) { return '<p>' + rqButton(m.rq) + ' · ' + (m.role === "core" ? "直接研究 / 问题来源" : "方法 / 场景支撑") + '</p>'; }).join("") + '<h4>适用边界</h4><p class="rq-gap">' + esc(p.boundary) + '</p><h4>来源与核验</h4><p class="rq-provenance">' + esc(p.evidence) + '</p><p class="rq-muted">记录核查日期：' + esc(p.verified || "沿用既有笔记") + '；本次重新检查关键承接边，不表示重做全部论文实验。</p>' + sources + (p.aliases.length ? '<p class="rq-muted">历史别名：' + esc(p.aliases.join("、")) + '，已合并至当前版本。</p>' : '') + '<h4>与其他论文的关系 · ' + related.length + '</h4>' + (related.length ? related.map(function (edge) { return evidenceCard(edge) + sourceButtons([edge.source === p.id ? edge.target : edge.source]); }).join("") : '<p class="rq-muted">本轮已映射到 RQ；尚未为这篇核验单独的引用承接边。没有连线不表示它没有前作。</p>');
    } else if (e) {
      detail.innerHTML = '<span class="rq-id">关系证据</span><h3>' + esc(papers.get(e.source).short) + (e.kind === "citation" ? ' → ' : ' ⇢ ') + esc(papers.get(e.target).short) + '</h3>' + sourceButtons([e.source, e.target]) + evidenceCard(e) + '<p class="rq-muted" style="margin-top:16px">“被引用”是文献事实；“改变了什么条件”是本图的比较归纳。相关工作引用可能是对照、基础或反例，不必然是算法继承。</p>';
    }
    if (p && p.research_question) {
      var questionBlock = document.createElement('div');
      questionBlock.innerHTML = '<h4>本篇 RQ · ' + esc(p.research_question.kind) + '</h4><p>' + esc(p.research_question.text) + '</p><p class="rq-muted">' + esc(p.research_question.location) + '</p>';
      detail.insertBefore(questionBlock, detail.querySelector('h4'));
    }
  }
  function render() {
    renderSummary();
    if (state.view === "tree") renderTree();
    if (state.view === "lineage") renderLineage();
    if (state.view === "coverage") renderCoverage();
    if (state.view === "bridges") renderBridges();
    renderDetail();
    var ids = new Set();
    routeBranches().forEach(function (b) { branchPapers(b).forEach(function (p) { ids.add(p.id); }); });
    var local = Array.from(ids).filter(function (i) { return papers.get(i).collected; }).length;
    document.getElementById("rq-status").textContent = (state.view === "coverage" || state.view === "bridges") ? "当前视图跨两条路线 · " + data.coverage.local_documents + " 篇本地文献 + " + data.coverage.external_papers + " 篇外部补充 · 更新 " + data.updated : "当前路线与筛选：" + local + " 篇已收集 + " + (ids.size-local) + " 篇未收集 · 同一论文可支撑多个 RQ，数量去重 · " + routeBranches().length + " 个分支";
  }
  function select(id, changeHash, scroll) {
    id = data.coverage.historical_aliases[id] || id;
    var b = branches.get(id);
    var p = papers.get(id);
    if (!b && !p && !edges.has(id) && !parents.has(id)) return;
    if (parents.has(id) && parents.get(id).route !== state.route) { state.route = parents.get(id).route; state.parent = 'all'; }
    if (b && b.route !== state.route) { state.route = b.route; state.parent = "all"; }
    if (b && state.parent !== "all" && state.parent !== b.parent) state.parent = "all";
    if (p && !p.mappings.some(function (m) { return branches.get(m.rq).route === state.route; })) {
      state.route = branches.get(p.mappings[0].rq).route;
      state.parent = "all";
    }
    state.selection = id;
    render();
    detail.scrollTop = 0;
    if (scroll) detail.focus({ preventScroll: true });
    if (changeHash) history.replaceState(null, "", "#rq-" + encodeURIComponent(id));
    if (scroll && window.matchMedia("(max-width: 760px)").matches) detail.scrollIntoView({block:"start",behavior:"smooth"});
  }
  atlas.addEventListener("click", function (event) {
    var button = event.target.closest("button");
    if (!button) return;
    if (button.dataset.rqRoute) {
      state.route = button.dataset.rqRoute;
      state.parent = "all";
      state.selection = state.route === "world" ? "W1b" : "X2b";
      select(state.selection, true, false);
    } else if (button.dataset.rqView) {
      state.view = button.dataset.rqView;
      render();
    } else if (button.dataset.rq) {
      if (state.view === "bridges" || state.view === "coverage") state.view = "tree";
      select(button.dataset.rq, true, true);
    } else if (button.dataset.paper) select(button.dataset.paper, true, true);
    else if (button.dataset.parentSource) select(button.dataset.parentSource, true, true);
    else if (button.dataset.edge) select(button.dataset.edge, true, true);
  });
  search.addEventListener("input", function () { state.query = search.value; render(); });
  collectionSelect.addEventListener("change", function () { state.collection = this.value; render(); });
  parentSelect.addEventListener("change", function () {
    state.parent = this.value;
    if (state.parent !== "all") state.selection = data.branches.find(function (b) { return b.parent === state.parent; }).id;
    render();
  });
  document.getElementById("rq-reset").addEventListener("click", function () {
    state.query = search.value = "";
    state.collection = collectionSelect.value = "all";
    state.parent = "all";
    render();
  });
  function readHash() {
    if (!window.location.hash.startsWith("#rq-")) return;
    try { select(decodeURIComponent(window.location.hash.slice(4)), false, false); } catch (_) { /* Ignore invalid fragment. */ }
  }
  window.addEventListener("hashchange", readHash);
  render();
  readHash();
})();
