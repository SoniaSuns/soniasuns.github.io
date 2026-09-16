(function () {
  "use strict";
  var root = document.getElementById("literature-review");
  if (!root) return;
  var prefix = "literature-review:personal-note:v1:";
  var maxLength = 100000;
  var entries = new Map();
  var initialized = false;
  var message = document.getElementById("lr-notes-message");
  var aliases = { P003: "P002", P082: "P081", P109: "P103" };

  // Lucide icon paths; license is distributed in lucide-LICENSE.txt.
  var icons = {
    download: ["M12 15V3", "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4", "m7 10 5 5 5-5"],
    upload: ["M12 3v12", "m17 8-5-5-5 5", "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"],
    trash: ["M10 11v6", "M14 11v6", "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6", "M3 6h18", "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"]
  };
  function addIcon(button, name) {
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    var attrs = { viewBox: "0 0 24 24", width: "18", height: "18", fill: "none", stroke: "currentColor", "stroke-width": "2", "stroke-linecap": "round", "stroke-linejoin": "round", "aria-hidden": "true" };
    Object.keys(attrs).forEach(function (key) { svg.setAttribute(key, attrs[key]); });
    icons[name].forEach(function (d) {
      var path = document.createElementNS(ns, "path");
      path.setAttribute("d", d);
      svg.appendChild(path);
    });
    button.prepend(svg);
  }
  function element(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }
  function announce(text) {
    message.textContent = text;
    message.hidden = !text;
  }
  function decode(raw) {
    if (raw === null) return { text: "", updated_at: null };
    var record = JSON.parse(raw);
    if (!record || record.version !== 1 || typeof record.text !== "string" || record.text.length > maxLength || typeof record.updated_at !== "string" || !Number.isFinite(Date.parse(record.updated_at))) {
      throw new Error("Invalid stored note");
    }
    return record;
  }
  function publish(entry) {
    var hasText = !!entry.input.value.trim();
    entry.card.dataset.hasNote = String(hasText);
    entry.card.dataset.noteSearch = entry.input.value.normalize("NFKC").toLocaleLowerCase();
    entry.badge.hidden = !hasText;
    entry.indicator.textContent = hasText ? "有内容" : "未添加";
    if (initialized) root.dispatchEvent(new Event("lr-notes-changed"));
  }
  function failure(entry, text) {
    entry.status.textContent = text;
    entry.status.classList.add("lr-note-error");
    entry.recovery.hidden = false;
  }
  function load(entry) {
    try {
      var raw = localStorage.getItem(prefix + entry.id);
      var record = decode(raw);
      entry.raw = raw;
      entry.input.value = record.text;
      entry.updated = record.updated_at;
      entry.dirty = false;
      entry.blocked = false;
      entry.recovery.hidden = true;
      entry.status.classList.remove("lr-note-error");
      entry.status.textContent = record.text ? "已保存到此浏览器" : "尚无个人笔记";
      publish(entry);
    } catch (_) {
      entry.blocked = true;
      failure(entry, "无法读取本地笔记，原有数据未被覆盖。");
      announce("部分笔记无法读取。请保留备份，勿清除浏览器数据。");
    }
  }
  function save(entry, force) {
    entry.dirty = true;
    publish(entry);
    try {
      var current = localStorage.getItem(prefix + entry.id);
      if (!force && (entry.blocked || current !== entry.raw)) {
        failure(entry, "尚未保存：本地内容已变化或无法读取。请选择保留的版本。");
        return false;
      }
      if (entry.input.value.length > maxLength) throw new Error("Note too long");
      var updated = new Date().toISOString();
      var raw = JSON.stringify({ version: 1, text: entry.input.value, updated_at: updated });
      // A key per paper avoids overwriting edits to other papers in another tab.
      localStorage.setItem(prefix + entry.id, raw);
      entry.raw = raw;
      entry.updated = updated;
      entry.dirty = false;
      entry.blocked = false;
      entry.recovery.hidden = true;
      entry.status.classList.remove("lr-note-error");
      entry.status.textContent = "已保存到此浏览器";
      return true;
    } catch (_) {
      failure(entry, "未保存：浏览器存储不可用或已满。请导出备份。");
      return false;
    }
  }

  root.querySelectorAll(".lr-paper").forEach(function (card) {
    var panel = element("details", "lr-personal-note");
    var summary = element("summary", "", "我的笔记");
    var indicator = element("span", "lr-note-indicator", "未添加");
    summary.appendChild(indicator);
    panel.appendChild(summary);
    var body = element("div", "lr-note-editor");
    var label = element("label", "lr-note-label", card.dataset.id + " · 个人笔记");
    var input = element("textarea", "lr-note-input");
    input.id = "lr-personal-" + card.id;
    input.rows = 6;
    input.maxLength = maxLength;
    input.spellcheck = false;
    label.htmlFor = input.id;
    var footer = element("div", "lr-note-footer");
    var status = element("span", "lr-note-status");
    status.setAttribute("role", "status");
    var clear = element("button", "lr-note-clear");
    clear.type = "button";
    clear.title = "清空此篇个人笔记";
    clear.setAttribute("aria-label", card.dataset.id + "：清空个人笔记");
    addIcon(clear, "trash");
    footer.append(status, clear);
    var recovery = element("div", "lr-note-recovery");
    recovery.hidden = true;
    var keep = element("button", "", "保存当前编辑");
    var reload = element("button", "", "载入已保存内容");
    keep.type = reload.type = "button";
    recovery.append(keep, reload);
    body.append(label, input, footer, recovery);
    panel.appendChild(body);
    card.querySelector(".lr-paper-body").prepend(panel);
    var badge = element("span", "lr-personal-badge", "有个人笔记");
    badge.hidden = true;
    card.querySelector(".lr-badges").appendChild(badge);
    var entry = { id: card.dataset.id, card: card, input: input, indicator: indicator, badge: badge, status: status, recovery: recovery, dirty: false, raw: null, updated: null, blocked: false };
    entries.set(entry.id, entry);
    input.addEventListener("input", function () { save(entry, false); });
    clear.addEventListener("click", function () {
      if (window.confirm("清空 " + entry.id + " 的个人笔记？此操作无法撤销。")) {
        input.value = "";
        save(entry, false);
      }
    });
    keep.addEventListener("click", function () {
      if (window.confirm("用当前编辑替换此篇已保存的内容？")) save(entry, true);
    });
    reload.addEventListener("click", function () {
      if (!entry.dirty || window.confirm("放弃此篇尚未保存的编辑，载入已保存内容？")) load(entry);
    });
    load(entry);
  });
  initialized = true;
  document.getElementById("lr-notes-toolbar").hidden = false;
  document.getElementById("lr-noted-filter").hidden = false;
  root.dispatchEvent(new Event("lr-notes-changed"));

  var exportButton = document.getElementById("lr-notes-export");
  var importButton = document.getElementById("lr-notes-import");
  var fileInput = document.getElementById("lr-notes-file");
  addIcon(exportButton, "download");
  addIcon(importButton, "upload");
  exportButton.addEventListener("click", function () {
    var notes = [];
    var unreadable = 0;
    entries.forEach(function (entry) {
      if (!entry.dirty) load(entry);
      if (entry.blocked) unreadable += 1;
      if (!entry.input.value.trim()) return;
      notes.push({ paper_id: entry.id, paper_title: entry.card.dataset.title, text: entry.input.value, updated_at: entry.updated || new Date().toISOString(), unsaved: entry.dirty });
    });
    var backup = { format: "literature-review-personal-notes", version: 1, exported_at: new Date().toISOString(), notes: notes };
    var url = URL.createObjectURL(new Blob([JSON.stringify(backup, null, 2)], { type: "application/json;charset=utf-8" }));
    var anchor = element("a");
    anchor.href = url;
    anchor.download = "literature-personal-notes-" + new Date().toISOString().slice(0, 10) + ".json";
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
    announce("已导出 " + notes.length + " 篇个人笔记（含未保存编辑）。" + (unreadable ? "另有 " + unreadable + " 篇原有数据无法读取，未包含在备份中。" : ""));
  });
  importButton.addEventListener("click", function () { fileInput.click(); });
  fileInput.addEventListener("change", function () {
    var file = fileInput.files[0];
    fileInput.value = "";
    if (!file) return;
    if (file.size > 10 * 1024 * 1024) { announce("备份超过10 MB，未导入。"); return; }
    file.text().then(function (text) {
      var backup = JSON.parse(text);
      if (!backup || backup.format !== "literature-review-personal-notes" || backup.version !== 1 || !Array.isArray(backup.notes) || backup.notes.length > 10000) throw new Error("Invalid backup");
      var seen = new Set();
      var unknown = 0;
      var plans = [];
      // Validate the entire backup before changing any draft or stored note.
      backup.notes.forEach(function (note) {
        if (!note || typeof note.paper_id !== "string" || !/^P\d{3,6}$/.test(note.paper_id) || typeof note.text !== "string" || note.text.length > maxLength || typeof note.updated_at !== "string" || !Number.isFinite(Date.parse(note.updated_at))) throw new Error("Invalid note");
        var id = aliases[note.paper_id] || note.paper_id;
        if (seen.has(id)) throw new Error("Duplicate note");
        seen.add(id);
        if (!entries.has(id)) { unknown += 1; return; }
        var entry = entries.get(id);
        if (!entry.dirty) load(entry);
        var current = entry.input.value;
        if (!note.text.trim() || current === note.text) return;
        var section = "\n\n--- 导入备份 " + note.updated_at + " ---\n\n" + note.text;
        if (current.includes(section)) return;
        var merged = current.trim() ? current + section : note.text;
        if (merged.length > maxLength) throw new Error("Merged note too long");
        plans.push({ entry: entry, text: merged });
      });
      var unsaved = 0;
      plans.forEach(function (plan) {
        plan.entry.input.value = plan.text;
        if (!save(plan.entry, false)) unsaved += 1;
      });
      announce("已导入或合并 " + plans.length + " 篇，保留了原有内容。" + (unknown ? "跳过 " + unknown + " 篇资料库中不存在的论文。" : "") + (unsaved ? unsaved + " 篇未能保存，请导出当前编辑。" : ""));
    }).catch(function () { announce("备份格式无效、内容重复或过长，未导入。请选择个人笔记备份 JSON。"); });
  });

  window.addEventListener("storage", function (event) {
    if (event.key !== null && !event.key.startsWith(prefix)) return;
    entries.forEach(function (entry) {
      if (event.key !== null && event.key !== prefix + entry.id) return;
      if (entry.dirty) failure(entry, "另一标签页修改了此篇笔记；当前未保存编辑已保留。");
      else load(entry);
    });
  });
  window.addEventListener("beforeunload", function (event) {
    if (Array.from(entries.values()).some(function (entry) { return entry.dirty; })) {
      event.preventDefault();
      event.returnValue = "";
    }
  });
})();
