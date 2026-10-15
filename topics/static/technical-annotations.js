/* Add the same reviewed annotations wherever an XR / AIGC paper is read. */
(async()=>{
  const script=document.currentScript,base=new URL('../',script.src),report=location.pathname.includes('problem-lineage')||location.pathname.includes('research-preview');
  const response=window.TOPIC_TECHNICAL_DATA||await fetch(new URL('data/technical-annotations.json',base)).then(r=>{if(!r.ok)throw Error('Annotations unavailable');return r.json();});
  const records=new Map(response.records.map(r=>[r.key,r])),aliases=response.alias_index;
  const h=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const value=v=>Array.isArray(v)?v.join(' / '):v||'无';
  const normalize=s=>s.toLowerCase().split(/[（(]/)[0].replace(/[^a-z0-9]/g,'');
  const titles=new Map(response.records.map(r=>[normalize(r.title),r]));
  function byAlias(a){return records.get(aliases[a]);}
  function row(label,v){return `<div><b>${h(label)}</b><span>${h(value(v))}</span></div>`;}
  function block(r,compact=false){
    const t=r.taxonomy,f=r.technical,node=document.createElement('div');node.className='technical-inline'+(compact?' compact':'');node.dataset.annotationKey=r.key;
    const catalog=new URL('video-generation-pool/#'+r.id,base).href;
    node.innerHTML='<div class="technical-tags">'+[['任务',t.task],['主贡献',t.contribution_primary],['次贡献',t.contribution_secondary],['控制信号',t.control_signals],['目标性质',t.target_properties],['生成范式',t.generation_paradigm],['类型',t.paper_type]].map(([k,v])=>`<span><b>${h(k)}</b> ${h(value(v))}</span>`).join('')+'</div>'+`<p class="technical-contribution"><b>具体贡献：</b>${h(f.contribution_plain)}</p>`+'<div class="technical-facts">'+[['Model',f.model],['Backbone',f.backbone],['生成方式',f.mechanism],['Condition 标签 [推断]',f.condition_tags],['条件内容与来源',f.conditions_detail],['训练／适应数据',f.training_datasets]].map(([k,v])=>row(k,v)).join('')+'</div>'+
    '<details class="technical-more"><summary>任务定义、数据用途与原文依据</summary><div class="technical-facts">'+[['输入',t.task_input],['输出',t.task_output],['保持不变',t.task_invariants],['判断对错',t.correctness_criteria],['证据类型',t.evidence_types],['user study 样本量',t.user_study_sample],['训练信号的具体做法',f.training_signal_plain],['条件注入的具体做法',f.conditioning_plain],['底座预训练数据',f.pretraining_datasets],['评测数据／协议',f.evaluation_datasets],['一句话推进',t.one_sentence_advance],['不确定性',t.uncertainty],['原文位置',r.evidence.locator],['核验范围',r.evidence.scope]].map(([k,v])=>row(k,v)).join('')+`</div><p class="technical-note">分类映射为 [推断]；原有 taxonomy 保留。内部生成条件与用户输入按 Condition 描述区分。</p><a href="${h(r.evidence.url)}">原文 ↗</a> · <a href="${h(catalog)}">打开完整论文卡片 ↗</a></details>`;
    return node;
  }
  function add(host,r,anchor,compact=false){if(!r||[...host.children].some(c=>c.dataset.annotationKey===r.key))return;const node=block(r,compact);if(anchor)anchor.after(node);else host.append(node);}
  document.querySelectorAll('article.paper[id^="paper-"]').forEach(el=>{const r=byAlias('library:'+el.id.slice(6));add(el,r,el.querySelector('h3'));if(r)el.dataset.search+=' '+JSON.stringify(r.technical).toLowerCase()+' '+JSON.stringify(r.taxonomy).toLowerCase();});
  document.querySelectorAll('.paper-card[id^="paper-"]').forEach(el=>add(el,byAlias('lineage:'+el.id.slice(6)),el.querySelector(':scope > details')));
  document.querySelectorAll('.reading-update-card').forEach(el=>{const heading=el.querySelector('h4,h3');if(heading)add(el,titles.get(normalize(heading.textContent)),heading,true);});
  document.querySelectorAll('[id^="recent-"]').forEach(el=>{const r=byAlias('recent:'+el.id.slice(7));if(r&&!el.closest('.technical-inline'))add(el,r,el.querySelector('h3,h4'),true);});
  const candidates=[...document.querySelectorAll('.overview-card a, .direction a, [data-reading-update] a, .card td a, .card li a')];
  for(const a of candidates){
    if(a.closest('.technical-inline,.reading-update-card')||a.textContent.trim().length<20)continue;
    const host=a.closest('td,li');if(!host||host.querySelector('.technical-inline'))continue;
    let r=titles.get(normalize(a.textContent.replace(/^(?:VG\d+|P\d+)\s*/,'')));
    if(!r){const hash=a.hash||'';if(hash.startsWith('#paper-'))r=byAlias((report?'lineage:':'library:')+hash.slice(7));else if(hash.startsWith('#recent-'))r=byAlias('recent:'+hash.slice(8));}
    add(host,r,null,true);
  }
  document.documentElement.dataset.technicalAnnotations='ready';
  window.dispatchEvent(new Event('resize'));
})().catch(error=>{console.error(error);document.documentElement.dataset.technicalAnnotations='error';});
