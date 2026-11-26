// Native Web Component. No iframe, framework, or browser-side model credentials.
class FacilityCopilot extends HTMLElement {
  constructor() {
    super(); this.history=[]; this.busy=false; this.attachShadow({mode:'open'});
  }
  connectedCallback() {
    if(this.initialized)return;this.initialized=true;
    const root=this.shadowRoot;
    root.innerHTML=`<style>
      :host{display:block;height:100%;min-height:360px;font:14px/1.6 system-ui,sans-serif;color:#294b3d;background:#fafbf8;border:1px solid #dce5d8;border-radius:12px;overflow:hidden}*{box-sizing:border-box}.panel{height:100%;display:flex;flex-direction:column}header{padding:16px;border-bottom:1px solid #dce5d8;display:flex;justify-content:space-between;align-items:center}header strong{font-size:16px}button,select,textarea{font:inherit}button{cursor:pointer}select{max-width:150px;border:1px solid #d3decd;border-radius:6px;padding:5px;background:white}.tools{display:flex;gap:8px;flex-wrap:wrap;padding:10px 16px}.tools button{border:0;background:transparent;color:#45664e}section{flex:1;overflow:auto;padding:16px;min-height:0}.message{margin-bottom:18px}.user{background:#edf3e7;padding:10px 14px;border-radius:9px}.label{font-size:10px;font-weight:700;letter-spacing:1px;color:#758c76}p{white-space:pre-wrap;margin:8px 0}.sources{margin-top:10px}details{border:1px solid #dce5d8;border-radius:7px;padding:9px;margin:8px 0;font-size:12px}summary{cursor:pointer}pre{white-space:pre-wrap;font:12px/1.7 system-ui;max-height:220px;overflow:auto}a{color:#277047}.notice{font-size:12px;color:#7b6230;background:#fff5df;padding:8px}form{border-top:1px solid #dce5d8;padding:12px;background:white}textarea{width:100%;border:1px solid #d5e1ce;border-radius:8px;padding:10px;resize:vertical;min-height:65px;max-height:140px}form button{background:#2e594b;color:white;border:0;border-radius:7px;padding:8px 15px;float:right}form button:disabled{opacity:.5}.foot{font-size:10px;color:#7a8d79;max-width:75%;margin-top:8px}.welcome{color:#6c806d}.status{font-size:10px;color:#7a8d79}:focus-visible{outline:2px solid #64876e;outline-offset:2px}
    </style><div class="panel"><header><strong>Facility Copilot</strong><span class="status">Connecting…</span></header><div class="tools"><select aria-label="Program area"><option>All programs</option></select><button type="button" class="new">＋ New chat</button></div><section aria-live="polite"><p class="welcome">Ask a guideline question. Answers are based on retrieved passages and include source references.</p></section><form><textarea aria-label="Guideline question" maxlength="2000" placeholder="Ask about your guidelines…" required></textarea><button type="submit">Send ↑</button><div class="foot">AI answers need review. Questions and relevant passages are sent to the configured ML server.</div></form></div>`;
    this.q=s=>root.querySelector(s);
    this.q('form').onsubmit=e=>{e.preventDefault();this.ask();};
    this.q('textarea').onkeydown=e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();this.q('form').requestSubmit();}};
    this.q('.new').onclick=()=>this.reset();
    this.q('select').onchange=()=>this.reset();
    this.loadLibrary();
  }
  // Call after logout or any patient-context change; clears browser-memory conversation.
  reset(){if(this.busy)return false;this.history=[];this.q('section').replaceChildren(this.element('p','Start a new guideline conversation.','welcome'));return true;}
  element(tag,text,cls){const e=document.createElement(tag);if(text)e.textContent=text;if(cls)e.className=cls;return e;}
  base(){return (this.getAttribute('api-base')||'').replace(/\/$/,'');}
  async loadLibrary(){try{const r=await fetch(this.base()+'/api/library',{credentials:'same-origin'});if(!r.ok)throw Error('Library unavailable');const data=await r.json();data.programs.forEach(p=>this.q('select').append(this.element('option',p)));const selected=this.getAttribute('program');if(data.programs.includes(selected))this.q('select').value=selected;this.q('.status').textContent=data.mode;}catch(e){this.q('.status').textContent=e.message;}}
  bubble(text,kind){this.q('.welcome')?.remove();const e=this.element('article',null,'message '+kind);e.append(this.element('div',kind==='user'?'YOU':'FACILITY COPILOT','label'),this.element('p',text));this.q('section').append(e);return e;}
  sourceLink(source,label){const a=this.element('a',label);a.href=this.base()+source.url;a.target='_blank';a.rel='noopener';return a;}
  async ask(){const input=this.q('textarea');const question=input.value.trim();if(this.busy||!question)return;this.busy=true;const send=this.q('form button');send.disabled=true;this.bubble(question,'user');input.value='';const reply=this.bubble('Reading the relevant guidelines…','assistant');try{
      const r=await fetch(this.base()+'/api/chat',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},body:JSON.stringify({question,program:this.q('select').value,include_drafts:false,history:this.history.slice(-6)})});const data=await r.json();if(!r.ok)throw Error(data.error||'Could not answer');reply.querySelector('p').remove();
      for(const b of data.blocks||[{text:data.message,citations:[]}]){const p=this.element('p',b.text);for(const id of b.citations)p.append(this.sourceLink(data.sources[id-1],' ['+id+']'));reply.append(p);}
      this.history.push({role:'user',content:question},{role:'assistant',content:(data.blocks?.map(block=>block.text).join('\n\n')??data.message).slice(0,8000)});this.history=this.history.slice(-6);
      if(data.mode!=='llm')reply.append(this.element('div','AI is not configured. Showing guideline excerpts.','notice'));
      for(const notice of data.notices||[])reply.append(this.element('div',notice,'notice'));
      const sources=this.element('div',null,'sources');(data.sources||[]).forEach((s,i)=>{const d=this.element('details');d.open=i===0;const pageKind=s.page_kind||'PDF page';const pages=s.page?(s.page_end&&s.page_end!==s.page?' · '+pageKind+'s '+s.page+'–'+s.page_end:' · '+pageKind+' '+s.page):'';d.append(this.element('summary',`[${i+1}] ${s.document.title} · ${s.document.version}${pages}${s.heading_path?' · '+s.heading_path:''}`),this.element('pre',s.text),this.sourceLink(s,s.url.includes('#page=')?'Open source page ↗':'Open source ↗'));sources.append(d);});reply.append(sources);
    }catch(e){reply.replaceChildren(this.element('p',e.message));input.value=question;}finally{this.busy=false;send.disabled=false;this.q('section').scrollTop=this.q('section').scrollHeight;}}
}
if(!customElements.get('facility-copilot'))customElements.define('facility-copilot',FacilityCopilot);
