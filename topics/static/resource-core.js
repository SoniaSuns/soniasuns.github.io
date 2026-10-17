/* Shared, additive resource annotations. Does not mutate the original taxonomy. */
(() => {
  const base=new URL('../',document.currentScript.src);
  const h=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const num=x=>x==null?'未定位':Number(x).toLocaleString('zh-CN',{maximumFractionDigits:2});
  const range=(a,b)=>a==null?'未定位':num(a)+(a!==b?'–'+num(b):'');
  const labels={single:'单卡',small:'2–8 卡',medium:'9–64 卡',large:'65+ 卡',unknown:'未纳入微调卡数比较'};
  function stage(s){
    const devices=s.count_min==null?h(s.device)+' · 数量未定位':range(s.count_min,s.count_max)+' × '+h(s.device);
    const boundary=s.time_bound==='upper'?'≤ ':s.time_bound==='lower'?'≥ ':'约 ';
    return `<li class="resource-stage"><div><b>${h(s.role_label)}</b> <span>${devices}</span></div><dl><div><dt>卡容量</dt><dd>${s.card_memory_gb==null?'未定位':num(s.card_memory_gb)+' GB'}</dd></div><div><dt>实测 peak</dt><dd>${s.peak_memory_gb==null?'未定位':num(s.peak_memory_gb)+' GB（范围见备注）'}</dd></div><div><dt>墙钟耗时</dt><dd>${s.wall_hours_min==null?'未定位':boundary+range(s.wall_hours_min,s.wall_hours_max)+' h'}</dd></div><div><dt>GPU-hours</dt><dd>${s.gpu_hours_min==null?'未定位／不换算':boundary+range(s.gpu_hours_min,s.gpu_hours_max)}</dd></div></dl><p>${h(s.scope)}</p>${s.gpu_hours_basis?`<small>${h(s.gpu_hours_basis)}</small>`:''}<small>依据：<a href="${h(s.source_url)}" target="_blank" rel="noopener">${h(s.locator)} ↗</a></small></li>`;
  }
  function summary(r){
    const main=r.stages.filter(s=>s.role==='ft'),other=r.stages.filter(s=>!['inf','claim'].includes(s.role));
    const ss=main.length?main:other.length?other:r.stages;
    const text=ss.slice(0,2).map(s=>(s.count_min==null?'':range(s.count_min,s.count_max)+' × ')+s.device+(s.wall_hours_min==null?'': ' · '+(s.time_bound==='upper'?'≤':s.time_bound==='lower'?'≥':'约 ')+range(s.wall_hours_min,s.wall_hours_max)+' h'));
    return text.length?text.join('；')+(ss.length>2?'；另有阶段':''):r.no_weight_update?'无新增权重训练；运行成本另计':r.status;
  }
  function card(r,{expanded=false,link=true}={}){
    const badge=r.max_reported_ft_gpus!=null?labels[r.hardware_bin]+'微调配置':r.stages.length?'分阶段资源':r.no_weight_update?'不更新权重':'资源缺项';
    return `<details class="resource-inline" data-resource-id="${h(r.id)}" ${expanded?'open':''}><summary><b>训练资源</b><span class="resource-badge ${h(r.hardware_bin)}">${h(badge)}</span><span>${h(summary(r))}</span></summary><div class="resource-content"><p class="resource-scope">${h(r.status)} · ${h(r.resource_note||'以下仅对应列明的训练阶段；未报告的基础模型、数据生成、搜索与调参成本不默认包含。')}</p>${r.stages.length?'<ol class="resource-stages">'+r.stages.map(stage).join('')+'</ol>':''}<dl class="resource-meta"><div><dt>Model / 模块</dt><dd>${h(r.model)}</dd></div><div><dt>训练／适配 dataset</dt><dd>${h(r.training_datasets)}</dd></div><div><dt>训练信号</dt><dd>${h(r.training_signal)}</dd></div></dl><p class="resource-footnote">${h(r.screening)} ${link?`<a href="${h(new URL('resources/#'+r.id,base))}" target="_blank" rel="noopener">资源比较与原文 ↗</a>`:''}</p></div></details>`;
  }
  const data=window.TOPIC_RESOURCE_DATA?Promise.resolve(window.TOPIC_RESOURCE_DATA):fetch(new URL('data/finetune-resources.json',base)).then(r=>{if(!r.ok)throw Error('Resource data unavailable');return r.json();});
  window.TopicResources={data,h,num,range,labels,stage,summary,card,base};
})();
