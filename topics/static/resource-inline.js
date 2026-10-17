(async()=>{
  const api=window.TopicResources,data=await api.data,records=new Map(data.records.map(r=>[r.id,r]));
  const byAlias=a=>records.get(data.alias_index[a]);
  const normalize=s=>s.toLowerCase().split(/[（(]/)[0].replace(/[^a-z0-9]/g,'');
  const titles=new Map(data.records.map(r=>[normalize(r.title),r]));
  function add(host,r,anchor){
    if(!r||!host||[...host.children].some(x=>x.dataset.resourceId===r.id))return;
    const wrapper=document.createElement('div');wrapper.innerHTML=api.card(r);const node=wrapper.firstElementChild;
    if(anchor)anchor.after(node);else host.append(node);
    if(host.dataset.search!=null)host.dataset.search+=' '+api.summary(r).toLowerCase()+' '+r.stages.map(s=>s.scope).join(' ').toLowerCase();
  }
  document.querySelectorAll('article.paper[id^="paper-"]').forEach(el=>add(el,byAlias('library:'+el.id.slice(6)),el.querySelector('h3')));
  document.querySelectorAll('.catalog-paper[data-key]').forEach(el=>add(el,records.get(data.technical_index[el.dataset.key]),el.querySelector('h2,h3')));
  document.querySelectorAll('.paper-card[id^="paper-"]').forEach(el=>add(el,byAlias('lineage:'+el.id.slice(6)),el.querySelector('h2,h3')));
  document.querySelectorAll('.reading-update-card').forEach(el=>{const h=el.querySelector('h3,h4');if(h)add(el,titles.get(normalize(h.textContent)),h);});
  document.querySelectorAll('[id^="recent-"]').forEach(el=>add(el,byAlias('recent:'+el.id.slice(7)),el.querySelector('h3,h4')));
  for(const a of document.querySelectorAll('.overview-card a, .direction a, [data-reading-update] a, .card td a, .card li a')){
    if(a.closest('.resource-inline,.technical-inline,.reading-update-card'))continue;
    const host=a.closest('td,li');if(!host)continue;
    let r=titles.get(normalize(a.textContent.replace(/^(?:VG\d+|P\d+)\s*/,'')));
    if(!r&&a.hash.startsWith('#paper-'))r=byAlias((location.pathname.includes('problem-lineage')?'lineage:':'library:')+a.hash.slice(7));
    if(!r&&a.hash.startsWith('#recent-'))r=byAlias('recent:'+a.hash.slice(8));
    add(host,r,null);
  }
  document.querySelectorAll('.overview-card[data-code],.direction[id]').forEach(el=>{
    const code=el.dataset.code||el.id,group=data.records.filter(r=>r.topic_code===code||r.directions.includes(code));
    if(!group.length)return;
    const known=group.filter(r=>r.max_reported_ft_gpus!=null),small=known.filter(r=>r.max_reported_ft_gpus<=8),large=known.filter(r=>r.max_reported_ft_gpus>=9);
    const p=document.createElement('p');p.className='resource-direction';p.innerHTML=`<b>本方向训练资源</b> ${group.length} 篇中，${known.length} 篇有可比较的微调卡数：${small.length} 篇已披露阶段不超过 8 卡，${large.length} 篇达到 9+ 卡。<a href="${api.h(new URL('resources/?group='+encodeURIComponent(code),api.base))}" target="_blank" rel="noopener">查看具体配置与缺项 ↗</a>`;
    (el.querySelector('.overview-summary')||el.querySelector('h2,h3'))?.after(p);
  });
  document.documentElement.dataset.resourceAnnotations='ready';window.dispatchEvent(new Event('resize'));
})().catch(e=>{console.error(e);document.documentElement.dataset.resourceAnnotations='error';});
