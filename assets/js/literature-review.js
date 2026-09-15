(function () {
  "use strict";
  var root = document.getElementById("literature-review");
  if (!root) return;
  var list = document.getElementById("lr-papers");
  var cards = Array.from(list.querySelectorAll(".lr-paper"));
  var search = document.getElementById("lr-search");
  var topic = document.getElementById("lr-topic");
  var year = document.getElementById("lr-year");
  var priority = document.getElementById("lr-priority");
  var sort = document.getElementById("lr-sort");
  var recent = document.getElementById("lr-new");
  var texts = new Map(
    cards.map(function (card) {
      return [card, card.textContent.normalize("NFKC").toLocaleLowerCase()];
    })
  );
  var aliases = { p003: "p002", p082: "p081", p109: "p103" };
  var timer;

  function filter() {
    var tokens = search.value.normalize("NFKC").trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    var count = 0;
    cards.forEach(function (card) {
      var data = card.dataset;
      var visible =
        tokens.every(function (token) {
          return texts.get(card).includes(token);
        }) &&
        (topic.value === "all" || data.topics.split(" ").includes(topic.value)) &&
        (year.value === "all" || data.years.split(" ").includes(year.value)) &&
        (!priority || priority.value === "all" || data.priority === priority.value) &&
        (!recent.checked || data.new === "true");
      card.hidden = !visible;
      if (visible) count += 1;
    });
    document.getElementById("lr-count").textContent = count + " / " + cards.length + " 份笔记";
    document.getElementById("lr-empty").hidden = count !== 0;
  }

  function order() {
    var ordered = cards.slice().sort(function (a, b) {
      if (sort.value === "title") return a.dataset.title.localeCompare(b.dataset.title, "en");
      if (sort.value === "year") return Number(b.dataset.year) - Number(a.dataset.year) || b.id.localeCompare(a.id);
      if (sort.value === "id") return a.id.localeCompare(b.id);
      return b.id.localeCompare(a.id);
    });
    var fragment = document.createDocumentFragment();
    ordered.forEach(function (card) {
      fragment.appendChild(card);
    });
    list.appendChild(fragment);
  }

  function reset() {
    clearTimeout(timer);
    search.value = "";
    topic.value = year.value = "all";
    if (priority) priority.value = "all";
    recent.checked = false;
    filter();
  }

  function openHash() {
    var id;
    try {
      id = decodeURIComponent(window.location.hash.slice(1));
    } catch (_) {
      return;
    }
    if (!id) return;
    var target = document.getElementById(aliases[id] || id);
    if (!target || !root.contains(target)) return;
    if (target.classList.contains("lr-paper") && target.hidden) reset();
    var cursor = target;
    while (cursor && cursor !== root) {
      if (cursor.tagName === "DETAILS") cursor.open = true;
      cursor = cursor.parentElement;
    }
    requestAnimationFrame(function () {
      target.scrollIntoView({ block: "start" });
    });
  }

  search.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(filter, 120);
  });
  [topic, year, priority, recent].filter(Boolean).forEach(function (control) {
    control.addEventListener("change", filter);
  });
  sort.addEventListener("change", order);
  document.getElementById("lr-filters").addEventListener("submit", function (event) {
    event.preventDefault();
    filter();
  });
  document.getElementById("lr-reset").addEventListener("click", function () {
    reset();
    search.focus();
  });
  document.getElementById("lr-collapse").addEventListener("click", function () {
    cards.forEach(function (card) {
      card.open = false;
    });
  });
  root.addEventListener("click", function (event) {
    var anchor = event.target.closest("a[href^='#']");
    if (!anchor) return;
    if (anchor.hash === window.location.hash) setTimeout(openHash, 0);
  });
  window.addEventListener("hashchange", openHash);
  filter();
  openHash();
})();
