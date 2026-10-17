(() => {
  const rows=[...document.querySelectorAll('.catalog-paper')], size=18;
  const query=document.querySelector('#query'),task=document.querySelector('#task'),contribution=document.querySelector('#contribution'),direction=document.querySelector('#direction');
  let page=0, visible=[];
  const panels=['catalog','matrix','questions','taxonomy'];
  function show(name){for(const p of panels)document.getElementById('view-'+p).hidden=p!==name;document.querySelectorAll('nav button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.panel===name)));}
  function filter(reset=true){if(reset)page=0;const words=query.value.trim().toLowerCase().split(/\s+/).filter(Boolean);visible=rows.filter(r=>words.every(w=>r.dataset.search.includes(w))&&(!task.value||r.dataset.task===task.value)&&(!contribution.value||r.dataset.contributions.split(' / ').includes(contribution.value))&&(!direction.value||r.dataset.directions.split(' / ').includes(direction.value)));render();}
  function render(){const shown=new Set(visible.slice(page*size,(page+1)*size));rows.forEach(r=>r.hidden=!shown.has(r));document.getElementById('count').textContent=`匹配 ${visible.length} / ${rows.length} 篇 · 当前显示 ${shown.size} 篇`;document.getElementById('page-status').textContent=`${page+1} / ${Math.max(1,Math.ceil(visible.length/size))}`;document.getElementById('prev').disabled=page===0;document.getElementById('next').disabled=(page+1)*size>=visible.length;}
  function reset(){query.value=task.value=contribution.value=direction.value='';filter();}
  for(const x of [query,task,contribution,direction])x.addEventListener(x===query?'input':'change',()=>filter());
  document.getElementById('reset').onclick=reset;
  for(const [id,delta] of [['prev',-1],['next',1]])document.getElementById(id).onclick=()=>{page+=delta;render();document.getElementById('view-catalog').scrollIntoView();};
  document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{show(b.dataset.panel);history.replaceState(null,'','#view-'+b.dataset.panel);});
  document.querySelectorAll('.matrix-filter').forEach(b=>b.onclick=()=>{reset();task.value=b.dataset.task;contribution.value=b.dataset.contribution;filter();show('catalog');history.replaceState(null,'','#view-catalog');document.getElementById('view-catalog').scrollIntoView();});
  function reveal(){const id=decodeURIComponent(location.hash.slice(1));const legacy={'view-papers':'catalog','view-expansion':'catalog','view-sources':'taxonomy','view-overview':'catalog'};if(legacy[id])show(legacy[id]);else if(id.startsWith('view-')&&panels.includes(id.slice(5)))show(id.slice(5));else if(/^[PX]\d+$/.test(id)){const r=document.getElementById(id);if(!r)return;reset();page=Math.floor(visible.indexOf(r)/size);render();show('catalog');r.querySelector('details:not(.resource-inline)').open=true;requestAnimationFrame(()=>r.scrollIntoView({block:'start'}));}else if(/^q\d+$/.test(id)){show('questions');requestAnimationFrame(()=>document.getElementById(id)?.scrollIntoView({block:'start'}));}}
  window.addEventListener('hashchange',reveal);document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(a&&a.hash===location.hash)reveal();});
  reset();show('catalog');reveal();
})();
