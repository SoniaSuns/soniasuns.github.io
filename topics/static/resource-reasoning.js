(async()=>{
 const api=window.TopicResources,data=await api.data,byId=new Map(data.records.map(r=>[r.id,r]));
 const norm=s=>s.toLowerCase().split(/[（(]/)[0].replace(/[^a-z0-9]/g,'');
 const titles=new Map(data.records.map(r=>[norm(r.title),r]));
 function add(host,r){if(!r||host.querySelector(':scope > .resource-inline'))return;const wrap=document.createElement('div');wrap.innerHTML=api.card(r);(host.querySelector('h3')||host.lastElementChild).after(wrap.firstElementChild);}
 function attach(){
  document.querySelectorAll('#cards article[id^="paper-"]').forEach(el=>add(el,byId.get(data.alias_index['reasoning:'+el.id.slice(6)])));
  document.querySelectorAll('#paperlist article').forEach(el=>add(el,titles.get(norm(el.querySelector('h3')?.textContent||''))));
  document.querySelectorAll('#table tbody tr').forEach(tr=>{const td=tr.firstElementChild;add(td,titles.get(norm(td.querySelector('a')?.textContent||'')));});
  document.documentElement.dataset.resourceAnnotations='ready';
 }
 for(const id of ['cards','table','paperlist']){const el=document.getElementById(id);if(el)new MutationObserver(attach).observe(el,{childList:true});}
 attach();
})().catch(e=>{console.error(e);document.documentElement.dataset.resourceAnnotations='error';});
