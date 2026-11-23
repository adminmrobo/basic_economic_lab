#!/usr/bin/env python3
"""마지막 장 · 실전 연습장 (practice/index.html) — 경기장 매표소 · 스포츠용품점 · 시청 정책실 · 중앙은행 상황실."""
import os, sys, json, html
B = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(B))
OUT = sys.argv[1] if len(sys.argv) > 1 else ROOT
SP = json.load(open(os.path.join(B, 'sprites.json')))
def spr(k):
    a = SP['alias'].get(k, k); return SP['img'][a]
NEED = ['doc_front', 'doc_judge', 'doc_think', 'asst_report', 'asst_smile', 'fly_point', 'fly_arms', 'robo_coin', 'robo_happy', 'robo_sigh', 'sia_start', 'moa_judge', 'x2_watch']
IMG = {k: spr(k) for k in NEED}

CSS = r'''
:root{--bg:#fff;--panel2:#f5f6f9;--rule:#d9dce5;--text:#1d2030;--muted:#545a6e;--green:#137a45;--blue:#2457b8;--red:#c0392b;--amber:#8f5f00;--violet:#6a3fc2;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:#fff;color:var(--text);font-family:Pretendard,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",system-ui,sans-serif;line-height:1.75;font-size:16px}
header.top{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px 24px;border-bottom:1px solid var(--rule);flex-wrap:wrap;background:#fff;position:sticky;top:0;z-index:5}
header.top .brand{font-weight:800;color:var(--green);text-decoration:none}header.top nav a{margin-left:16px;color:var(--blue);font-size:14px}
main{max-width:1120px;margin:0 auto;padding:22px 20px 60px}
.eyebrow{font-size:13px;font-weight:700;color:var(--green);letter-spacing:.04em;margin:18px 0 4px}
h1{font-size:clamp(28px,4.6vw,44px);line-height:1.25;margin:4px 0 12px}.lead{font-size:18px;color:var(--muted);margin:0 0 18px}
.cast{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:18px 0}
.cast div{border:1px solid var(--rule);border-radius:14px;padding:10px;display:flex;gap:10px;align-items:center;background:var(--panel2)}
.cast img,.say img{width:52px;height:52px;image-rendering:pixelated;object-fit:contain;flex:none}.cast b{display:block;font-size:14px}.cast span{font-size:13px;color:var(--muted)}
.howto{border-left:4px solid var(--green);background:#f2f8f4;padding:12px 16px;border-radius:0 10px 10px 0;margin:14px 0 22px;font-size:15px}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0 0;position:sticky;top:58px;background:#fff;padding:8px 0;z-index:4}
.tabs button{font:inherit;font-size:15px;font-weight:700;border:1px solid var(--rule);background:#fff;border-radius:999px;padding:8px 16px;cursor:pointer;color:var(--text)}
.tabs button[aria-selected=true]{background:var(--text);color:#fff;border-color:var(--text)}
.sim{display:none;border:1px solid var(--rule);border-radius:20px;padding:22px;margin-top:10px;background:#fff}.sim.on{display:block}
.sim h2{margin:0 0 4px;font-size:26px}.sim .q{color:var(--muted);margin:0 0 14px}
.scene{background:var(--panel2);border-radius:12px;padding:12px 16px;font-size:15px;margin-bottom:16px}
.grid{display:grid;grid-template-columns:320px 1fr;gap:20px}
.controls{border:1px solid var(--rule);border-radius:14px;padding:14px;background:#fff;align-self:start}
.controls h3{font-size:15px;margin:6px 0 8px}.controls h3.env{color:var(--green)}.controls h3.me{color:var(--blue)}
.ctl{margin:10px 0}.ctl label{display:flex;justify-content:space-between;font-size:14px;font-weight:600;gap:8px}
.ctl output{font-variant-numeric:tabular-nums}.ctl.env output{color:var(--green)}.ctl.me output{color:var(--blue)}
.ctl input[type=range]{width:100%}.ctl.env input{accent-color:var(--green)}.ctl.me input{accent-color:var(--blue)}
.score{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px}
.score div{border:1px solid var(--rule);border-radius:12px;padding:10px 12px}.score b{display:block;font-size:22px;font-variant-numeric:tabular-nums}.score span{font-size:13px;color:var(--muted)}
.score .good b{color:var(--green)}.score .bad b{color:var(--red)}.score .mid b{color:var(--amber)}.score .info b{color:var(--blue)}
.charts{display:grid;grid-template-columns:1fr 1fr;gap:12px}.charts svg{width:100%;height:auto;border:1px solid var(--rule);border-radius:12px;background:#fff}
.talk{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0}
.say{display:flex;gap:10px;align-items:flex-start;border:1px solid var(--rule);border-radius:12px;padding:8px 10px}.say b{font-size:13px}.say p{margin:0;font-size:14px}
.missions{border:1px solid var(--rule);border-radius:14px;padding:12px 16px;margin-top:10px}.missions h3{margin:0 0 6px;font-size:16px}
.missions li{margin:6px 0;font-size:15px}.missions li .st{display:inline-block;min-width:64px;font-size:12px;font-weight:700;border-radius:999px;padding:1px 8px;margin-right:6px;background:#eef0f5;color:var(--muted);text-align:center}
.missions li.done .st{background:#e3f3ea;color:var(--green)}
.back{font-size:14px;margin-top:10px}.back a{color:var(--blue);margin-right:12px}
.wrapup{border:2px solid var(--green);border-radius:16px;padding:16px 20px;margin-top:26px}
.notice{font-size:13px;color:var(--amber);background:#fff8e6;border-radius:8px;padding:8px 12px}
footer{border-top:1px solid var(--rule);margin-top:30px;padding-top:14px;font-size:13px;color:var(--muted)}
@media (max-width:860px){.grid,.charts,.talk{grid-template-columns:1fr}.cast{grid-template-columns:repeat(2,1fr)}.score{grid-template-columns:repeat(2,1fr)}}
'''

SCENES = [
 dict(id='ticket', tab='① 경기장 매표소', title='경기장 매표소 — 결승전 티켓 값 정하기',
      q='좌석은 정해져 있어요. 정가를 얼마로 해야 빈자리도 암표도 없을까요?',
      scene='결승전 좌석이 정해져 있어요(공급은 고정). 팬들의 수요는 Q<sub>d</sub> = 인기 − 2P(천 석, P는 만 원)예요. 정가가 너무 낮으면 표가 모자라 암표가 돌고, 너무 높으면 빈자리가 생겨요.',
      env=[('A', '인기(수요 크기)', 12, 30, 1, 20, ''), ('S', '좌석 수(천 석)', 4, 16, 1, 10, '')], me=[('P', '티켓 정가(만 원)', 1, 12, .25, 3, '')],
      missions=['빈 좌석도 암표도 없는 정가(균형가격) 찾기 — 오차 0.25만 원 이내', '함정 관찰: 정가를 균형보다 1만 원 이상 낮게 두고, 암표 가격이 정가보다 높아지는 것 확인하기', '인기나 좌석 수를 바꾼 뒤에도 균형 정가 다시 찾기'],
      back=[('03_supply_demand.html#lv3', 'CH03 균형'), ('05_government_policy.html#lv1', 'CH05 가격상한'), ('06_market_efficiency.html#lv3', 'CH06 총잉여')]),
 dict(id='shop', tab='② 스포츠용품점', title='스포츠용품점 — 운동화 값 정하기',
      q='매출을 가장 크게 하는 값과 이윤을 가장 크게 하는 값은 같을까요?',
      scene='운동화 수요는 Q = 120 − b·P(켤레, P는 천 원)예요. 근처에 경쟁 가게가 많을수록 b가 커져(더 탄력적) 값에 민감해져요. 한 켤레 원가는 c예요.',
      env=[('b', '경쟁 정도 b(클수록 탄력적)', .5, 3, .25, 1, ''), ('c', '한 켤레 원가(천 원)', 0, 40, 2, 20, '')], me=[('P', '판매가(천 원)', 5, 115, 1, 40, '')],
      missions=['이윤이 가장 큰 판매가 찾기 — 오차 1천 원 이내', '함정 관찰: 원가가 10 이상일 때 매출이 가장 큰 가격(탄력성 1)에 두고, 이윤이 최대가 아닌 것 확인하기', '경쟁 정도 b를 바꾼 뒤 이윤 최대 판매가 다시 찾기'],
      back=[('04_elasticity.html#lv2', 'CH04 탄력성과 매출'), ('08_market_structure.html#lv2', 'CH08 MR = MC')]),
 dict(id='city', tab='③ 시청 정책실', title='시청 정책실 — 공장 매연에 세금 매기기',
      q='세금이 클수록 좋을까요? 이웃 피해만큼만 매기면 어떻게 될까요?',
      scene='시장 수요 P = 100 − Q, 공장의 사적 비용 P = 20 + Q예요. 한 단위마다 이웃에게 D만큼 피해가 생겨요. 시청은 단위당 세금 t를 정해요. 판정은 이웃 피해까지 넣은 사회적 총잉여예요.',
      env=[('D', '한 단위당 이웃 피해 D', 0, 40, 2, 20, '')], me=[('t', '단위당 세금 t', 0, 60, 1, 0, '')],
      missions=['피해 D = 20에서 사회적 총잉여가 가장 큰 세금 찾기 — 오차 1 이내', '함정 관찰: 피해가 0인데 세금을 20 이상 매겨 사중손실이 생기는 것 확인하기', '피해 D를 20이 아닌 값으로 바꾼 뒤 최적 세금 다시 찾기'],
      back=[('07_cost_of_taxation.html#lv1', 'CH07 사중손실'), ('09_market_failure.html#lv1', 'CH09 피구세')]),
 dict(id='bank', tab='④ 중앙은행 상황실', title='중앙은행 상황실 — 금리와 지출로 경기 맞추기',
      q='경기 갭을 0으로 만드는 손잡이 조합은 무엇일까요?',
      scene='처음 GDP 갭이 주어져요(음수 = 침체, 양수 = 과열). 기준금리 1%p 인하 = 갭 +1.2%p, 정부지출 1조 원 = 갭 +1.5%p(승수·구축효과를 반영한 설명용 값). 물가상승률 = 2 + 0.6 × 갭.',
      env=[('g0', '처음 GDP 갭(%)', -4, 4, 1, -3, '')], me=[('r', '기준금리(%)', .5, 6, .25, 3, ''), ('dG', '정부지출 변화(조 원)', -3, 4, .5, 0, '')],
      missions=['침체(처음 갭 음수)에서 정책 뒤 갭을 ±0.3% 안으로 맞추기', '함정 관찰: 금리는 그대로(3%) 두고 지출만 3.5조 이상 늘려 과열(갭 +2% 이상) 확인하기', '과열(처음 갭 양수)로 바꾼 뒤 갭을 ±0.3% 안으로 맞추기'],
      back=[('10_macro_economy.html#lv3', 'CH10 필립스 곡선'), ('11_economic_policy.html#lv3', 'CH11 정책조합')]),
]

JS = r'''
var IMG=__IMG__;
function $(s,r){return (r||document).querySelector(s)}function $$(s,r){return [].slice.call((r||document).querySelectorAll(s))}
function f(v,d){return Number(v).toLocaleString('ko-KR',{minimumFractionDigits:d||0,maximumFractionDigits:d||0})}
function svg(w,h,body){return '<svg viewBox="0 0 '+w+' '+h+'" role="img">'+body+'</svg>'}
function tw(t,z){var w=0;String(t).split('').forEach(function(ch){w+=/[\u3131-\uD79D]/.test(ch)?z*0.98:/[A-Z0-9%$]/.test(ch)?z*0.62:z*0.5});return w}
function chart(o){var W=460,H=280,L=46,R=12,T=30,Bt=34,pw=W-L-R,ph=H-T-Bt,BX=[];function hit(b){return BX.some(function(a){return b.x<a.x+a.w&&b.x+b.w>a.x&&b.y<a.y+a.h&&b.y+b.h>a.y})}function X(v){return L+(v-o.x0)/(o.x1-o.x0)*pw}function Y(v){return T+ph-(v-o.y0)/(o.y1-o.y0)*ph}
 var s='<text x="'+L+'" y="18" font-size="13" font-weight="700" fill="#1d2030">'+o.title+'</text>';BX.push({x:L,y:5,w:tw(o.title,13),h:16});if(o.key)BX.push({x:L+pw-tw(o.key,11),y:7,w:tw(o.key,11),h:14});
 for(var i=0;i<=4;i++){var yv=o.y0+(o.y1-o.y0)*i/4,y=Y(yv);s+='<line x1="'+L+'" x2="'+(L+pw)+'" y1="'+y+'" y2="'+y+'" stroke="#eceef4"/><text x="'+(L-6)+'" y="'+(y+4)+'" font-size="10" text-anchor="end" fill="#545a6e">'+f(yv,o.yd||0)+'</text>'}
 for(var i=0;i<=4;i++){var xv=o.x0+(o.x1-o.x0)*i/4,x=X(xv);s+='<text x="'+(i?x:x+2)+'" y="'+(T+ph+14)+'" font-size="10" text-anchor="'+(i?'middle':'start')+'" fill="#545a6e">'+f(xv,o.xd||0)+'</text>'}
 s+='<line x1="'+L+'" x2="'+L+'" y1="'+T+'" y2="'+(T+ph)+'" stroke="#999"/><line x1="'+L+'" x2="'+(L+pw)+'" y1="'+(T+ph)+'" y2="'+(T+ph)+'" stroke="#999"/>';
 s+='<text x="'+(L+pw)+'" y="'+(H-4)+'" font-size="10" text-anchor="end" fill="#545a6e">'+o.xl+'</text>';
 (o.lines||[]).forEach(function(l){var p=[],n=80;for(var i=0;i<=n;i++){var x=o.x0+(o.x1-o.x0)*i/n,y=l.f(x);if(isFinite(y)&&y>=o.y0-1e-9&&y<=o.y1+1e-9)p.push(X(x).toFixed(1)+','+Y(y).toFixed(1));else if(p.length&&p[p.length-1]!=='M')p.push('M')}var d='',st=true;p.forEach(function(q){if(q==='M'){st=true;return}d+=(st?'M':'L')+q+' ';st=false});s+='<path d="'+d+'" fill="none" stroke="'+l.c+'" stroke-width="'+(l.w||2.4)+'"'+(l.dash?' stroke-dasharray="5 4"':'')+'/>'});
 (o.vlines||[]).forEach(function(v){s+='<line x1="'+X(v.x)+'" x2="'+X(v.x)+'" y1="'+T+'" y2="'+(T+ph)+'" stroke="'+v.c+'" stroke-width="'+(v.w||2.4)+'"'+(v.dash?' stroke-dasharray="4 3"':'')+'/>'});
 (o.hlines||[]).forEach(function(v){s+='<line x1="'+L+'" x2="'+(L+pw)+'" y1="'+Y(v.y)+'" y2="'+Y(v.y)+'" stroke="'+v.c+'" stroke-width="1.6" stroke-dasharray="5 4"/>'+(v.l?(function(){var yy=Y(v.y)-4<T+10?Y(v.y)+12:Y(v.y)-4;BX.push({x:L+pw-2-tw(v.l,10),y:yy-9,w:tw(v.l,10),h:12});return '<text x="'+(L+pw-2)+'" y="'+yy+'" font-size="10" text-anchor="end" fill="'+v.c+'">'+v.l+'</text>'})():'')});
 var DP=(o.dots||[]).map(function(d){var x=X(Math.max(o.x0,Math.min(o.x1,d.x))),y=Y(Math.max(o.y0,Math.min(o.y1,d.y)));BX.push({x:x-6,y:y-6,w:12,h:12});s+='<circle cx="'+x+'" cy="'+y+'" r="5.5" fill="'+d.c+'" stroke="#fff" stroke-width="1.5"/>';return {d:d,x:x,y:y}});
 DP.forEach(function(q){var d=q.d,w=tw(d.l,11),pref=(d.dx||8)<0?-1:1,C=[];[-8,10,-20,22,-32,34].forEach(function(dy){C.push([pref,dy]);C.push([-pref,dy])});var pick=null;
  for(var k=0;k<C.length;k++){var lx=C[k][0]>0?q.x+8:q.x-8-w,ly=q.y+C[k][1];if(lx<2||lx+w>W-2||ly-10<2||ly+2>H-2)continue;var b={x:lx,y:ly-10,w:w,h:13};if(!hit(b)){pick=[lx,ly,b];break}}
  if(!pick){var lx=Math.max(2,Math.min(W-2-w,q.x+8)),ly=Math.max(12,Math.min(H-4,q.y-8));pick=[lx,ly,{x:lx,y:ly-10,w:w,h:13}]}
  BX.push(pick[2]);s+='<text x="'+pick[0]+'" y="'+pick[1]+'" font-size="11" font-weight="700" fill="'+d.c+'">'+d.l+'</text>'});
 if(o.key)s+='<text x="'+(L+pw)+'" y="18" font-size="11" text-anchor="end" fill="#545a6e">'+o.key+'</text>';
 return svg(W,H,s)}
function say(who,mood,name,t){return '<div class="say"><img src="'+IMG[who+'_'+mood]+'" alt=""><div><b>'+name+'</b><p>'+t+'</p></div></div>'}
function score(items){return items.map(function(k){return '<div class="'+k[2]+'"><b>'+k[0]+'</b><span>'+k[1]+'</span></div>'}).join('')}
var MODEL={
 ticket:function(v){var Pe=(v.A-v.S)/2,qd=Math.max(0,v.A-2*v.P),sold=Math.min(qd,v.S),empty=v.S-sold,short=Math.max(0,qd-v.S),black=short>0?(v.A-v.S)/2:null,rev=v.P*sold,near=Math.abs(v.P-Pe)<=.2501;
  var opt=Math.max(v.A/4,Pe),R=function(p){return p*Math.min(Math.max(0,v.A-2*p),v.S)};
  return {sc:[[f(sold,1)+'천 석','판매 좌석',empty>0.01?'bad':'good'],[f(empty,1)+'천 석','빈 좌석',empty>0.01?'bad':'good'],[black?f(black,2)+'만 원':'없음','암표 가격(모자랄 때)',black?'bad':'good'],[f(rev,1)+'천만 원','매출','info']],
   c1:chart({title:'수요(파랑)·좌석(빨강)·정가(주황)',x0:0,x1:30,y0:0,y1:15,xl:'좌석(천 석)',lines:[{f:function(q){return (v.A-q)/2},c:'#2457b8'}],vlines:[{x:v.S,c:'#c0392b'}],hlines:[{y:v.P,c:'#8f5f00',l:'정가'}],dots:[{x:v.S,y:Pe,c:'#137a45',l:'균형 '+f(Pe,2)}]}),
   c2:chart({title:'정가별 매출(초록)',x0:0,x1:15,y0:0,y1:Math.max(10,R(opt)*1.2),xl:'정가(만 원)',yd:0,lines:[{f:R,c:'#137a45'}],dots:[{x:v.P,y:R(v.P),c:'#2457b8',l:'내 정가'},{x:opt,y:R(opt),c:'#c0392b',l:'매출 최대',dx:-8}]}),
   talk:[say('doc',near?'judge':'think','박사',near?'빈자리도 줄서기도 없는 정가예요. 가격이 신호등 역할을 했어요.':'정가가 균형('+f(Pe,2)+'만 원)과 어긋나 있어요. 남거나 모자라는 쪽을 보세요.'),say('asst','report','하루',short>0?'표가 '+f(short,1)+'천 석 모자라요. 3개를 놓고 사려는 사람처럼 암표가 '+f(black,2)+'만 원까지 올라가요.':empty>0?'빈 좌석이 '+f(empty,1)+'천 석이에요.':'좌석이 꼭 맞게 팔렸어요.'),say('fly','point','초파리 조교',v.P<Pe?'정가가 싸면 팬에게 좋아 보이지? 그 차액은 암표상 주머니로 가.':'좌석 수 슬라이더를 바꿔 봐. 균형이 함께 움직여.'),say('robo',v.P<Pe?'happy':'coin','주판봇 조교',v.P<Pe?'싸게 팔면 다들 좋아하겠지!':'비싸게 받으면 무조건 더 벌겠지!')],
   m:[near&&v.A>0,v.P<=Pe-1&&black>v.P,near&&(v.A!==20||v.S!==10)]}},
 shop:function(v){var Q=function(p){return Math.max(0,120-v.b*p)},q=Q(v.P),e=q>0?v.b*v.P/q:Infinity,rev=v.P*q,pr=(v.P-v.c)*q,Popt=(120/v.b+v.c)/2,Prev=60/v.b,Pf=function(p){return (p-v.c)*Q(p)},near=Math.abs(v.P-Popt)<=1;
  return {sc:[[f(q,0)+'켤레','판매량','info'],[isFinite(e)?f(e,2):'∞','가격탄력성',e>1?'mid':'info'],[f(rev,0),'매출(천 원)','info'],[f(pr,0),'이윤(천 원)',near?'good':pr<0?'bad':'mid']],
   c1:chart({title:'수요(파랑)와 내 판매가',x0:0,x1:130,y0:0,y1:Math.max(10,120/v.b),xl:'판매량(켤레)',lines:[{f:function(x){return (120-x)/v.b},c:'#2457b8'}],hlines:[{y:v.c,c:'#c0392b',l:'원가'}],dots:[{x:q,y:v.P,c:'#8f5f00',l:'나'}]}),
   c2:chart({title:'판매가별 매출(파랑)·이윤(초록)',x0:0,x1:Math.min(120,120/v.b),y0:Math.min(0,Pf(0)),y1:Math.max(100,Prev*Q(Prev)*1.1),xl:'판매가(천 원)',lines:[{f:function(p){return p*Q(p)},c:'#2457b8'},{f:Pf,c:'#137a45'}],dots:[{x:v.P,y:pr,c:'#8f5f00',l:'내 이윤'},{x:Popt,y:Pf(Popt),c:'#137a45',l:'이윤 최대',dx:-8},{x:Prev,y:Prev*Q(Prev),c:'#2457b8',l:'매출 최대'}]}),
   talk:[say('doc',near?'judge':'think','박사',near?'이윤 최대 판매가예요. 한 켤레 더 팔 때 수입과 비용이 같은 곳이에요.':'매출 꼭대기와 이윤 꼭대기를 그래프에서 비교해 보세요.'),say('asst','report','하루','지금 탄력성 '+(isFinite(e)?f(e,2):'∞')+', 이윤 '+f(pr,0)+'천 원이에요. 이윤 최대는 '+f(Popt,1)+'천 원 근처예요.'),say('fly','point','초파리 조교',v.c>0?'원가가 있으면 매출 최대 가격이 이윤 최대 가격이 아니야. 원가를 0으로 바꿔 봐.':'원가가 0이면 매출 최대 = 이윤 최대야.'),say('robo',Math.abs(v.P-Prev)<1?'happy':'coin','주판봇 조교','매출이 제일 큰 가격이 최고 아니야?')],
   m:[near,v.c>=10&&Math.abs(v.P-Prev)<=1&&pr<Pf(Popt)-1,near&&v.b!==1]}},
 city:function(v){var Q=Math.max(0,(80-v.t)/2),Qo=Math.max(0,(80-v.D)/2),W=function(q){return 80*q-q*q-v.D*q},Wt=function(t){return W(Math.max(0,(80-t)/2))},loss=W(Qo)-W(Q),near=Math.abs(v.t-v.D)<=1;
  return {sc:[[f(Q,1),'거래량(최적 '+f(Qo,1)+')','info'],[f(v.t*Q,0),'세수','info'],[f(W(Q),0),'사회적 총잉여',near?'good':'mid'],[f(loss,0),'남은 손실',loss<1?'good':'bad']],
   c1:chart({title:'수요(파랑)·사적 비용(빨강)·사회적 비용(보라)',x0:0,x1:60,y0:0,y1:110,xl:'생산량',lines:[{f:function(q){return 100-q},c:'#2457b8'},{f:function(q){return 20+q},c:'#c0392b'},{f:function(q){return 20+q+v.D},c:'#6a3fc2',dash:1}],dots:[{x:Q,y:100-Q,c:'#8f5f00',l:'시장'},{x:Qo,y:100-Qo,c:'#137a45',l:'최적',dx:-8}]}),
   c2:chart({title:'세금별 사회적 총잉여',x0:0,x1:60,y0:Math.min(0,Wt(60)),y1:Math.max(10,W(Qo)*1.15),xl:'세금 t',lines:[{f:Wt,c:'#137a45'}],dots:[{x:v.t,y:W(Q),c:'#8f5f00',l:'내 세금'},{x:v.D,y:W(Qo),c:'#c0392b',l:'t = D',dx:-8}]}),
   talk:[say('doc',near?'judge':'think','박사',near?'세금이 피해와 같아 시장이 스스로 최적량을 골랐어요(피구세).':'세금과 피해의 차이를 보세요. 작으면 너무 많이, 크면 너무 적게 만들어요.'),say('asst','report','하루','지금 거래량 '+f(Q,1)+', 최적 '+f(Qo,1)+'. 남은 손실 '+f(loss,0)+'이에요.'),say('fly','point','초파리 조교',v.D===0?'피해가 없는데 세금을 매기면 그냥 사중손실이야.':'피해 D를 바꾸면 최적 세금도 같이 움직여.'),say('robo',v.t>v.D+5?'happy':'coin','주판봇 조교','세금은 높을수록 공장이 정신 차리지!')],
   m:[v.D===20&&near,v.D===0&&v.t>=20&&loss>1,v.D!==20&&near]}},
 bank:function(v){var y=v.g0-1.2*(v.r-3)+1.5*v.dG,inf=2+.6*y,ok=Math.abs(y)<=.3001,G=function(r){return v.g0-1.2*(r-3)+1.5*v.dG};
  return {sc:[[f(y,1)+'%','정책 뒤 GDP 갭',ok?'good':'bad'],[f(inf,1)+'%','물가상승률',inf>3?'bad':'good'],[f(v.r+2,2)+'%','대출금리','info'],[f(v.dG,1)+'조','재정 지출 변화',Math.abs(v.dG)>3?'mid':'info']],
   c1:chart({title:'기준금리별 GDP 갭(지금 지출 유지)',x0:.5,x1:6,y0:-8,y1:8,xl:'기준금리(%)',xd:1,lines:[{f:G,c:'#2457b8'}],hlines:[{y:0,c:'#137a45',l:'잠재 GDP'}],dots:[{x:v.r,y:y,c:'#8f5f00',l:'지금'}]}),
   c2:chart({title:'필립스 관계: 갭 → 물가',x0:-8,x1:8,y0:-3,y1:7,xl:'GDP 갭(%)',lines:[{f:function(g){return 2+.6*g},c:'#c0392b'}],hlines:[{y:2,c:'#137a45',l:'물가 목표 2%'}],dots:[{x:y,y:inf,c:'#8f5f00',l:'지금'}]}),
   talk:[say('doc',ok?'judge':'think','박사',ok?'갭이 0 근처예요. 침체도 과열도 아니에요.':(y<0?'아직 침체예요. 금리를 내리거나 지출을 늘려 보세요.':'과열이에요. 금리를 올리거나 지출을 줄여 보세요.')),say('asst','report','하루','금리 효과 '+f(-1.2*(v.r-3),1)+'%p, 재정 효과 '+f(1.5*v.dG,1)+'%p, 합쳐서 갭 '+f(y,1)+'%예요.'),say('fly','point','초파리 조교','손잡이 두 개를 조금씩. 한쪽만 세게 돌리면 반대로 넘어가.'),say('robo',v.dG>=3?'happy':'coin','주판봇 조교','침체엔 돈을 왕창 푸는 게 최고지!')],
   m:[v.g0<0&&ok,v.r===3&&v.dG>=3.5&&y>=2,v.g0>0&&ok]}}};
var DONE={},TOUCH={};
function render(id){var box=$('#'+id),v={};$$('input',box).forEach(function(i){v[i.name]=+i.value;$('output[for='+i.id+']').textContent=i.value});var o=MODEL[id](v);
 $('.score',box).innerHTML=score(o.sc);$('.c1',box).innerHTML=o.c1;$('.c2',box).innerHTML=o.c2;$('.talk',box).innerHTML=o.talk.join('');
 DONE[id]=DONE[id]||[false,false,false];if(TOUCH[id])o.m.forEach(function(x,i){if(x)DONE[id][i]=true});
 $$('.missions li',box).forEach(function(li,i){li.classList.toggle('done',DONE[id][i]);$('.st',li).textContent=DONE[id][i]?'통과 ✓':'도전 중'});
 var n=Object.keys(MODEL).reduce(function(s,k){return s+(DONE[k]||[]).filter(Boolean).length},0);$('#total').textContent=n+' / 12'}
function show(id){$$('.sim').forEach(function(s){s.classList.toggle('on',s.id===id)});$$('.tabs button').forEach(function(b){b.setAttribute('aria-selected',String(b.dataset.t===id))});if(location.hash!=='#'+id)history.replaceState(null,'','#'+id);render(id)}
$$('.tabs button').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t)})});
$$('.sim').forEach(function(s){$$('input',s).forEach(function(i){i.addEventListener('input',function(){TOUCH[s.id]=true;render(s.id)})});render(s.id)});
window.__MODEL=MODEL;
show((location.hash||'').slice(1) in MODEL?location.hash.slice(1):'ticket');
'''

def ctl(prefix, cls, items):
    o = []
    for k, lab, a, b, st, v, _ in items:
        i = f'{prefix}-{k}'
        o.append(f'<div class="ctl {cls}"><label for="{i}">{lab}<output for="{i}">{v}</output></label><input type="range" id="{i}" name="{k}" min="{a}" max="{b}" step="{st}" value="{v}"></div>')
    return ''.join(o)

def page():
    e = html.escape
    tabs = ''.join(f'<button type="button" role="tab" data-t="{s["id"]}" aria-selected="false">{s["tab"]}</button>' for s in SCENES)
    sims = []
    for s in SCENES:
        ms = ''.join(f'<li><span class="st">도전 중</span>{m}</li>' for m in s['missions'])
        bk = ''.join(f'<a href="../{h}">{t}</a>' for h, t in s['back'])
        sims.append(f'''<section class="sim" id="{s["id"]}" role="tabpanel" aria-label="{e(s["title"])}"><h2>{s["title"]}</h2><p class="q">{s["q"]}</p><div class="scene">{s["scene"]}</div>
<div class="grid"><div class="controls"><h3 class="env">시장 환경(초록)</h3>{ctl(s["id"], "env", s["env"])}<h3 class="me">내 결정(파랑)</h3>{ctl(s["id"], "me", s["me"])}</div>
<div><div class="score"></div><div class="charts"><div class="c1"></div><div class="c2"></div></div></div></div>
<div class="talk"></div><div class="missions"><h3>미션 3개 — 조작해야 판정해요</h3><ol style="list-style:none;padding:0;margin:0">{ms}</ol></div><p class="back">배운 곳 다시 보기: {bk}</p></section>''')
    cast = ''.join(f'<div><img src="{IMG[k]}" alt=""><span><b>{n}</b>{r}</span></div>' for k, n, r in [('doc_front', '박사', '판정과 정리'), ('asst_smile', '하루', '숫자 보고'), ('fly_point', '초파리 조교', '의심과 힌트'), ('robo_coin', '주판봇 조교', '성급한 확신')])
    return f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>마지막 장 · 실전 연습장 — 경제학 원론 연구실</title>
<meta name="description" content="경기장 매표소·스포츠용품점·시청 정책실·중앙은행 상황실을 직접 운영하며 수요와 공급, 탄력성, 피구세, 정책조합을 연습하는 시뮬레이터. 한국체육대학교 교양과정 강의노트 기반.">
<meta property="og:title" content="마지막 장 · 실전 연습장 — 경제학 원론 연구실"><meta property="og:image" content="https://adminmrobo.github.io/basic_economic_lab/assets/og/cover_prac.jpg">
<style>{CSS}</style></head>
<body>
<header class="top"><a class="brand" href="../index.html">경제학 원론 연구실</a><nav><a href="../index.html">목차</a><a href="../11f_final_review.html">기말 정리</a><a href="../tower.html">건물 보기</a><a href="#wrap">정리</a></nav></header>
<main>
<p class="eyebrow">마지막 장 · 실전 연습장 · 골목 끝 광장 경기장</p>
<h1>매표소·용품점·시청·중앙은행을<br>직접 운영해 보세요</h1>
<p class="lead">열한 강의에서 배운 수요와 공급, 탄력성, 외부효과와 세금, 경제정책을 네 곳에서 연습합니다. 슬라이더를 움직이면 성적표와 그래프, 강의실 식구들의 말이 바로 바뀌어요.</p>
<div class="cast">{cast}</div>
<p class="howto"><b>사용법</b> · 초록 슬라이더는 내가 바꿀 수 없는 시장 환경, 파랑 슬라이더는 내 결정이에요. 미션은 슬라이더를 직접 움직인 뒤에만 판정해요. 주소 끝에 #ticket, #shop, #city, #bank를 붙이면 그 장면이 바로 열려요. 진행 기록은 이 탭에서만 유지돼요. <b>통과한 미션: <span id="total">0 / 12</span></b></p>
<nav class="tabs" role="tablist" aria-label="장면 고르기">{tabs}</nav>
{"".join(sims)}
<section class="wrapup" id="wrap"><h2>마무리 — 네 장면이 함께 묻는 질문</h2>
<p>매표소의 정가, 용품점의 판매가, 시청의 세금, 중앙은행의 금리는 모두 "한 단위 더 바꾸면 무엇이 늘고 무엇이 주나"를 비교해 정했어요. 그리고 네 곳 모두 "크게, 많이"가 답이 아니었어요. 균형을 찾는 것, 이윤 꼭대기와 매출 꼭대기를 구분하는 것, 피해만큼만 세금을 매기는 것, 갭만큼만 경기를 조절하는 것이 핵심이었습니다.</p>
<p class="notice">모형의 한계: 모든 숫자는 교육용 예시이며 직선 수요·공급과 고정된 효과 계수를 가정했어요. 실제 시장과 정책 효과는 추정이 필요하고 시차와 불확실성이 큽니다. 경영·투자 권고가 아닙니다.</p></section>
<footer>본 강의는 한국체육대학교 교양과정의 「경제학의 이해」, 「생활 속의 경제학」 강의노트를 기반으로 제작됐습니다.<br>글 · 안상선 (<a href="https://www.ahnboat.xyz" target="_blank" rel="noopener">www.ahnboat.xyz</a>) · (주)M-Robo 대표 · 경제학 원론 연구실 실전 연습장 v1.0 · 2026-11-23<br>캐릭터 이름·설정·그림의 저작권은 안상선(개인)에게 있으며 허락 없이 쓸 수 없습니다.</footer>
</main>
<script>{JS.replace('__IMG__', json.dumps(IMG))}</script>
</body></html>'''

if __name__ == '__main__':
    d = os.path.join(OUT, 'practice'); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, 'index.html'); import pxfix; open(p, 'w', encoding='utf-8').write(pxfix.apply(page())); print(p, os.path.getsize(p) // 1024, 'KB')
