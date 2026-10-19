/* Progressive enhancement: all scenario content remains readable without JS. */
document.querySelectorAll('.dp-scenarios').forEach(section=>{
  const buttons=[...section.querySelectorAll('[data-scenario]')];
  const panels=[...section.querySelectorAll('[data-scenario-panel]')];
  function select(id){
    buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.scenario===id)));
    panels.forEach(p=>p.hidden=p.dataset.scenarioPanel!==id);
  }
  buttons.forEach(b=>b.addEventListener('click',()=>select(b.dataset.scenario)));
  if(buttons.length)select(buttons[0].dataset.scenario);
});
