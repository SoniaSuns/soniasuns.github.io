
'use strict';
const panels=['overview','papers','matrix','questions','taxonomy','sources'];
function showPanel(name){for(const key of panels)document.getElementById('view-'+key).hidden=key!==name;document.querySelectorAll('[data-panel]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.panel===name)));}
document.querySelectorAll('[data-panel]').forEach(b=>b.addEventListener('click',()=>{showPanel(b.dataset.panel);history.replaceState(null,'','#view-'+b.dataset.panel);}));
const rows=[...document.querySelectorAll('tr.paper')];
const ids=['query','task','contribution','contributionMode','source','sourceMode','year','venue','status','kind','paradigm','control','goal','evidence'];
const fields=Object.fromEntries(ids.map(id=>[id,document.getElementById(id)]));
function filter(){let n=0;const words=fields.query.value.trim().toLowerCase().split(/\s+/).filter(Boolean);for(const row of rows){const d=row.dataset;const sources=fields.sourceMode.value==='all'?d.all.split('; '):[d.source];const contributions=fields.contributionMode.value==='all'?[d.contribution,...d.secondary.split('; ')]:[d.contribution];let show=words.every(w=>d.search.includes(w))&&(!fields.source.value||sources.includes(fields.source.value))&&(!fields.contribution.value||contributions.includes(fields.contribution.value));for(const k of ['task','year','venue','status','kind','paradigm'])show=show&&(!fields[k].value||d[k]===fields[k].value);for(const k of ['control','goal','evidence'])show=show&&(!fields[k].value||d[k].split(/;\s*/).includes(fields[k].value));row.classList.toggle('hidden',!show);if(show)n++;}document.getElementById('count').textContent=`显示 ${n} / ${rows.length} 篇`;document.getElementById('empty').classList.toggle('hidden',n!==0);}
function reset(){ids.forEach(id=>fields[id].value=['sourceMode','contributionMode'].includes(id)?'primary':'');filter();}
ids.forEach(id=>fields[id].addEventListener(id==='query'?'input':'change',filter));
document.getElementById('reset').onclick=reset;
document.getElementById('expand').onclick=()=>rows.filter(r=>!r.classList.contains('hidden')).forEach(r=>r.querySelector('details').open=true);
document.getElementById('collapse').onclick=()=>rows.forEach(r=>r.querySelector('details').open=false);
document.querySelectorAll('[data-matrix-task]').forEach(b=>b.addEventListener('click',()=>{reset();fields.task.value=b.dataset.matrixTask;fields.contribution.value=b.dataset.matrixContribution;filter();showPanel('papers');history.replaceState(null,'','#view-papers');document.querySelector('.nav').scrollIntoView({behavior:'instant'});}));
function reveal(){const id=decodeURIComponent(location.hash.slice(1));if(/^P\d{3}$/.test(id)){const row=document.getElementById(id);if(!row)return;reset();showPanel('papers');row.querySelector('details').open=true;requestAnimationFrame(()=>row.scrollIntoView({block:'start'}));}else if(/^q\d+$/.test(id)){const q=document.getElementById(id);if(!q)return;showPanel('questions');q.open=true;requestAnimationFrame(()=>q.scrollIntoView({block:'start'}));}else if(id.startsWith('view-')&&panels.includes(id.slice(5)))showPanel(id.slice(5));}
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{if(location.hash===a.hash)reveal();}));window.addEventListener('hashchange',reveal);filter();reveal();
