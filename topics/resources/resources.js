(async()=>{
  const api=window.TopicResources,{h,num,card}=api,data=await api.data,rs=data.records,byId=new Map(rs.map(r=>[r.id,r]));
  const $=id=>document.getElementById(id),bins=['single','small','medium','large','unknown'];
  const directionNames={'XR-C':'XR-C · 因果教程编辑','XR-L':'XR-L · 主动澄清','XR-S':'XR-S · 新证据下纠错','XR-E':'XR-E · 跨任务持续改善','AIGC-A':'AIGC-A · 选择性编辑','AIGC-B':'AIGC-B · 记忆修订','AIGC-C':'AIGC-C · 事件／揭示时间','AIGC-D':'AIGC-D · 最少控制信号'};
  const topics=[...new Map(rs.filter(r=>r.topic_code).map(r=>[r.topic_code,r.topic])).entries()].sort();
  const tasks=[...new Set(rs.filter(r=>r.technical_key).map(r=>r.task))].sort();
  const reasoningTopics=[...new Set(rs.filter(r=>r.reasoning_id).map(r=>r.reasoning_topic))].sort();
  const c=data.counts;
  $('resource-kpis').innerHTML=[[c.total,'去重论文 · 每篇有资源状态'],[c.fulltext,'已取得可检索正文'],[c.known_ft_gpu_count,'有可比微调 GPU 数'],[c.known_ft_device_hours,'有可归属的微调 GPU-hours']].map(([n,l])=>`<div class="resource-kpi"><strong>${n}</strong><span>${h(l)}</span></div>`).join('');
  $('resource-coverage').textContent=`覆盖边界：${c.resource_stage_checked} 篇有已核对的分阶段资源记录；${c.no_weight_update} 篇确认无需本文权重训练（可能仍有推理硬件记录）；${c.status['未定位可比微调配置']||0} 篇本轮未定位可比微调配置；${c.status['全文获取受限']||0} 篇全文受限。阶段记录包括预训练／辅助训练／推理，因此不能把 ${c.resource_stage_checked} 当作已知 fine-tuning 成本的篇数。`;
  $('resource-rules').innerHTML=data.rules.map(t=>'<li>'+h(t)+'</li>').join('');
  $('resource-legend').innerHTML=bins.map(b=>`<span><i class="bin-${b}"></i>${h(api.labels[b])}</span>`).join('');
  $('resource-group').innerHTML+='<optgroup label="Topics 主 topic">'+topics.map(([code,title])=>`<option value="${h(code)}">${h(code+' · '+title)}</option>`).join('')+'</optgroup><optgroup label="XR / AIGC 方向">'+Object.entries(directionNames).map(([c,t])=>`<option value="${c}">${h(t)}</option>`).join('')+'</optgroup><optgroup label="原视频任务轴">'+tasks.map(t=>`<option value="task:${h(t)}">${h(t)}</option>`).join('')+'</optgroup>';
  const devices=[...new Set(rs.flatMap(r=>r.stages.map(s=>s.device)))].sort();
  $('chart-scope').insertAdjacentHTML('beforeend','<option value="reasoning">推理研究池 · 109 篇 · 原任务主题</option>');
  $('resource-group').insertAdjacentHTML('beforeend','<optgroup label="R1 / R2 / R3 研究池">'+reasoningTopics.map(t=>`<option value="reasoning:${h(t)}">${h(t)}</option>`).join('')+'</optgroup>');
  $('resource-device').innerHTML+=devices.map(t=>`<option value="${h(t)}">${h(t)}</option>`).join('');
  function groupRows(){
    if($('chart-scope').value==='reasoning')return reasoningTopics.map(t=>({key:'reasoning:'+t,title:t,rows:rs.filter(r=>r.reasoning_id&&r.reasoning_topic===t)}));
    if($('chart-scope').value==='video')return tasks.map(t=>({key:'task:'+t,title:t,rows:rs.filter(r=>r.technical_key&&r.task===t)}));
    if($('chart-scope').value==='directions')return Object.entries(directionNames).map(([key,title])=>({key,title,rows:rs.filter(r=>r.directions.includes(key))}));
    return topics.map(([key,title])=>({key,title:key+' · '+title,rows:rs.filter(r=>r.topic_code===key)}));
  }
  function chart(){
    const groups=groupRows(),knownOnly=$('chart-denominator').value==='known';
    $('resource-chart').innerHTML=groups.map(g=>{
      const cc=Object.fromEntries(bins.map(b=>[b,g.rows.filter(r=>r.hardware_bin===b).length])),known=g.rows.length-cc.unknown,den=knownOnly?known:g.rows.length;
      return `<div class="resource-chart-row"><button data-resource-group="${h(g.key)}">${h(g.title)}</button><div class="resource-bar" aria-label="${h(g.title)}：${bins.map(b=>api.labels[b]+' '+cc[b]).join('，')}">${bins.filter(b=>!(knownOnly&&b==='unknown')).map(b=>cc[b]?`<span class="bin-${b}" style="width:${100*cc[b]/(den||1)}%" title="${h(api.labels[b])}：${cc[b]} / ${den}">${cc[b]/(den||1)>.055?cc[b]:''}</span>`:'').join('')}</div><small>有数 ${known} / 全部 ${g.rows.length}</small></div>`;
    }).join('');
    $('topic-table').innerHTML=groups.map(g=>{
      const cc=Object.fromEntries(bins.map(b=>[b,g.rows.filter(r=>r.hardware_bin===b).length])),known=g.rows.length-cc.unknown;
      return `<tr><td><button data-resource-group="${h(g.key)}">${h(g.title)}</button></td><td>${g.rows.length}</td><td>${known}</td>${bins.slice(0,4).map(b=>`<td>${cc[b]}</td>`).join('')}<td>${g.rows.filter(r=>r.has_ft_time).length}</td><td>${known?`${(cc.single/known*100).toFixed(0)}% / ${((cc.single+cc.small)/known*100).toFixed(0)}%`:'—'}</td></tr>`;
    }).join('');
    document.querySelectorAll('[data-resource-group]').forEach(b=>b.onclick=()=>{resetFields();$('resource-group').value=b.dataset.resourceGroup;filter();$('paper-resources').scrollIntoView({behavior:'instant'});});
  }
  const inputs=['resource-query','resource-group','resource-filter','resource-device'];let page=0,shown=[],focusId='';const size=20;
  const ft=r=>r.stages.filter(s=>s.role==='ft'&&s.comparable&&s.is_gpu);
  const predicates={single:r=>ft(r).some(s=>s.count_max===1),consumer:r=>ft(r).some(s=>s.count_max===1&&/RTX (?:20|30|40|50)\d\d|GTX|Titan/i.test(s.device)&&!s.scope.includes('不符')),small:r=>r.max_reported_ft_gpus!=null&&r.max_reported_ft_gpus<=8,large:r=>r.max_reported_ft_gpus>=9,timed:r=>r.has_ft_time,pre:r=>r.stages.some(s=>s.role==='pre'),opt:r=>r.stages.some(s=>s.role==='opt'),none:r=>r.no_weight_update,missing:r=>['未定位可比微调配置','全文获取受限'].includes(r.status)};
  function filter(){
    page=0;focusId='';const words=$('resource-query').value.toLowerCase().trim().split(/\s+/).filter(Boolean),g=$('resource-group').value,f=$('resource-filter').value,dev=$('resource-device').value;
    shown=rs.filter(r=>(!g||r.topic_code===g||r.directions.includes(g)||(g.startsWith('task:')&&r.technical_key&&r.task===g.slice(5))||(g.startsWith('reasoning:')&&r.reasoning_id&&r.reasoning_topic===g.slice(10)))&&(!f||predicates[f](r))&&(!dev||r.stages.some(s=>s.device===dev))&&words.every(w=>(r.id+' '+r.title+' '+r.model+' '+r.training_datasets+' '+r.topic+' '+r.reasoning_role+' '+JSON.stringify(r.stages)).toLowerCase().includes(w)));
    render();
  }
  function render(){
    $('resource-count').textContent=`匹配 ${shown.length} / ${rs.length} 篇 · 可比微调卡数 ${shown.filter(r=>r.max_reported_ft_gpus!=null).length} 篇 · 有微调 GPU-hours ${shown.filter(r=>r.has_ft_time).length} 篇`;
    $('resource-list').innerHTML=shown.slice(page*size,(page+1)*size).map(r=>`<article class="resource-paper" id="${r.id}"><div class="eyebrow">${h(r.id+' · '+r.year+' · '+(r.topic_code?r.topic_code+' '+r.topic:'补充研究池'))}</div><h3>${h(r.title)}</h3><p class="resource-footnote">${h(r.directions.join(' / '))} · <a href="${h(r.source_url)}" target="_blank" rel="noopener">原文 ↗</a> ${r.library_id?` · <a href="../#paper-${h(r.library_id)}" target="_top">原 Topics 标注</a>`:''}${r.catalog_id?` · <a href="../video-generation-pool/#${h(r.catalog_id)}" target="_blank" rel="noopener">完整 taxonomy</a>`:''}</p>${card(r,{expanded:r.id===focusId,link:false})}</article>`).join('')||'<p>没有符合这些条件的已记录论文。缺失数据不会自动算作低资源。</p>';
    $('resource-page').textContent=`${page+1} / ${Math.max(1,Math.ceil(shown.length/size))}`;$('resource-prev').disabled=page===0;$('resource-next').disabled=(page+1)*size>=shown.length;
  }
  function resetFields(){for(const id of inputs)$(id).value='';}
  for(const id of inputs)$(id).addEventListener(id==='resource-query'?'input':'change',filter);
  $('resource-reset').onclick=()=>{resetFields();filter();};
  $('resource-prev').onclick=()=>{page--;render();$('paper-resources').scrollIntoView();};$('resource-next').onclick=()=>{page++;render();$('paper-resources').scrollIntoView();};
  $('chart-scope').onchange=chart;$('chart-denominator').onchange=chart;
  function reveal(){const id=decodeURIComponent(location.hash.slice(1));if(!byId.has(id))return;resetFields();shown=rs;focusId=id;page=Math.floor(rs.findIndex(r=>r.id===id)/size);render();requestAnimationFrame(()=>$(id).scrollIntoView({block:'start'}));}
  window.addEventListener('hashchange',reveal);document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#R"]');if(a&&a.hash===location.hash)reveal();});
  chart();const group=new URLSearchParams(location.search).get('group');if(group)$('resource-group').value=group;filter();reveal();document.documentElement.dataset.resourceDashboard='ready';
})().catch(e=>{console.error(e);document.getElementById('resource-count').textContent='资源数据未能加载，请刷新或下载 CSV。';document.documentElement.dataset.resourceDashboard='error';});
