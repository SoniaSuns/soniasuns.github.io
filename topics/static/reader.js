'use strict';
const fields=Object.fromEntries(['category','type','topic','xr','aigc','search'].map(k=>[k,document.getElementById(k)]));
const papers=[...document.querySelectorAll('.paper')];let view='topics';
function apply(){let n=0;const q=fields.search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);for(const p of papers){p.hidden=!((!fields.category.value||p.dataset.category===fields.category.value)&&(!fields.type.value||p.dataset.type===fields.type.value)&&(!fields.topic.value||p.dataset.topic===fields.topic.value)&&(!fields.xr.value||p.dataset.xr.split(' ').includes(fields.xr.value))&&(!fields.aigc.value||(p.dataset.aigc||'').split(' ').includes(fields.aigc.value))&&q.every(w=>p.dataset.search.includes(w)));if(!p.hidden)n++;}document.getElementById('count').textContent=`显示 ${n} / ${papers.length} 个研究条目`;document.getElementById('empty').hidden=n!==0;}
function show(v){view=v;for(const k of ['xr','aigc','methods','topics','papers','video-pool','video-reasoning','topic-trends','resources'])document.getElementById(k+'-view').hidden=k!==v;document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===v)));apply();}
function reset(){Object.values(fields).forEach(f=>f.value='');apply();}
Object.values(fields).forEach(f=>f.addEventListener('input',apply));
document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>{show(b.dataset.view);document.getElementById(b.dataset.view+'-view').scrollIntoView({behavior:'instant'});}));
document.querySelectorAll('[data-topic-jump]').forEach(b=>b.addEventListener('click',()=>{reset();fields.topic.value=b.dataset.topicJump;show('papers');document.getElementById('papers-view').scrollIntoView();}));
document.querySelectorAll('[data-category-jump]').forEach(b=>b.addEventListener('click',()=>{reset();fields.category.value=b.dataset.categoryJump;show('papers');document.getElementById('papers-view').scrollIntoView();}));
document.getElementById('reset').addEventListener('click',reset);
function filterOverview(category){
  document.querySelectorAll('.overview-category,.overview-toc-group').forEach(el=>el.hidden=!!category&&el.dataset.category!==category);
  document.querySelectorAll('[data-overview-category]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.overviewCategory===category)));
  const n=[...document.querySelectorAll('.overview-card')].filter(el=>!el.closest('.overview-category').hidden).length;
  document.getElementById('overview-count').textContent=`显示 ${n} / ${document.querySelectorAll('.overview-card').length} 个 overview`;
}
document.querySelectorAll('[data-overview-category]').forEach(b=>b.addEventListener('click',()=>filterOverview(b.dataset.overviewCategory)));
function reveal(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;let target=document.getElementById(id);if(!target&&id.startsWith('p-P'))target=document.getElementById('paper-'+id.slice(2));if(!target)return;for(let el=target.parentElement;el;el=el.parentElement){if(el.tagName==='DETAILS')el.open=true;}if(target.closest('#resources-view'))show('resources');else if(target.closest('#video-reasoning-view'))show('video-reasoning');else if(target.closest('#topic-trends-view'))show('topic-trends');else if(target.closest('#video-pool-view'))show('video-pool');else if(target.classList.contains('paper')){reset();show('papers');}else if(target.closest('#xr-view'))show('xr');else if(target.closest('#aigc-view'))show('aigc');else if(target.closest('#methods-view'))show('methods');else if(target.closest('#topics-view')){show('topics');const section=target.closest('.overview-category');if(section&&(section.hidden||section===target))filterOverview(section.dataset.category);}requestAnimationFrame(()=>target.scrollIntoView({behavior:'smooth'}));}
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{if(location.hash===a.hash)reveal();}));window.addEventListener('hashchange',reveal);apply();reveal();

// Keep the independently usable paper-pool page within the normal Topics scroll.
const poolFrame=document.getElementById('video-pool-frame');
let poolObserver;
function sizePool(){
  const body=poolFrame.contentDocument?.body;
  if(body&&!document.getElementById('video-pool-view').hidden){
    const height=Math.ceil(body.getBoundingClientRect().height)+2;
    if(poolFrame.style.height!==height+'px')poolFrame.style.height=height+'px';
  }
}
poolFrame.addEventListener('load',()=>{
  poolObserver?.disconnect();
  poolObserver=new ResizeObserver(sizePool);
  poolObserver.observe(poolFrame.contentDocument.body);
  sizePool();
});
document.querySelector('[data-view="video-pool"]').addEventListener('click',()=>{
  history.replaceState(null,'','#video-pool-view');
  requestAnimationFrame(sizePool);
});
window.addEventListener('hashchange',()=>requestAnimationFrame(sizePool));

// Research supplement frames use the same document scroll as Topics.
for(const name of ['video-reasoning','topic-trends','resources']){
 const frame=document.getElementById(name+'-frame');let observer;
 const resize=()=>{const body=frame.contentDocument?.body;if(body&&!document.getElementById(name+'-view').hidden){const h=Math.ceil(body.getBoundingClientRect().height)+4;if(frame.style.height!==h+'px')frame.style.height=h+'px';}};
 frame.addEventListener('load',()=>{observer?.disconnect();if(frame.contentDocument?.body){observer=new ResizeObserver(resize);observer.observe(frame.contentDocument.body);resize();}});
 document.querySelector('[data-view="'+name+'"]').addEventListener('click',()=>{history.replaceState(null,'','#'+name+'-view');requestAnimationFrame(resize);});
 window.addEventListener('hashchange',()=>requestAnimationFrame(resize));
}
