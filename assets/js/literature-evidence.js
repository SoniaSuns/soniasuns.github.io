(function () {
  "use strict";
  var element = document.getElementById("lr-evidence-data");
  if (!element) return;
  var data;
  try { data = JSON.parse(element.textContent); } catch (_) { return; }
  var section = document.getElementById("lr-evidence");
  var list = document.getElementById("lr-evidence-list");
  var detail = document.getElementById("lr-evidence-detail");
  var papers = data.papers || [];
  var byId = new Map(papers.map(function (paper) { return [paper.id, paper]; }));
  var topics = new Map((data.topics || []).map(function (topic) { return [topic.id, topic.label]; }));
  var reviews = { method_checked: "已核查方法条件", abstract_review: "摘要初读", existing_notes: "既有阅读笔记", metadata_only: "仅书目 / 待补读" };
  var search = document.getElementById("lr-evidence-search");
  var topic = document.getElementById("lr-evidence-topic");
  var review = document.getElementById("lr-evidence-review");
  var collection = document.getElementById("lr-evidence-collection");
  var state = { team: "all", page: 0, selected: "" };
  var pageSize = 8;
  var teamData = JSON.parse(document.getElementById("lr-evidence-team-data").textContent).teams;
  function esc(value) { return String(value == null ? "" : value).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function external(url, label) { return /^https?:\/\//i.test(url || "") ? '<a href="' + esc(url) + '" target="_blank" rel="noopener noreferrer">' + esc(label) + ' ↗</a>' : esc(label); }
  function badge(paper) { return '<span class="' + (paper.collected ? "lr-collected" : "lr-external") + '">● ' + (paper.collected ? "已收集 PDF" : "未收集 PDF") + '</span>'; }
  function field(label, text) { return '<div class="lr-evidence-field"><h4>' + esc(label) + '</h4><p>' + esc(text || "尚未逐项核查") + '</p></div>'; }
  function filtered() {
    var tokens = search.value.normalize("NFKC").trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    return papers.filter(function (paper) {
      return (state.team === "all" || (paper.teams || []).includes(state.team)) &&
        (topic.value === "all" || (paper.topics || []).includes(topic.value)) &&
        (review.value === "all" || paper.review_status === review.value) &&
        (collection.value === "all" || (paper.collected ? "collected" : "external") === collection.value) &&
        tokens.every(function (token) { return JSON.stringify(paper).normalize("NFKC").toLocaleLowerCase().includes(token); });
    });
  }
  function renderDetail() {
    var paper = byId.get(state.selected);
    if (!paper) { detail.innerHTML = '<p class="lr-muted">当前筛选无匹配论文。</p>'; return; }
    detail.innerHTML = '<div class="lr-evidence-detail-top">' + badge(paper) + '<span>' + esc(reviews[paper.review_status] || paper.review_status) + '</span></div>' +
      '<p class="lr-evidence-id">' + esc(paper.id + " · " + paper.year) + '</p><h3>' + esc(paper.title) + '</h3><p class="lr-evidence-authors">' + esc(paper.authors) + '</p>' +
      '<p class="lr-evidence-tags">' + (paper.topics || []).map(function (id) { return '<span>' + esc(topics.get(id) || id) + '</span>'; }).join("") + '</p>' +
      field("本篇研究的问题", paper.question) + '<p class="lr-evidence-origin">' + esc(paper.question_origin || "依据作者任务归纳，非作者明确编号的 RQ") + '</p>' +
      field("输入与任务条件", paper.input_conditions) + field("训练方式与监督", paper.training_supervision) +
      field("推理时的外部依赖 / 推演承担者", paper.inference_support) + field("作者验证了什么", paper.evaluation) +
      field("适用范围与待验证条件", paper.boundary) +
      (paper.observed_failures ? field("作者报告的失败", paper.observed_failures) : '') +
      field("证据与核查范围", paper.evidence) + '<p class="lr-evidence-origin">标注更新：' + esc(paper.checked || data.updated) + ' · 未独立复现实验</p>' +
      '<div class="lr-evidence-links">' + (paper.links || []).map(function (link) { return external(link.url, link.label); }).join(" ") +
      (paper.note ? '<a href="#' + esc(paper.note) + '">打开阅读笔记 ↓</a>' : '') +
      (paper.rqs || []).map(function (id) { return '<a href="#rq-' + esc(id) + '">' + esc(id) + ' 文献分支</a>'; }).join(" ") + '</div>';
  }
  function render() {
    var rows = filtered();
    var totalPages = Math.max(1, Math.ceil(rows.length / pageSize));
    state.page = Math.max(0, Math.min(state.page, totalPages - 1));
    var visibleRows = rows.slice(state.page * pageSize, (state.page + 1) * pageSize);
    if (!visibleRows.some(function (paper) { return paper.id === state.selected; })) state.selected = visibleRows.length ? visibleRows[0].id : "";
    list.innerHTML = visibleRows.map(function (paper) {
      return '<button type="button" class="lr-evidence-paper" data-evidence-id="' + esc(paper.id) + '" aria-pressed="' + (state.selected === paper.id) + '"><span class="lr-evidence-paper-meta">' + esc(paper.id + " · " + paper.year) + '<span>' + esc(reviews[paper.review_status] || paper.review_status) + '</span></span><strong>' + esc(paper.title) + '</strong><span class="lr-evidence-paper-bottom">' + badge(paper) + '<span>' + esc((paper.topics || []).slice(0, 2).map(function (id) { return topics.get(id) || id; }).join(" · ")) + '</span></span></button>';
    }).join("") || '<p class="lr-evidence-empty">没有匹配论文。可以清除筛选或缩短关键词。</p>';
    section.querySelectorAll("[data-evidence-team]").forEach(function (button) { button.setAttribute("aria-pressed", button.dataset.evidenceTeam === state.team); });
    document.getElementById("lr-evidence-status").textContent = rows.length + " / " + papers.length + " 篇标注 · " + rows.filter(function (paper) { return paper.collected; }).length + " 篇有本地 PDF" + (state.team === "all" ? " · 全部收藏与既有文献" : " · 当前研究者收藏");
    document.getElementById("lr-evidence-page").textContent = (state.page + 1) + " / " + totalPages;
    document.getElementById("lr-evidence-prev").disabled = state.page === 0;
    document.getElementById("lr-evidence-next").disabled = state.page >= totalPages - 1;
    renderDetail();
    var currentTeam = teamData.find(function (team) { return team.id === state.team; });
    document.getElementById("lr-team-insight").innerHTML = currentTeam ? '<h3>' + esc(currentTeam.name) + ' · 阅读脉络</h3><p>' + esc(currentTeam.assessment) + '</p><div class="lr-team-stages">' + (currentTeam.stages || []).map(function (stage) { return '<article><h4>' + esc(stage.label) + '</h4><p>' + esc(stage.question) + '</p><p>' + esc(stage.delta) + '</p><div>' + stage.papers.map(function (paper) { return '<a href="#evidence-' + esc(paper.id) + '">' + esc(paper.title.split(':')[0]) + '</a>'; }).join(' → ') + '</div></article>'; }).join('') + '</div><small>以上为问题对照的阅读路径；直接引用关系另见完整脉络图。</small>' : '<p>默认优先显示已核查方法的重点论文。点击研究者可查看该收藏的阅读路径；同篇合著论文只计一个主记录。</p>';
  }
  function reset() { state.team = "all"; state.page = 0; search.value = ""; topic.value = review.value = collection.value = "all"; }
  section.addEventListener("click", function (event) {
    var button = event.target.closest("button");
    if (!button) return;
    if (button.dataset.evidenceTeam) { state.team = state.team === button.dataset.evidenceTeam ? "all" : button.dataset.evidenceTeam; state.page = 0; render(); }
    if (button.dataset.evidenceId) { state.selected = button.dataset.evidenceId; render(); history.replaceState(null, "", "#evidence-" + state.selected); if (window.innerWidth < 900) { detail.scrollIntoView({ block: "start" }); detail.focus({ preventScroll: true }); } }
  });
  search.addEventListener("input", function () { state.page = 0; render(); });
  [topic, review, collection].forEach(function (input) { input.addEventListener("change", function () { state.page = 0; render(); }); });
  document.getElementById("lr-evidence-filters").addEventListener("submit", function (event) { event.preventDefault(); });
  document.getElementById("lr-evidence-reset").addEventListener("click", function () { reset(); render(); });
  document.getElementById("lr-evidence-prev").addEventListener("click", function () { state.page--; render(); });
  document.getElementById("lr-evidence-next").addEventListener("click", function () { state.page++; render(); });
  function openHash() {
    var match = window.location.hash.match(/^#evidence-([\w-]+)$/);
    if (!match || !byId.has(match[1])) return;
    var selected = byId.get(match[1]);
    if (state.team !== "all" && !(selected.teams || []).includes(state.team)) reset();
    search.value = ""; topic.value = review.value = collection.value = "all";
    state.selected = match[1]; state.page = Math.floor(filtered().findIndex(function (paper) { return paper.id === state.selected; }) / pageSize); render();
    requestAnimationFrame(function () { section.scrollIntoView({ block: "start" }); });
  }
  window.addEventListener("hashchange", openHash);
  render(); openHash();
})();
