(function () {
  "use strict";
  var section = document.getElementById("lr-synthesis");
  if (!section) return;
  var panels = Array.from(section.querySelectorAll("[data-ls-panel]"));
  var buttons = Array.from(section.querySelectorAll("[data-ls-view]"));
  var filter = document.getElementById("ls-stage-filter");
  var cards = Array.from(section.querySelectorAll("[data-ls-stages]"));

  function show(view, updateHash) {
    if (!panels.some(function (panel) { return panel.dataset.lsPanel === view; })) return;
    panels.forEach(function (panel) { panel.hidden = panel.dataset.lsPanel !== view; });
    buttons.forEach(function (button) { button.setAttribute("aria-pressed", String(button.dataset.lsView === view)); });
    if (updateHash) history.replaceState(null, "", "#synthesis-" + view);
  }
  function readHash() {
    var view = location.hash.replace(/^#synthesis-/, "");
    if (panels.some(function (panel) { return panel.dataset.lsPanel === view; })) {
      show(view, false);
      document.getElementById("synthesis-" + view).scrollIntoView({ block: "start" });
    }
  }
  buttons.forEach(function (button) {
    button.addEventListener("click", function () { show(button.dataset.lsView, true); });
  });
  filter.addEventListener("change", function () {
    var count = 0;
    cards.forEach(function (card) {
      card.hidden = filter.value !== "all" && !card.dataset.lsStages.split(" ").includes(filter.value);
      if (!card.hidden) count += 1;
    });
    document.getElementById("ls-progress-status").textContent = count + " / " + cards.length + " 条脉络 · 同一工作可以支撑多类问题";
  });
  section.addEventListener("click", function (event) {
    var link = event.target.closest('a[href^="#rq-"]');
    if (!link) return;
    // The atlas renders paper details dynamically, so paper hashes have no static anchor.
    requestAnimationFrame(function () {
      var detail = document.getElementById("rq-detail");
      if (detail) {
        detail.scrollIntoView({ block: "start" });
        detail.focus({ preventScroll: true });
      }
    });
  });
  section.querySelector(".ls-controls").hidden = false;
  section.querySelector(".ls-stage-filter").hidden = false;
  show("progress", false);
  window.addEventListener("hashchange", readHash);
  readHash();
})();
