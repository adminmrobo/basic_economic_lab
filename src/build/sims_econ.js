/* 경제학 원론 연구실 실험 모듈 (설명용 모형, 숫자는 예시값) */
function barPlot(c,H,title,items,max,sub){var W=fit(c,H),ctx=c.getContext('2d');ctx.clearRect(0,0,W,H);grid(ctx,W,H);txt(ctx,title,16,18,COL.text,13,'left',true);if(sub)txt(ctx,sub,16,34,COL.muted,11,'left');
  var m=max||Math.max.apply(null,items.map(function(i){return Math.abs(i.v)}).concat([1]))*1.15;bars(ctx,24,H-28,W-48,H-(sub?80:64),items,m);return {ctx:ctx,W:W}}
function won1(v){return nf(Math.round(v))+'만 원'}

/* ===== CH01 경제학의 10대 원리 ===== */
/* 희소성: 원하는 양과 있는 양 */
SIMS.scarce=function(el,cfg){var c=S0(el,cfg,250,'원하는 양과 있는 양으로 보는 희소성'),row=rows(el),K=kpis(el,4),I=insight(el);
  var G=[{n:'공기',have:1000,want:300},{n:'생수',have:300,want:420},{n:'외발가재',have:20,want:10},{n:'양발가재',have:200,want:600}],k=1;
  buttons(row,'재화',G.map(function(g,i){return [i,g.n]}),k,function(v){k=v;sh.set(G[k].have);sw.set(G[k].want)});
  var sh=S(row,'있는 양(존재량)',0,1000,10,G[k].have,null,function(v){G[k].have=v;draw()}),sw=S(row,'사람들이 원하는 양',0,1000,10,G[k].want,null,function(v){G[k].want=v;draw()});
  function draw(){var it=[];G.forEach(function(g){it.push({v:g.have,c:COL.s,l:'',t:g.have});it.push({v:g.want,c:COL.a,l:'',t:g.want})});
    barPlot(c,250,'재화별 있는 양(파랑)과 원하는 양(주황)',it,1100);(function(){var ctx=c.getContext('2d'),W=c.clientWidth,x0=24,w=W-48,gw=w/G.length;G.forEach(function(g,i){fitLab(ctx,g.n,x0+gw*i+gw/2,250-28+16,gw-6,COL.muted,11)})})();var g=G[k],sc=g.want>g.have,ratio=g.want/Math.max(1,g.have);
    K([[g.have,'있는 양','i'],[g.want,'원하는 양','a'],[sc?'희소함':'희소하지 않음','판정',sc?'r':'g'],[sc?'경제재(값을 치름)':'무료재(자유재)','분류','m']]);
    I([[sc?'r':'g',sc?'원하는 양이 있는 양보다 많아요. 값을 치러야 얻을 수 있는 경제재입니다.':'있는 양이 원하는 양보다 많아요. 값을 치르지 않아도 되는 무료재(자유재)예요.'],['i','희소성은 "드물다(희귀)"가 아니라 "원하는 것에 비해 모자라다"는 뜻이에요. 외발가재는 드물지만 원하는 사람이 적어 양발가재보다 싸게 팔릴 수 있어요. 원하는 양 ÷ 있는 양 = '+f1(ratio,2)+'.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* 기회비용: 쇼핑몰 창업 */
SIMS.oppcost=function(el,cfg){var c=S0(el,cfg,250,'명시적 비용과 암묵적 비용'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var w=300,inv=10000,rev=13000,r=0;
  S(row,'모델 월급(만 원)',100,600,10,w,null,function(v){w=v;draw()});S(row,'쇼핑몰 투입비용(만 원)',5000,15000,500,inv,null,function(v){inv=v;draw()});
  S(row,'쇼핑몰 1년 수입(만 원)',8000,18000,500,rev,null,function(v){rev=v;draw()});S(row,'투입금 이자율(%)',0,10,.5,r,fx(1),function(v){r=v;draw()});
  function draw(){var imp=w*12+inv*r/100,oc=inv+imp,acc=rev-inv,eco=rev-oc;
    barPlot(c,250,'쇼핑몰 1년: 수입과 비용 (만 원)',[{v:rev,c:COL.g,l:'수입',t:nf(rev)},{v:inv,c:COL.s,l:'명시적 비용',t:nf(inv)},{v:imp,c:COL.m,l:'암묵적 비용',t:nf(imp)},{v:oc,c:COL.r,l:'기회비용 합',t:nf(oc)}],Math.max(rev,oc)*1.15);
    K([[won1(acc),'회계상 이윤(수입 − 명시적 비용)',acc>=0?'i':'r'],[won1(imp),'암묵적 비용(포기한 월급·이자)','m'],[won1(oc),'기회비용 = 명시적 + 암묵적','a'],[won1(eco),'경제적 이윤',eco>=0?'g':'r']]);
    E('기회비용 = 투입비용 '+nf(inv)+' + 포기한 월급 '+w+' × 12 = '+nf(w*12)+(r?' + 포기한 이자 '+nf(inv*r/100):'')+' = <i>'+nf(oc)+'</i>만 원');
    I([[eco>=0?'g':'r',eco>=0?'수입이 기회비용보다 커요. 모델을 그만두고 창업해도 손해가 아니에요.':'회계상으로는 '+won1(acc)+'를 벌지만, 포기한 월급까지 넣으면 '+won1(-eco)+' 손해예요. 창업하려면 수입이 '+won1(oc)+'은 넘어야 해요.'],['i','이 계산은 투입한 1억 원이 1년 안에 다 쓰인다(돌려받지 못한다)고 가정했어요. 이자율을 올리면 포기한 이자 수입도 기회비용에 들어가요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* 한계적 판단: 하루 훈련 시간 */
SIMS.marginal=function(el,cfg){var c=S0(el,cfg,260,'한 시간 더 훈련할 때의 편익과 비용'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var mc=cfg.mc||20,h=cfg.h||6;
  S(row,'훈련 1시간의 기회비용(아르바이트 시급, 천 원)',4,56,2,mc,null,function(v){mc=v;draw()});S(row,'내가 정한 훈련 시간',0,15,.5,h,fx(1),function(v){h=v;draw()});
  function B(x){return 60*x-2*x*x}
  function draw(){var hs=clamp((60-mc)/4,0,15),N=function(x){return B(x)-mc*x};
    var P=plot(c,260,{xlo:0,xhi:15,ylo:0,yhi:64,xl:'하루 훈련 시간',yl:'천 원 가치',title:'초록 한계편익 MB = 60 − 4h · 빨강 한계비용 MC'});
    P.fn(function(x){return 60-4*x},COL.g,2.4);P.seg(0,mc,15,mc,COL.r,2.2);
    if(h<hs)P.poly([[h,60-4*h],[hs,mc],[h,mc]],COL.a,.3);else if(h>hs)P.poly([[hs,mc],[h,mc],[h,60-4*h]],COL.r,.25);
    P.seg(h,0,h,64,COL.a,1.5,[3,3]);P.dot(hs,mc,COL.g,6,'최적 h*');stamp(P.ctx,P.W,'예시값');
    K([[f1(hs,1)+'시간','최적 훈련 시간 h*','g'],[f1(N(hs),0),'h*에서 순편익','g'],[f1(N(h),0),'내가 정한 시간의 순편익',N(h)>=N(hs)-.01?'g':'a'],[f1(N(hs)-N(h),0),'놓친 순편익','r']]);
    E('한 시간 더 할 때: MB = 60 − 4h = MC = '+mc+' → h* = (60 − '+mc+') ÷ 4 = <i>'+f1(hs,1)+'</i>');
    I([['g','합리적 판단은 "전부 아니면 전무"가 아니라 "한 시간 더?"를 묻는 것이에요(원리 3). 한계편익이 한계비용보다 크면 늘리고, 작으면 줄여요.'],['a','시급을 올려 보세요. 훈련 1시간의 기회비용이 커져 최적 시간이 줄어요. 사람들은 유인에 반응해요(원리 4).']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH02 경제학자처럼 생각하기 ===== */
SIMS.consfn=function(el,cfg){var c=S0(el,cfg,250,'소비함수 C = c·Y와 지원금의 효과'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var cc=.6,g=10,tgt=1;
  S(row,'한계소비성향 c',.1,.95,.05,cc,fx(2),function(v){cc=v;draw()});S(row,'1인당 지원금(만 원)',0,50,1,g,null,function(v){g=v;draw()});S(row,'목표 소비 증가(조 원)',.5,5,.5,tgt,fx(1),function(v){tgt=v;draw()});
  function draw(){var P=plot(c,250,{xlo:0,xhi:400,ylo:0,yhi:400,xl:'소득 Y(만 원)',yl:'소비 C',title:'파랑 C = c·Y · 회색 45°선(번 만큼 다 쓰기)'});
    P.seg(0,0,400,400,COL.muted,1,[4,4]);P.fn(function(y){return cc*y},COL.s,2.4);P.dot(250,cc*250,COL.s,5,'월 소득 250');P.dot(250+g,cc*(250+g),COL.g,5,'지원금 후',8,16);stamp(P.ctx,P.W,'단순화 모형');
    var dc=cc*g,need=tgt/cc;
    K([[f1(cc,2),'소득 1원 중 소비하는 몫 c','i'],[f1(dc,1)+'만 원','1인당 소비 증가 = c × 지원금','g'],[f1(need,2)+'조 원','목표 달성에 필요한 총 지원금','a'],[f1(1-cc,2),'저축으로 가는 몫','m']]);
    E('ΔC = c × ΔY = '+f1(cc,2)+' × '+g+' = <i>'+f1(dc,1)+'</i>만 원 · 필요한 지원금 = 목표 ÷ c = '+f1(tgt,1)+' ÷ '+f1(cc,2)+' = '+f1(need,2)+'조 원');
    I([['i','모형은 "소비는 소득으로만 정해진다"고 단순화했어요. 취향·유행·빚은 뺐습니다. 그래도 지원금 규모를 정하는 첫 계산에는 충분히 쓸모 있어요(정확성보다 유용성).'],['a','여기서는 한 번 쓴 돈이 다시 남의 소득이 되는 연쇄(승수효과)는 빼고 첫 단계만 봤어요. 연쇄는 CH11에서 다뤄요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.ppf=function(el,cfg){var c=S0(el,cfg,280,'생산가능곡선: 효율·상충관계·기회비용·성장'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var x=60,e=1,g=0,lin=0;
  S(row,'컴퓨터 생산량',0,100,5,x,null,function(v){x=v;draw()});S(row,'자원을 쓰는 정도',.5,1,.05,e,function(v){return Math.round(v*100)+'%'},function(v){e=v;draw()});
  S(row,'기술 진보(경제성장)',0,30,5,g,function(v){return '+'+v+'%'},function(v){g=v;draw()});buttons(row,'곡선 모양',[[0,'바깥으로 볼록(기회비용 체증)'],[1,'직선(일정)']],lin,function(v){lin=v;draw()});
  function F(xx,s){var R=100*s;return lin?Math.max(0,R-xx):Math.sqrt(Math.max(0,R*R-xx*xx))}
  function draw(){var s=1+g/100,xm=Math.min(x,100*s),y=F(xm,1)*e,yf=F(xm,s),oc=F(xm,s)-F(Math.min(xm+10,100*s),s);
    var P=plot(c,280,{xlo:0,xhi:135,ylo:0,yhi:135,xl:'컴퓨터',yl:'자동차',title:'파랑 생산가능곡선 · 초록 성장 후 · 점 = 지금 생산'});
    P.fn(function(q){return F(q,1)},COL.s,2.4,null,0,100);if(g)P.fn(function(q){return F(q,s)},COL.g,2,[5,4],0,100*s);
    P.dot(xm,y,e<1?COL.r:COL.g,6,e<1?'비효율 A':'효율 B');stamp(P.ctx,P.W,'예시값');
    K([[f1(y,1),'지금 자동차 생산',e<1?'r':'g'],[e<1?'비효율':'효율','곡선 위인가',e<1?'r':'g'],[f1(oc,1)+'대','컴퓨터 10대 더 → 포기할 자동차','a'],[f1(yf-y,1),'성장·효율로 늘릴 수 있는 자동차','i']]);
    E('곡선: 컴퓨터² + 자동차² = (100'+(g?'×'+f1(s,2):'')+')² · 기회비용 = 곡선 기울기 크기 = 컴퓨터 ÷ 자동차 = <i>'+(lin?'1 (일정)':f1(xm/Math.max(1e-9,F(xm,s)),2))+'</i>');
    I([[e<1?'r':'g',e<1?'곡선 안쪽(A)에서는 아무것도 포기하지 않고 둘 다 늘릴 수 있어요. 자원을 놀리고 있다는 뜻이에요.':'곡선 위(B)에서는 하나를 늘리려면 다른 것을 줄여야 해요. 이것이 상충관계(trade-off)예요.'],['a',lin?'직선이면 컴퓨터를 몇 대 만들든 기회비용이 같아요.':'컴퓨터를 많이 만들수록 10대를 더 만들 때 포기하는 자동차가 커져요. 자동차에 더 알맞은 자원까지 끌어오기 때문이에요(기회비용 체증).']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* 실증 · 규범 / 미시 · 거시 분류 게임 */
SIMS.posnorm=function(el,cfg){var box=h('div',{class:'stack',style:'gap:10px'});el.appendChild(box);var K=kpis(el,4),I=insight(el);
  var Q=[['최저임금이 오르면 10대 고용이 줄어든다.','실증','미시'],['정부는 최저임금을 올려야 한다.','규범','미시'],['통화량이 지나치게 늘면 물가가 오른다.','실증','거시'],['정년은 60세로 의무화하는 것이 바람직하다.','규범','거시'],['라면 값이 오르면 라면 판매량이 줄어든다.','실증','미시'],['고소득자 세율이 저소득자보다 높아야 한다.','규범','거시']],ans={},m={};
  Q.forEach(function(q,i){var d=h('div',{class:'panel',style:'padding:10px 14px'});d.innerHTML='<p style="margin:0 0 6px"><b>'+(i+1)+'.</b> '+q[0]+'</p>';var r=ctrlRow(d);
    buttons(r,'',[['실증','실증(있는 사실)'],['규범','규범(바람직한가)']],null,function(v){ans[i]=v;draw()});buttons(r,'',[['미시','미시'],['거시','거시']],null,function(v){m[i]=v;draw()});box.appendChild(d)});
  function draw(){var a=0,b=0,n=0;Q.forEach(function(q,i){if(ans[i]){n++;if(ans[i]===q[1])a++}if(m[i]&&m[i]===q[2])b++});
    K([[a+'/'+Q.length,'실증·규범 맞힘','g'],[b+'/'+Q.length,'미시·거시 맞힘','i'],[n+'/'+Q.length,'고른 문장','m'],[a===Q.length&&b===Q.length?'만점':'진행 중','상태','a']]);
    I([['i','"~이다/~한다"처럼 확인할 수 있는 사실은 실증, "~해야 한다/바람직하다"처럼 가치판단이 들어가면 규범이에요.'],['a','정년 연장처럼 같은 사실을 보고도 견해가 갈리는 건, 과학적 판단이 달라서이거나 가치관이 달라서예요.']])}
  draw()};

/* ===== CH03 수요와 공급 (음반 시장: Qd = 9 − 2P, Qs = 1 + 2P, P는 만 원) ===== */
SIMS.demandsh=function(el,cfg){var c=S0(el,cfg,270,'수요량의 변화와 수요의 변화'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var p=2,inc=0,typ=0,sub=0,com=0,pref=0;
  S(row,'이 재화 가격 P(만 원)',.5,4,.25,p,fx(2),function(v){p=v;draw()});S(row,'소득 변화',-2,2,.5,inc,function(v){return (v>0?'+':'')+v},function(v){inc=v;draw()});
  buttons(row,'재화 성격',[[0,'정상재'],[1,'열등재']],typ,function(v){typ=v;draw()});S(row,'대체재(MP3) 가격 변화',-2,2,.5,sub,function(v){return (v>0?'+':'')+v},function(v){sub=v;draw()});
  S(row,'보완재(재생기) 가격 변화',-2,2,.5,com,function(v){return (v>0?'+':'')+v},function(v){com=v;draw()});S(row,'선호 변화',-2,2,.5,pref,function(v){return (v>0?'+':'')+v},function(v){pref=v;draw()});
  function draw(){var sh=(typ?-1:1)*inc+sub-com+pref,a=9+sh,q0=9-2*p,q=Math.max(0,a-2*p);
    var P=plot(c,270,{xlo:0,xhi:14,ylo:0,yhi:6,xl:'수요량 Q',yl:'가격 P(만 원)',title:'회색 처음 수요 · 파랑 지금 수요'});
    P.fn(function(Q){return (9-Q)/2},COL.muted,1.6,[5,4],0,9);P.fn(function(Q){return (a-Q)/2},COL.s,2.4,null,0,Math.max(0,a));P.dot(q,p,COL.s,6,'지금 ('+f1(q,1)+'개)');stamp(P.ctx,P.W,'예시값');
    K([[f1(q,1)+'개','지금 수요량','i'],[(sh>0?'+':'')+f1(sh,1),'수요곡선 이동(개)',sh>0?'g':sh<0?'r':'m'],[sh===0?'곡선 위 이동':'곡선 자체 이동','무엇이 바뀌었나','a'],[sh>0?'오른쪽(증가)':sh<0?'왼쪽(감소)':'없음','수요의 변화','m']]);
    E('Q<sub>d</sub> = 9 − 2P <b>'+(sh?(sh>0?'+ ':'− ')+f1(Math.abs(sh),1):'')+'</b> → P = '+f1(p,2)+'에서 '+f1(q,1)+'개');
    I([['i','이 재화의 가격만 바꾸면 같은 곡선 위를 움직여요(수요량의 변화). 소득·다른 재화 가격·선호가 바뀌면 곡선 자체가 옮겨 가요(수요의 변화).'],[typ?'a':'g',typ?'열등재는 소득이 늘면 수요가 줄어요(라면·대기근 때의 감자). 기펜재는 열등재 가운데 아주 드문 특수한 경우예요.':'정상재는 소득이 늘면 수요가 늘어요. 대체재 값이 오르면 이 재화 수요가 늘고, 보완재 값이 오르면 줄어요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.supplysh=function(el,cfg){var c=S0(el,cfg,270,'공급량의 변화와 공급의 변화'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var p=2,cost=0,tech=0,nf_=0,wx=0;
  S(row,'이 재화 가격 P(만 원)',.5,4,.25,p,fx(2),function(v){p=v;draw()});S(row,'원료·인건비 변화',-2,2,.5,cost,function(v){return (v>0?'+':'')+v},function(v){cost=v;draw()});
  S(row,'기술 수준 변화',-2,2,.5,tech,function(v){return (v>0?'+':'')+v},function(v){tech=v;draw()});S(row,'공급자 수 변화',-2,2,.5,nf_,function(v){return (v>0?'+':'')+v},function(v){nf_=v;draw()});
  buttons(row,'날씨(농산물이라면)',[[0,'보통'],[-1.5,'흉작'],[1.5,'풍작']],wx,function(v){wx=v;draw()});
  function draw(){var sh=-cost+tech+nf_+wx,a=1+sh,q=Math.max(0,a+2*p);
    var P=plot(c,270,{xlo:0,xhi:14,ylo:0,yhi:6,xl:'공급량 Q',yl:'가격 P(만 원)',title:'회색 처음 공급 · 빨강 지금 공급'});
    P.fn(function(Q){return (Q-1)/2},COL.muted,1.6,[5,4],1,13);P.fn(function(Q){return (Q-a)/2},COL.r,2.4,null,Math.max(0,a),14);P.dot(q,p,COL.r,6,'지금 ('+f1(q,1)+'개)');stamp(P.ctx,P.W,'예시값');
    K([[f1(q,1)+'개','지금 공급량','i'],[(sh>0?'+':'')+f1(sh,1),'공급곡선 이동(개)',sh>0?'g':sh<0?'r':'m'],[sh===0?'곡선 위 이동':'곡선 자체 이동','무엇이 바뀌었나','a'],[sh>0?'오른쪽(증가)':sh<0?'왼쪽(감소)':'없음','공급의 변화','m']]);
    E('Q<sub>s</sub> = 1 + 2P <b>'+(sh?(sh>0?'+ ':'− ')+f1(Math.abs(sh),1):'')+'</b> → P = '+f1(p,2)+'에서 '+f1(q,1)+'개');
    I([['i','공급곡선이 오른쪽 위로 올라가는 이유: 가격이 오르면 ① 기존 기업이 더 만들고 ② 새 기업이 들어와요.'],['a','원료 값이 오르거나 흉작이면 같은 가격에서 덜 내놓아요(왼쪽 이동). 기술이 좋아지거나 공급자가 늘면 오른쪽으로 옮겨 가요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.equil=function(el,cfg){var c=S0(el,cfg,280,'초과수요·초과공급과 균형의 이동'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var p=cfg.p||3,dD=cfg.dD||0,dS=0;
  S(row,'지금 가격 P(만 원)',.5,4,.25,p,fx(2),function(v){p=v;draw()});S(row,'수요 이동(개)',-4,4,1,dD,function(v){return (v>0?'+':'')+v},function(v){dD=v;draw()});S(row,'공급 이동(개)',-4,4,1,dS,function(v){return (v>0?'+':'')+v},function(v){dS=v;draw()});
  action(row,'MP3 값 하락(수요 −4)',function(){dD=-4;draw()});action(row,'가격을 균형으로',function(){p=(8+dD-dS)/4;draw()},true);
  function draw(){var Ps=(8+dD-dS)/4,Qs_=9+dD-2*Ps,qd=Math.max(0,9+dD-2*p),qs=Math.max(0,1+dS+2*p),gap=qd-qs;
    var P=plot(c,280,{xlo:0,xhi:14,ylo:0,yhi:6,xl:'수량',yl:'가격 P(만 원)',title:'파랑 수요 · 빨강 공급 · 주황 지금 가격'});
    P.fn(function(Q){return (9+dD-Q)/2},COL.s,2.4,null,0,9+dD);P.fn(function(Q){return (Q-1-dS)/2},COL.r,2.4,null,Math.max(0,1+dS),14);P.seg(0,p,14,p,COL.a,1.5,[4,3]);
    if(Math.abs(gap)>1e-9){P.seg(qd,p,qs,p,gap>0?COL.r:COL.i,4)}P.dot(Qs_,Ps,COL.g,6,'균형 E');stamp(P.ctx,P.W,'예시값');
    K([[f1(Ps,2)+'만 원','균형가격','g'],[f1(Qs_,1)+'개','균형거래량','g'],[f1(qd,1)+' / '+f1(qs,1),'지금 수요량 / 공급량','i'],[gap>0?'초과수요 '+f1(gap,1):gap<0?'초과공급 '+f1(-gap,1):'균형','지금 상태',gap>0?'r':gap<0?'a':'g']]);
    E('Q<sub>d</sub> = Q<sub>s</sub>: 9 '+(dD?(dD>0?'+ ':'− ')+Math.abs(dD):'')+' − 2P = 1 '+(dS?(dS>0?'+ ':'− ')+Math.abs(dS):'')+' + 2P → P* = <i>'+f1(Ps,2)+'</i>, Q* = '+f1(Qs_,1));
    I([[gap>0?'r':gap<0?'a':'g',gap>0?'사려는 양이 더 많아요(초과수요). 더 내고라도 사려는 사람이 생겨 가격이 올라가요.':gap<0?'팔려는 양이 더 많아요(초과공급). 더 싸게라도 팔려는 사람이 생겨 가격이 내려가요.':'사려는 양 = 팔려는 양. 다른 충격이 없으면 이 상태가 유지돼요. 가격이 신호등 역할을 한 결과예요.'],['i','MP3 값이 내려가면(대체재) 음반 수요가 4개 줄어 균형이 2만 원·5개 → 1만 원·3개로 옮겨 가요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH04 탄력성 ===== */
SIMS.elas=function(el,cfg){var c=S0(el,cfg,250,'점 탄력성과 중간점(호) 탄력성'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var p1=500,p2=1000,q1=100,q2=80;
  S(row,'처음 가격(원)',100,2000,50,p1,null,function(v){p1=v;draw()});S(row,'바뀐 가격(원)',100,2000,50,p2,null,function(v){p2=v;draw()});
  S(row,'처음 수요량(개)',10,200,5,q1,null,function(v){q1=v;draw()});S(row,'바뀐 수요량(개)',10,200,5,q2,null,function(v){q2=v;draw()});
  function draw(){var dp=(p2-p1)/p1,dq=(q2-q1)/q1,e=dp?Math.abs(dq/dp):0,dpm=(p2-p1)/((p1+p2)/2),dqm=(q2-q1)/((q1+q2)/2),em=dpm?Math.abs(dqm/dpm):0;
    var P=plot(c,250,{xlo:0,xhi:220,ylo:0,yhi:2100,xl:'수요량',yl:'가격(원)',title:'두 점 A(처음)와 B(바뀐 뒤)'});
    P.seg(q1,p1,q2,p2,COL.s,2.4);P.dot(q1,p1,COL.s,6,'A');P.dot(q2,p2,COL.g,6,'B');stamp(P.ctx,P.W,'예시값');
    K([[pct(dp,1),'가격 변화율','i'],[pct(dq,1),'수요량 변화율','a'],[f1(e,2),'점 탄력성(처음 값 기준)',e>1?'r':'g'],[f1(em,2),'호 탄력성(중간점 기준)',em>1?'r':'g']]);
    E('탄력성 = |수요량 변화율 ÷ 가격 변화율| = |'+pct(dq,1)+' ÷ '+pct(dp,1)+'| = <i>'+f1(e,2)+'</i> · 중간점: |'+pct(dqm,1)+' ÷ '+pct(dpm,1)+'| = '+f1(em,2));
    I([[em>1?'r':'g',em>1?'탄력적(1보다 큼): 가격 변화보다 수요량이 더 크게 반응해요.':em===1?'단위탄력적: 가격과 같은 비율로 반응해요.':'비탄력적(1보다 작음): 가격이 크게 변해도 수요량은 조금만 반응해요.'],['a','처음 값 기준이면 오를 때와 내릴 때 값이 달라져요(500→1000은 +100%, 1000→500은 −50%). 그래서 중간점(평균) 기준 호 탄력성을 씁니다.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.revenue=function(el,cfg){var c=S0(el,cfg,270,'가격과 매출, 그리고 탄력성'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var p=cfg.p||70,ch=10;
  S(row,'지금 가격',5,95,1,p,null,function(v){p=v;draw()});S(row,'가격을 바꿀 폭(%)',-30,30,5,ch,function(v){return (v>0?'+':'')+v+'%'},function(v){ch=v;draw()});
  function draw(){var q=100-p,e=p/q,p2=p*(1+ch/100),q2=Math.max(0,100-p2),R=p*q,R2=p2*q2;
    var P=plot(c,270,{xlo:0,xhi:100,ylo:0,yhi:100,xl:'수량 Q',yl:'가격 P',title:'수요 Q = 100 − P · 초록 사각형 = 매출 P × Q'});
    P.poly([[0,0],[q,0],[q,p],[0,p]],COL.g,.18);P.poly([[0,0],[q2,0],[q2,p2],[0,p2]],COL.a,.15);P.fn(function(Q){return 100-Q},COL.s,2.4);
    P.dot(q,p,COL.g,6,'지금');P.dot(q2,p2,COL.a,5,'바꾼 뒤',8,16);P.lab('탄력적(위쪽)',4,92,COL.r);P.lab('비탄력적(아래쪽)',62,10,COL.i);stamp(P.ctx,P.W,'예시값');
    K([[f1(e,2),'지금 가격탄력성 = P ÷ Q',e>1?'r':'i'],[nf(R),'지금 매출','g'],[nf(R2),'가격 '+(ch>0?'+':'')+ch+'% 뒤 매출',R2>R?'g':'r'],[(R2>=R?'+':'')+nf(R2-R),'매출 변화',R2>=R?'g':'r']]);
    E('직선 수요에서 탄력성 = (ΔQ/ΔP)·(P/Q) = 1 × '+p+' ÷ '+q+' = <i>'+f1(e,2)+'</i> → 탄력성 1인 P = 50에서 매출이 가장 커요');
    I([[e>1?'r':'i',e>1?'탄력적인 구간이에요. 값을 올리면 손님이 더 크게 줄어 매출이 줄고, 내리면 매출이 늘어요.':'비탄력적인 구간이에요. 값을 올려도 손님이 조금만 줄어 매출이 늘어요(우유처럼 대체재가 적은 재화).'],['a','같은 직선 수요라도 위치에 따라 탄력성이 달라요. 기울기와 탄력성은 다른 말이에요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.elasmap=function(el,cfg){var c=S0(el,cfg,250,'소득·교차·공급 탄력성'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var di=8,dx=6,cs=0;
  S(row,'소득 +10%일 때 수요량 변화(%)',-10,25,1,di,function(v){return (v>0?'+':'')+v+'%'},function(v){di=v;draw()});
  S(row,'다른 재화 값 +10%일 때 수요량 변화(%)',-15,15,1,dx,function(v){return (v>0?'+':'')+v+'%'},function(v){dx=v;draw()});
  S(row,'공급곡선 절편 c (Q = c + 2P)',-10,10,1,cs,null,function(v){cs=v;draw()});
  function draw(){var ei=di/10,ex=dx/10;
    var P=plot(c,250,{xlo:0,xhi:10,ylo:0,yhi:3.2,xl:'가격 P',yl:'공급탄력성',title:'공급 Q = c + 2P에서 가격별 공급탄력성'});
    P.fn(function(p){var q=cs+2*p;return q>0?2*p/q:NaN},COL.r,2.4,null,.1,10);P.seg(0,1,10,1,COL.muted,1,[4,4]);P.lab('탄력성 1',.2,1.12,COL.muted);stamp(P.ctx,P.W,'예시값');
    K([[f1(ei,2),'소득탄력성',ei<0?'r':'g'],[ei<0?'열등재':ei>1?'정상재·사치재':'정상재·필수재','재화 구분','m'],[f1(ex,2),'교차탄력성',ex>0?'i':ex<0?'a':'m'],[ex>0?'대체재':ex<0?'보완재':'관계 없음','두 재화 관계','a']]);
    E('소득탄력성 = '+di+'% ÷ 10% = <i>'+f1(ei,2)+'</i> · 교차탄력성 = '+dx+'% ÷ 10% = <i>'+f1(ex,2)+'</i> · 공급탄력성 = 2P ÷ (c + 2P)');
    I([['i','교차탄력성의 기준은 1이 아니라 0이에요. 0보다 크면 대체재(버스↔자가용), 0보다 작으면 보완재(프린터↔잉크)예요.'],[cs===0?'g':'a',cs===0?'원점을 지나는 직선 공급(c = 0)은 어느 가격에서나 탄력성이 1로 일정해요.':'원점을 지나지 않는 직선 공급은 가격마다 탄력성이 달라요. c를 0으로 맞춰 보세요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH05 정부정책 ===== */
SIMS.ceiling=function(el,cfg){var c=S0(el,cfg,280,'가격상한제: 초과수요와 암시장'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var pc=cfg.pc||1,lr=0;
  S(row,'가격 상한(만 원)',.5,4,.25,pc,fx(2),function(v){pc=v;draw()});buttons(row,'기간',[[0,'단기(반응 작음)'],[1,'장기(반응 큼)']],lr,function(v){lr=v;draw()});
  function draw(){var k=lr?2:1,a=lr?13:9,b=lr?-3:1,Pe=(a-b)/(4*k)*2/2;Pe=(a-b)/(4*k);var Qe=a-2*k*Pe;
    var qd=Math.max(0,a-2*k*Math.min(pc,Pe)),qs=Math.max(0,b+2*k*Math.min(pc,Pe)),bind=pc<Pe,trade=Math.min(qd,qs),pb=(a-trade)/(2*k);
    var P=plot(c,280,{xlo:0,xhi:16,ylo:0,yhi:6,xl:'수량(집·음반)',yl:'가격(만 원)',title:'파랑 수요 · 빨강 공급 · 주황 상한선'+(lr?' (장기: 완만)':' (단기: 가파름)')});
    P.fn(function(Q){return (a-Q)/(2*k)},COL.s,2.4,null,0,a);P.fn(function(Q){return (Q-b)/(2*k)},COL.r,2.4,null,Math.max(0,b),16);P.seg(0,pc,16,pc,COL.a,2,[5,4]);
    if(bind){P.seg(qs,pc,qd,pc,COL.r,5);P.dot(trade,pb,COL.m,5,'암시장 가격',8,-8)}P.dot(Qe,Pe,COL.g,5,'균형',8,16);stamp(P.ctx,P.W,'예시값');
    K([[bind?'실효 있음':'실효 없음','상한선이 균형보다 낮은가',bind?'r':'g'],[f1(trade,1),'실제 거래량','i'],[bind?f1(qd-qs,1):'0','부족한 양(초과수요)',bind?'r':'g'],[bind?f1(pb,2)+'만 원':'-','3개를 놓고 사려는 사람의 최대 지불가격','m']]);
    E('균형 P* = '+f1(Pe,2)+' · 상한 '+f1(pc,2)+'에서 수요량 '+f1(qd,1)+' − 공급량 '+f1(qs,1)+' = 부족 <i>'+f1(Math.max(0,qd-qs),1)+'</i>');
    I([[bind?'r':'g',bind?'상한선이 균형보다 낮아 모자람이 생겨요. 가격 대신 줄서기·추첨(할당)으로 나누고, 몰래 더 비싸게 파는 암시장이 생기기 쉬워요.':'상한선이 균형보다 높으면 시장가격이 이미 그 아래라 아무 효과가 없어요.'],['a','장기 버튼을 눌러 보세요. 시간이 지나면 수요·공급이 더 크게 반응해 임대주택 부족이 커져요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.floor=function(el,cfg){var c=S0(el,cfg,280,'가격하한제: 최저임금과 실업'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var wf=cfg.wf||1.2,el_=1;
  S(row,'최저임금(균형 = 1)',.6,1.6,.05,wf,fx(2),function(v){wf=v;draw()});S(row,'노동수요의 탄력성',.4,2,.2,el_,fx(1),function(v){el_=v;draw()});
  function draw(){var Ld=function(w){return 100-50*el_*(w-1)},Ls=function(w){return 100+50*(w-1)},bind=wf>1,w=bind?wf:1,emp=Math.min(Ld(w),Ls(w)),un=bind?Ls(w)-Ld(w):0,inc=emp*w;
    var P=plot(c,280,{xlo:0,xhi:160,ylo:.5,yhi:1.7,xl:'노동자 수',yl:'임금',title:'파랑 노동수요(기업) · 빨강 노동공급(노동자) · 주황 최저임금',fy:function(v){return v.toFixed(1)}});
    P.fn(function(L){return 1+(100-L)/(50*el_)},COL.s,2.4,null,0,160);P.fn(function(L){return 1+(L-100)/50},COL.r,2.4,null,40,160);P.seg(0,wf,160,wf,COL.a,2,[5,4]);
    if(bind)P.seg(Ld(w),w,Ls(w),w,COL.r,5);P.dot(100,1,COL.g,5,'균형',8,16);stamp(P.ctx,P.W,'설명용 모형');
    K([[f1(emp,0)+'명','일자리를 가진 사람','i'],[f1(un,0)+'명','일하고 싶지만 못 구한 사람(실업)',un>0?'r':'g'],[f1(inc,1),'노동자 전체 임금소득(균형 = 100)',inc>=100?'g':'r'],[bind?'실효 있음':'실효 없음','하한선이 균형보다 높은가','m']]);
    E('하한 '+f1(wf,2)+'에서 노동공급 '+f1(Ls(w),0)+' − 노동수요 '+f1(Ld(w),0)+' = 초과공급(실업) <i>'+f1(un,0)+'</i>명');
    I([[bind?'r':'g',bind?'최저임금이 균형보다 높으면 일하려는 사람은 늘고 기업이 쓰려는 사람은 줄어요. 그 차이가 실업이에요.':'하한선이 균형보다 낮으면 효과가 없어요.'],['a','노동수요가 덜 탄력적이면 실업이 작고 노동자 전체 소득은 늘 수 있어요. 반대로 탄력적이면 소득 합도 줄 수 있어요. 효과는 탄력성이 좌우해요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* 아이스크림 세금: 균형 3달러·100개, 구매자 반응 100/3, 판매자 반응 50 */
SIMS.icetax=function(el,cfg){var c=S0(el,cfg,280,'아이스크림 1개당 세금: 누가 실제로 부담하나'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var t=.5,kd=100/3,ks=50,payer=0;
  S(row,'1개당 세금(달러)',0,1.5,.05,t,fx(2),function(v){t=v;draw()});S(row,'구매자 반응(가격 1달러당 줄이는 개수)',5,150,5,Math.round(kd),null,function(v){kd=v;draw()});
  S(row,'판매자 반응(가격 1달러당 줄이는 개수)',5,150,5,ks,null,function(v){ks=v;draw()});buttons(row,'고지서 받는 쪽',[[0,'판매자'],[1,'구매자']],payer,function(v){payer=v;draw()});
  function draw(){var x=t*ks/(kd+ks),y=t-x,Pb=3+x,Ps=3-y,Q=100-kd*x;
    var P=plot(c,280,{xlo:40,xhi:140,ylo:1.5,yhi:4.5,xl:'아이스크림(개)',yl:'가격($)',title:'파랑 수요 · 빨강 공급 · 점선 = 세금만큼 옮긴 곡선',fy:function(v){return v.toFixed(1)}});
    P.fn(function(q){return 3+(100-q)/kd},COL.s,2.4);P.fn(function(q){return 3+(q-100)/ks},COL.r,2.4);
    if(payer)P.fn(function(q){return 3+(100-q)/kd-t},COL.s,1.4,[5,4]);else P.fn(function(q){return 3+(q-100)/ks+t},COL.r,1.4,[5,4]);
    P.poly([[40,Pb],[Q,Pb],[Q,Ps],[40,Ps]],COL.g,.18);P.dot(100,3,COL.muted,5,'세전 $3·100개');P.dot(Q,Pb,COL.s,5,'구매자 $'+Pb.toFixed(2));P.dot(Q,Ps,COL.r,5,'판매자 $'+Ps.toFixed(2),8,16);stamp(P.ctx,P.W,'예시값');
    K([['$'+Pb.toFixed(2),'구매자가 내는 가격','i'],['$'+Ps.toFixed(2),'판매자가 받는 가격','r'],[f1(Q,1)+'개','거래량','m'],[Math.round(x/Math.max(t,1e-9)*100)+'% / '+Math.round(y/Math.max(t,1e-9)*100)+'%','부담: 구매자 / 판매자','a']]);
    E('구매자 몫 = 판매자 반응 ÷ (구매자 반응 + 판매자 반응) = '+Math.round(ks)+' ÷ '+Math.round(kd+ks)+' = <i>'+Math.round(ks/(kd+ks)*100)+'%</i>');
    I([['g','고지서를 누가 받든 결과가 같아요. 세금 $0.5는 구매자 $0.30, 판매자 $0.20처럼 나뉘어요(법적 귀착 ≠ 경제적 귀착).'],['a','가격에 덜 반응하는(비탄력적인) 쪽이 더 많이 부담해요. 구매자 반응을 줄여 보세요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH06 잉여 ===== */
SIMS.cs=function(el,cfg){var c=S0(el,cfg,270,'지불용의와 소비자잉여'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var W=[['존',100],['폴',80],['조지',70],['링고',50]],n=1,p=80,mode=0;
  buttons(row,'정하는 방법',[[0,'음반 장수로 경매'],[1,'가격을 직접']],mode,function(v){mode=v;draw()});S(row,'음반 장수(경매)',1,4,1,n,null,function(v){n=v;draw()});S(row,'가격 직접(달러)',0,110,5,p,null,function(v){p=v;draw()});
  function draw(){var pr=mode?p:(n<4?W[n][1]:0),buy=W.filter(function(w){return w[1]>=pr&&(mode||W.indexOf(w)<n)}),cs=buy.reduce(function(s,w){return s+w[1]-pr},0);
    var P=plot(c,270,{xlo:0,xhi:4.5,ylo:0,yhi:120,xl:'음반 수량',yl:'달러',title:'계단 = 수요곡선(지불용의) · 초록 = 소비자잉여'});
    W.forEach(function(w,i){P.seg(i,w[1],i+1,w[1],COL.s,2.4);if(i<3)P.seg(i+1,w[1],i+1,W[i+1][1],COL.s,1.2);P.lab(w[0]+' '+w[1],i+.1,w[1]+5,COL.s);
      if(buy.indexOf(w)>=0)P.poly([[i,pr],[i+1,pr],[i+1,w[1]],[i,w[1]]],COL.g,.25)});
    P.seg(0,pr,4.5,pr,COL.a,2,[5,4]);stamp(P.ctx,P.W,'예시값');
    K([['$'+pr,'가격'+(mode?'':' (탈락자의 지불용의 바로 위)'),'a'],[buy.length+'장','사는 사람 수','i'],['$'+cs,'소비자잉여 합','g'],[buy.map(function(w){return w[0]+' '+(w[1]-pr)}).join(' · ')||'-','사람별 잉여','m']]);
    E('소비자잉여 = 지불용의 − 실제 낸 값 → 합 = <i>$'+cs+'</i> (수요곡선 아래 · 가격선 위 면적)');
    I([['g','음반 1장이면 폴이 포기하는 80달러에서 경매가 끝나 존이 20달러 이득을 봐요. 2장이면 70달러에 존 30 + 폴 10 = 40달러예요.'],['i','가격이 내리면 잉여가 커지는 길이 두 가지예요. 원래 사던 사람이 덜 내고(사각형), 새로 사는 사람이 생겨요(삼각형).']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.ps=function(el,cfg){var c=S0(el,cfg,270,'공급용의와 생산자잉여'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var C=[['그랜마',500],['조지아',600],['프리다',800],['메리',900]],n=1,p=600,mode=0;
  buttons(row,'정하는 방법',[[0,'칠할 집 수로 견적 경쟁'],[1,'가격을 직접']],mode,function(v){mode=v;draw()});S(row,'칠할 집(채)',1,4,1,n,null,function(v){n=v;draw()});S(row,'가격 직접(달러)',300,1000,50,p,null,function(v){p=v;draw()});
  function draw(){var pr=mode?p:(n<4?C[n][1]:1000),sell=C.filter(function(w,i){return w[1]<=pr&&(mode||i<n)}),ps=sell.reduce(function(s,w){return s+pr-w[1]},0);
    var P=plot(c,270,{xlo:0,xhi:4.5,ylo:0,yhi:1100,xl:'칠한 집 수',yl:'달러',title:'계단 = 공급곡선(공급용의 = 비용) · 초록 = 생산자잉여'});
    C.forEach(function(w,i){P.seg(i,w[1],i+1,w[1],COL.r,2.4);if(i<3)P.seg(i+1,w[1],i+1,C[i+1][1],COL.r,1.2);P.lab(w[0]+' '+w[1],i+.05,w[1]-30,COL.r);
      if(sell.indexOf(w)>=0)P.poly([[i,w[1]],[i+1,w[1]],[i+1,pr],[i,pr]],COL.g,.25)});
    P.seg(0,pr,4.5,pr,COL.a,2,[5,4]);stamp(P.ctx,P.W,'예시값');
    K([['$'+pr,'가격'+(mode?'':' (탈락자의 비용 바로 아래)'),'a'],[sell.length+'명','일하는 사람 수','i'],['$'+ps,'생산자잉여 합','g'],[sell.map(function(w){return w[0]+' '+(pr-w[1])}).join(' · ')||'-','사람별 잉여','m']]);
    E('생산자잉여 = 받은 값 − 공급용의(비용) → 합 = <i>$'+ps+'</i> (가격선 아래 · 공급곡선 위 면적)');
    I([['g','집 1채면 조지아의 600달러 바로 아래에서 견적 경쟁이 끝나 그랜마가 100달러 이득이에요. 2채면 800달러에 조지아 200 + 그랜마 300 = 500달러예요.'],['i','비용이 가장 싼 사람부터 일을 맡게 돼요. 시장이 생산비가 가장 싼 공급자에게 일을 나눠 주는 방식이에요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH07 조세의 비용 (P = 100 − Q, P = 20 + Q) ===== */
SIMS.taxtable=function(el,cfg){var c=S0(el,cfg,270,'세금 전후의 잉여 표'),row=rows(el),K=kpis(el,4),tb=h('div',{class:'tw'});el.appendChild(tb);var I=insight(el);
  var t=20;S(row,'1단위당 세금',0,80,2,t,null,function(v){t=v;draw()});
  function draw(){var Q=(80-t)/2,Pb=100-Q,Ps=20+Q,A=(100-Pb)*Q/2,B=(Pb-60)*Q,Cc=(Pb-60)*(40-Q)/2,D=(60-Ps)*Q,Ee=(60-Ps)*(40-Q)/2,F=(Ps-20)*Q/2;
    var P=plot(c,270,{xlo:0,xhi:80,ylo:0,yhi:100,xl:'수량',yl:'가격',title:'A 소비자 · B·D 세수 · C·E 사중손실 · F 생산자'});
    P.poly([[0,100],[0,Pb],[Q,Pb]],COL.s,.18);P.poly([[0,Pb],[Q,Pb],[Q,60],[0,60]],COL.g,.25);P.poly([[0,60],[Q,60],[Q,Ps],[0,Ps]],COL.g,.4);P.poly([[Q,Pb],[40,60],[Q,60]],COL.a,.35);P.poly([[Q,60],[40,60],[Q,Ps]],COL.r,.3);P.poly([[0,20],[0,Ps],[Q,Ps]],COL.r,.15);
    P.seg(0,100,80,20,COL.s,2.2);P.seg(0,20,80,100,COL.r,2.2);P.lab('A',Q*.25,Pb+(100-Pb)*.3,COL.s,'left',true);P.lab('B',Q*.45,(Pb+60)/2,COL.g,'left',true);P.lab('C',Q+(40-Q)*.25,(Pb+60)/2+1,COL.a,'left',true);P.lab('D',Q*.45,(60+Ps)/2,COL.g,'left',true);P.lab('E',Q+(40-Q)*.25,(60+Ps)/2-3,COL.r,'left',true);P.lab('F',Q*.25,Ps-(Ps-20)*.4,COL.r,'left',true);stamp(P.ctx,P.W,'예시값');
    function r(a,b,cc,d){return '<tr><td>'+a+'</td><td>'+b+'</td><td>'+cc+'</td><td>'+d+'</td></tr>'}
    tb.innerHTML='<table class="tb"><tr><th></th><th>세금 전</th><th>세금 뒤</th><th>변화</th></tr>'+r('소비자잉여','A+B+C = '+f1(A+B+Cc,0),'A = '+f1(A,0),'−(B+C) = −'+f1(B+Cc,0))+r('생산자잉여','D+E+F = '+f1(D+Ee+F,0),'F = '+f1(F,0),'−(D+E) = −'+f1(D+Ee,0))+r('세수','0','B+D = '+f1(B+D,0),'+'+f1(B+D,0))+r('총잉여',f1(A+B+Cc+D+Ee+F,0),f1(A+B+D+F,0),'<b>−(C+E) = −'+f1(Cc+Ee,0)+'</b>')+'</table>';
    K([[f1(Q,0),'세금 뒤 거래량(세전 40)','i'],[f1(B+D,0),'세수 B + D','g'],[f1(Cc+Ee,0),'사중손실 C + E','r'],[f1((Cc+Ee)/Math.max(1,B+D)*100,0)+'%','세수 1원당 사중손실','a']]);
    I([['r','소비자와 생산자가 잃은 것(B+C+D+E)이 정부가 얻은 것(B+D)보다 커요. 그 차이 C+E가 아무도 갖지 못하고 사라진 몫, 사중손실이에요.'],['i','사라진 이유는 거래가 줄었기 때문이에요. 세금이 사는 값과 받는 값 사이에 쐐기를 박아 서로 이득이던 거래까지 막아요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.laffer=function(el,cfg){var c=S0(el,cfg,260,'세금 크기에 따른 세수와 사중손실'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var t=20;S(row,'1단위당 세금',0,80,2,t,null,function(v){t=v;draw()});
  function Rv(x){return x*(80-x)/2}function DL(x){return x*x/4}
  function draw(){var P=plot(c,260,{xlo:0,xhi:80,ylo:0,yhi:1700,xl:'세금 크기',yl:'금액',title:'초록 세수(래퍼 곡선) · 빨강 사중손실'});
    P.fn(Rv,COL.g,2.4);P.fn(DL,COL.r,2.4);P.seg(t,0,t,1700,COL.a,1.5,[3,3]);P.dot(t,Rv(t),COL.g,5,'세수');P.dot(t,DL(t),COL.r,5,'사중손실',8,16);P.dot(40,800,COL.muted,4,'세수 최대',8,-8);stamp(P.ctx,P.W,'예시값');
    K([[f1(Rv(t),0),'세수 t × Q','g'],[f1(DL(t),0),'사중손실 ≈ t² ÷ 4','r'],[t?f1(DL(t)/Math.max(1,Rv(t)),2):'0','세수 1원당 손실','a'],[t<40?'세금↑ → 세수↑':t>40?'세금↑ → 세수↓':'꼭대기','지금 구간','i']]);
    E('Q = (80 − t) ÷ 2 · 세수 = t·Q = <i>'+f1(Rv(t),0)+'</i> · 사중손실 = t·(40 − Q) ÷ 2 = t² ÷ 4 = <i>'+f1(DL(t),0)+'</i>');
    I([['r','세금을 두 배로 하면 사중손실은 네 배가 돼요(제곱에 비례). 손실이 세금보다 훨씬 빨리 커져요.'],['a','세금이 40을 넘으면 거래가 너무 줄어 세금을 올려도 세수가 오히려 줄어요. 80이면 거래도 세수도 0이에요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH08 시장구조 ===== */
SIMS.structure=function(el,cfg){var c=S0(el,cfg,240,'시장구조 판정과 개별 기업이 보는 수요'),row=rows(el),K=kpis(el,4),I=insight(el);
  var n=100,dif=0,bar=0,pi=4;
  S(row,'기업 수',1,200,1,n,null,function(v){n=v;draw()});buttons(row,'제품',[[0,'똑같음(동질)'],[1,'조금씩 다름(차별화)']],dif,function(v){dif=v;draw()});buttons(row,'진입장벽',[[0,'낮음'],[1,'높음']],bar,function(v){bar=v;draw()});
  S(row,'내 가게 가격($, 시장가격 4)',3,5,.1,pi,fx(1),function(v){pi=v;draw()});
  function kind(){if(n===1)return '독점';if(n<=5||bar)return dif?'차별적 과점':'과점';return dif?'독점적 경쟁':'완전경쟁'}
  function draw(){var k=kind(),pt=k==='완전경쟁',sales=pt?(pi>4.001?0:pi<3.999?1000:100):Math.max(0,100-40*(pi-4)*(k==='독점'?.6:1));
    var P=plot(c,240,{xlo:0,xhi:1000,ylo:3,yhi:5,xl:'내 가게 판매량',yl:'가격($)',title:pt?'완전경쟁: 개별 기업의 수요는 $4에서 수평':'가격을 올려도 손님이 다 떠나지는 않음(우하향)',fy:function(v){return v.toFixed(1)}});
    if(pt)P.seg(0,4,1000,4,COL.s,2.4);else P.fn(function(q){return 4+(100-q)/(40*(k==='독점'?.6:1))},COL.s,2.4);P.dot(Math.min(sales,1000),pi,COL.a,6,'내 가격');stamp(P.ctx,P.W,'예시값');
    K([[k,'시장구조','m'],[pt?'가격수용자':'가격설정자','기업의 성격','i'],[f1(sales,0)+'개','내 가게 판매량',sales>0?'g':'r'],[k==='완전경쟁'?'농산물·주식':k==='독점'?'운영체제·상수도':k.indexOf('과점')>=0?'이동통신·자동차':'음식점·미용실','예','a']]);
    I([[pt?'r':'i',pt?'완전경쟁에서는 $0.1만 비싸도 손님이 0이 돼요. 시장이 정한 가격을 그대로 받아들이는 가격수용자예요.':'다른 곳과 다르거나 경쟁자가 적으면 가격을 올려도 손님이 조금만 줄어요. 스스로 가격을 정할 힘(시장지배력)이 있어요.'],['a','시장은 기업 수와 제품 차이로 네 가지로 나눠요: 완전경쟁 · 독점적 경쟁 · 과점 · 독점.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* 독점: P = 100 − 7.5Q, MC = 5Q (원자료 수치 재구성: Q=5 이윤 250, Q=8 이윤 160) */
SIMS.monoq=function(el,cfg){var c=S0(el,cfg,280,'독점기업의 생산량 결정: MR = MC'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var q=8;S(row,'생산량 Q',0,13,.5,q,fx(1),function(v){q=v;draw()});
  function Pr(x){return 100-7.5*x}function pi(x){return Pr(x)*x-2.5*x*x}
  function draw(){var P=plot(c,280,{xlo:0,xhi:13.4,ylo:0,yhi:105,xl:'생산량 Q',yl:'가격·비용',title:'파랑 수요(=평균수입) · 보라 한계수입 MR · 빨강 한계비용 MC'});
    P.poly([[5,Pr(5)],[8,40],[5,25]],COL.a,.35);P.fn(Pr,COL.s,2.4);P.fn(function(x){return 100-15*x},COL.m,2,[5,4],0,6.7);P.fn(function(x){return 5*x},COL.r,2.4);
    P.dot(5,62.5,COL.m,6,'독점 Q=5, P=62.5');P.dot(8,40,COL.g,5,'경쟁 Q=8, P=40',8,16);P.seg(q,0,q,105,COL.a,1.5,[3,3]);stamp(P.ctx,P.W,'예시값');
    K([[f1(Pr(q),1),'이 생산량의 가격','i'],[f1(pi(q),1),'독점기업 이윤',Math.abs(q-5)<.01?'g':'a'],[f1(100-15*q,1)+' / '+f1(5*q,1),'MR / MC',100-15*q>5*q?'g':'r'],['56.25','독점의 사중손실(주황)','r']]);
    E('이윤 = (100 − 7.5Q)·Q − 2.5Q² → MR = 100 − 15Q = MC = 5Q → Q = <i>5</i>, 이윤 250 · 경쟁이면 P = MC → Q = 8, 이 기업 이윤 160');
    I([[Math.abs(q-5)<.01?'g':'a',Math.abs(q-5)<.01?'MR = MC인 Q = 5에서 이윤이 가장 커요(250).':'한 개 더 팔 때 들어오는 돈(MR)과 드는 돈(MC)을 비교해 보세요. MR > MC면 늘리고, MR < MC면 줄여요.'],['r','독점은 가격이 MC보다 높은 곳(P > MR = MC)에서 멈춰 경쟁보다 적게 만들어요(5 < 8). 주황 삼각형만큼 사회 전체의 이득이 사라져요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* 과점: 잭과 질의 우물, P = 120 − Q, MC = 0 */
SIMS.oligo=function(el,cfg){var c=S0(el,cfg,250,'두 우물 주인의 생산량과 이윤'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var qj=30,ql=30;S(row,'잭의 생산량(갤런)',0,60,10,qj,null,function(v){qj=v;draw()});S(row,'질의 생산량(갤런)',0,60,10,ql,null,function(v){ql=v;draw()});
  action(row,'담합(30·30)',function(){qj=30;ql=30;draw()});action(row,'잭만 배신(40·30)',function(){qj=40;ql=30;draw()});action(row,'둘 다 40',function(){qj=40;ql=40;draw()},true);
  function draw(){var Q=qj+ql,P=Math.max(0,120-Q),pj=P*qj,pl=P*ql;
    barPlot(c,250,'이윤(달러) — 시장가격 $'+P+', 총생산 '+Q+'갤런',[{v:pj,c:COL.fly,l:'잭',t:nf(pj)},{v:pl,c:COL.robo,l:'질',t:nf(pl)},{v:pj+pl,c:COL.s,l:'둘의 합',t:nf(pj+pl)},{v:3600,c:COL.muted,l:'독점 이윤',t:'3,600'}],3900);
    K([['$'+P,'물값','i'],[Q+'갤런','총생산(독점 60 · 경쟁 120)','m'],[nf(pj)+' / '+nf(pl),'잭 / 질 이윤','a'],[nf(pj+pl),'둘의 이윤 합',pj+pl>=3600?'g':'r']]);
    E('물값 P = 120 − (잭 + 질) · 잭이 10 더 만들면: 산출효과 +P×10, 가격효과 −10×(잭 생산량)');
    I([['a','상대가 30을 지킬 때 내가 40으로 늘리면 1,800 → 2,000으로 이득이에요(우월전략). 하지만 둘 다 그러면 각자 1,600으로 함께 손해예요. 이것이 용의자의 딜레마예요.'],['i','담합(카르텔)은 독점처럼 이윤을 늘리지만, 서로 몰래 늘리려는 유인 때문에 깨지기 쉽고, 법(공정거래법)으로도 금지돼요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH09 시장실패 ===== */
SIMS.freeride=function(el,cfg){var c=S0(el,cfg,250,'공원 짓기: 무임승차'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var n=5,v=30,cost=100,my=20,oth=0;
  S(row,'주민 수',2,10,1,n,null,function(x){n=x;draw()});S(row,'1인당 공원의 가치',5,60,5,v,null,function(x){v=x;draw()});S(row,'내 기부액',0,100,5,my,null,function(x){my=x;draw()});
  buttons(row,'다른 주민',[[0,'모두 무임승차(0원)'],[1,'공평하게 나눠 냄']],oth,function(x){oth=x;draw()});
  function draw(){var each=cost/n,tot=my+(oth?each*(n-1):0),built=tot>=cost,myNet=(built?v:0)-my,soc=n*v;
    barPlot(c,250,'공원 짓는 비용 '+cost+' 대비 모인 돈',[{v:tot,c:built?COL.g:COL.r,l:'모인 돈',t:f1(tot,0)},{v:cost,c:COL.muted,l:'필요한 돈',t:cost},{v:soc,c:COL.s,l:'주민 전체 가치',t:soc},{v:v,c:COL.a,l:'나 혼자의 가치',t:v}],Math.max(soc,cost,tot)*1.15);
    K([[built?'지어짐':'안 지어짐','공원','m'],[f1(myNet,0),'내 순이득(가치 − 기부)',myNet>=0?'g':'r'],[soc>cost?'지어야 함':'안 지어도 됨','사회 전체로 보면',soc>cost?'g':'a'],[f1(each,0),'공평 분담액','i']]);
    E('사회 전체 가치 '+n+' × '+v+' = '+soc+(soc>cost?' > ':' ≤ ')+'비용 '+cost+' · 혼자의 가치 '+v+' < 비용 '+cost);
    I([['r','공원은 돈을 안 낸 사람도 막을 수 없고(비배제성), 내가 써도 남의 몫이 줄지 않아요(비경합성). 그래서 "남이 내겠지"하고 버티는 무임승차가 생겨요.'],['g','모두에게 가치가 비용보다 크면 지어야 하지만 자발적으로는 돈이 덜 모여요. 그래서 정부가 세금으로 공공재를 공급해요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

function lorenz(k,tau){var y=[];for(var i=1;i<=10;i++)y.push(Math.pow(i/10,k));var m=y.reduce(function(a,b){return a+b},0)/10;y=y.map(function(v){return (1-tau)*v+tau*m});var S=y.reduce(function(a,b){return a+b},0),sh=y.map(function(v){return v/S}),cum=[0];sh.forEach(function(s){cum.push(cum[cum.length-1]+s)});
  var B=0;for(var i=1;i<=10;i++)B+=(cum[i]+cum[i-1])/2*.1;return {sh:sh,cum:cum,gini:1-2*B,dec:(sh[0]+sh[1]+sh[2]+sh[3])/(sh[8]+sh[9])}}
SIMS.gini=function(el,cfg){var c=S0(el,cfg,270,'로렌츠 곡선과 지니계수'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var k=2,tau=0;S(row,'소득 격차 정도',0,4,.1,k,fx(1),function(v){k=v;draw()});S(row,'세금·이전으로 재분배(%)',0,60,5,tau*100,function(v){return v+'%'},function(v){tau=v/100;draw()});
  function draw(){var L=lorenz(k,tau),L0=lorenz(k,0);
    var P=plot(c,270,{xlo:0,xhi:1,ylo:0,yhi:1,xl:'인구 누적(가난한 쪽부터)',yl:'소득 누적',title:'회색 완전평등선 · 파랑 재분배 전 · 초록 재분배 후',fx:function(v){return Math.round(v*100)+'%'},fy:function(v){return Math.round(v*100)+'%'}});
    P.seg(0,0,1,1,COL.muted,1.4,[4,4]);var pts=L.cum.map(function(v,i){return [i/10,v]});P.poly([[0,0]].concat(pts).concat([[1,1]]),COL.a,.12);
    for(var i=0;i<10;i++){P.seg(i/10,L0.cum[i],(i+1)/10,L0.cum[i+1],COL.s,2);P.seg(i/10,L.cum[i],(i+1)/10,L.cum[i+1],COL.g,2.4)}stamp(P.ctx,P.W,'설명용 소득분포');
    K([[f1(L0.gini,3),'지니계수(재분배 전)','i'],[f1(L.gini,3),'지니계수(재분배 후)',L.gini<L0.gini?'g':'m'],[f1(L.dec,2),'10분위분배율 (하위40% ÷ 상위20%)','a'],[pct(L.sh[9],1),'상위 10% 소득 몫','r']]);
    E('지니계수 = 평등선과 로렌츠 곡선 사이 면적 ÷ 평등선 아래 삼각형 면적 = <i>'+f1(L.gini,3)+'</i> (0 완전평등 ~ 1 완전불평등)');
    I([['i','지니계수는 0에 가까울수록 평등, 1에 가까울수록 불평등이에요. 10분위분배율은 반대로 2에 가까울수록 평등, 0에 가까울수록 불평등이에요.'],['g','소득에 비례해 걷어 똑같이 나눠 주면 로렌츠 곡선이 평등선 쪽으로 다가가요. 다만 세금이 클수록 일할 유인이 줄 수 있어(효율 vs 형평) 정도를 정하는 건 사회의 선택이에요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH10 국민경제 ===== */
SIMS.gdp=function(el,cfg){var c=S0(el,cfg,250,'명목 GDP와 실질 GDP'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var q1=50,p1=3,q2=10,p2=2;var b={q1:45,p1:2,q2:8,p2:1};
  S(row,'올해 고구마(박스)',30,70,1,q1,null,function(v){q1=v;draw()});S(row,'올해 고구마 값(만 원)',1,5,.5,p1,fx(1),function(v){p1=v;draw()});
  S(row,'올해 두유(박스)',4,20,1,q2,null,function(v){q2=v;draw()});S(row,'올해 두유 값(만 원)',.5,4,.5,p2,fx(1),function(v){p2=v;draw()});
  function draw(){var g0=b.q1*b.p1+b.q2*b.p2,N=q1*p1+q2*p2,R=q1*b.p1+q2*b.p2,D=N/R*100;
    barPlot(c,250,'기준연도(2005) vs 올해(2012) — 만 원',[{v:g0,c:COL.muted,l:'기준연도 GDP',t:f1(g0,0)},{v:N,c:COL.a,l:'올해 명목',t:f1(N,0)},{v:R,c:COL.g,l:'올해 실질',t:f1(R,0)}],Math.max(N,R,g0)*1.2);
    K([[f1(N,0)+'만 원','명목 GDP(올해 값 × 올해 양)','a'],[f1(R,0)+'만 원','실질 GDP(기준연도 값 × 올해 양)','g'],[f1(D,1),'GDP 디플레이터','i'],[pct(R/g0-1,1)+' / '+pct(N/g0-1,1),'실질 / 명목 성장률','m']]);
    E('명목 = '+q1+'×'+p1+' + '+q2+'×'+p2+' = '+f1(N,0)+' · 실질 = '+q1+'×2 + '+q2+'×1 = '+f1(R,0)+' · 디플레이터 = 명목 ÷ 실질 × 100 = <i>'+f1(D,1)+'</i>');
    I([['g','명목 GDP는 값이 오르기만 해도 커져요. 생산이 실제로 얼마나 늘었는지 보려면 값을 기준연도에 고정한 실질 GDP를 봐요.'],['i','GDP는 "우리 땅 안에서" 만든 것(외국인 포함), GNP는 "우리 국민이" 만든 것(해외 포함)이에요. 해외 리그에서 뛰는 우리 선수의 수입은 우리 GNP, 그 나라 GDP예요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.labor=function(el,cfg){var c=S0(el,cfg,250,'경제활동인구와 고용지표'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var E0=60,U0=4,N=100,d=0;
  S(row,'취업자(명)',40,80,1,E0,null,function(v){E0=v;draw()});S(row,'구직 중인 실업자(명)',0,15,1,U0,null,function(v){U0=v;draw()});S(row,'구직을 포기한 사람(실망실업자)',0,10,1,d,null,function(v){d=v;draw()});
  function draw(){var U=Math.max(0,U0-d),L=E0+U,NL=N-L,ur=U/L,er=E0/N,pr=L/N,ur0=U0/(E0+U0);
    barPlot(c,250,'15세 이상 인구 100명 마을',[{v:E0,c:COL.g,l:'취업자',t:E0},{v:U,c:COL.r,l:'실업자',t:U},{v:NL,c:COL.muted,l:'비경제활동',t:NL},{v:d,c:COL.a,l:'그중 실망실업자',t:d}],100);
    K([[pct(ur,1),'실업률 = 실업자 ÷ 경제활동인구',ur<ur0?'a':'r'],[pct(er,1),'고용률 = 취업자 ÷ 15세 이상','g'],[pct(pr,1),'경제활동참가율','i'],[pct(ur0,1),'포기 전 실업률','m']]);
    E('실업률 = '+U+' ÷ ('+E0+' + '+U+') = <i>'+pct(ur,1)+'</i> · 고용률 = '+E0+' ÷ 100 = '+pct(er,1));
    I([[d?'a':'i',d?'구직을 포기한 사람은 실업자가 아니라 비경제활동인구로 빠져요. 실업률이 떨어져 좋아 보이지만 일자리는 하나도 늘지 않았어요(착시). 고용률은 그대로예요.':'일할 의사와 능력이 있는데 일자리를 못 구한 사람만 실업자예요. 학생·주부·은퇴자는 비경제활동인구예요.'],['i','실업률 하나만 보지 말고 고용률·경제활동참가율을 함께 보세요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.phillips=function(el,cfg){var c=S0(el,cfg,270,'총수요·총공급 충격과 필립스 곡선'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var g=1,s=0;S(row,'총수요 압력(정부지출·소비 등)',-1,1,.1,g,fx(1),function(v){g=v;draw()});S(row,'비용 충격(원자재·임금)',0,2,.1,s,fx(1),function(v){s=v;draw()});
  function draw(){var u=5.5-1.5*g+1*s,pi=4+2*g+3*s;
    var P=plot(c,270,{xlo:2,xhi:10,ylo:0,yhi:12,xl:'실업률(%)',yl:'물가상승률(%)',title:'파랑 필립스 곡선 · 빨강 비용 충격 뒤 곡선'});
    P.fn(function(x){return 6-(4/3)*(x-4)},COL.s,2.4,null,2,9);if(s)P.fn(function(x){return 6-(4/3)*(x-4)+s*(3+4/3)},COL.r,2,[5,4],2,10);
    P.dot(4,6,COL.s,4,'B (4%, 6%)');P.dot(7,2,COL.s,4,'A (7%, 2%)',8,16);P.dot(u,pi,COL.a,7,'지금');stamp(P.ctx,P.W,'원자료 수치 · 설명용');
    K([[f1(u,1)+'%','실업률',u>6?'r':'g'],[f1(pi,1)+'%','물가상승률',pi>5?'r':'g'],[s>0?'비용 인상':g>0?'수요 견인':g<0?'수요 위축':'중립','물가의 원인','a'],[s>.4&&u>5.5?'스태그플레이션':'곡선 위 이동','상태','m']]);
    E('수요 압력 g: 실업률 = 5.5 − 1.5g, 물가 = 4 + 2g → g = 1이면 B(4%, 6%), g = −1이면 A(7%, 2%)');
    I([['i','총수요를 늘리면 실업은 줄지만 물가가 올라요. 단기에는 실업과 인플레이션 사이에 상충관계가 있어요(원리 10, 필립스 곡선).'],[s?'r':'a',s?'원자재 값처럼 비용이 오르면 곡선 자체가 위로 옮겨 가요. 물가도 오르고 실업도 늘어나는 스태그플레이션이 생길 수 있어요.':'비용 충격을 올려 보세요. 수요 견인과 비용 인상 인플레이션은 실업에 반대로 작용해요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== CH11 경제정책 (Y* = 100) ===== */
SIMS.adas=function(el,cfg){var c=S0(el,cfg,270,'총수요(AD)와 총공급(AS)'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var dC=0,dI=-4,dG=0,dX=0,as=0;
  S(row,'소비 C 변화',-6,6,1,dC,null,function(v){dC=v;draw()});S(row,'투자 I 변화',-6,6,1,dI,null,function(v){dI=v;draw()});S(row,'정부지출 G 변화',-6,6,1,dG,null,function(v){dG=v;draw()});S(row,'순수출 NX 변화',-6,6,1,dX,null,function(v){dX=v;draw()});S(row,'비용 충격(AS 위로)',0,10,1,as,null,function(v){as=v;draw()});
  function draw(){var A=dC+dI+dG+dX,Y=100+(A*1.5-as)*.5,Pr=100+(A*1.5+as)*.5;
    var P=plot(c,270,{xlo:85,xhi:115,ylo:85,yhi:115,xl:'실질 GDP(잠재 = 100)',yl:'물가수준',title:'파랑 AD = C + I + G + NX · 빨강 AS · 회색 잠재 GDP'});
    P.seg(100,85,100,115,COL.muted,1.2,[4,4]);P.fn(function(y){return 200+A*1.5-y},COL.s,2.4);P.fn(function(y){return y+as},COL.r,2.4);P.dot(Y,Pr,COL.a,6,'균형');stamp(P.ctx,P.W,'설명용 모형');
    K([[f1(Y,1),'실질 GDP',Y<99?'r':Y>101?'a':'g'],[f1(Pr,1),'물가수준',Pr>101?'a':'i'],[f1(Y-100,1)+'%','GDP 갭',Math.abs(Y-100)<1?'g':'r'],[Y<99?'침체':Y>101?'과열':'안정','경기',Y<99?'r':Y>101?'a':'g']]);
    E('AD: P = 200 + 1.5×(C + I + G + NX 변화) − Y · AS: P = Y + 비용충격 → Y = <i>'+f1(Y,1)+'</i>, P = '+f1(Pr,1));
    I([[Y<99?'r':Y>101?'a':'g',Y<99?'총수요가 모자라 생산이 잠재수준보다 낮아요(침체·실업). 정부지출 G를 늘려 갭을 메워 보세요.':Y>101?'총수요가 넘쳐 물가가 올라요(과열). 지출을 줄이거나 금리를 올리는 정책이 필요해요.':'잠재 GDP 근처예요.'],['i','시장이 스스로 실업·인플레이션을 해결하려면 시간과 비용이 많이 들어요. 그래서 정부가 재정정책·통화정책으로 총수요를 조절해요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.fiscal=function(el,cfg){var c=S0(el,cfg,250,'정부지출 승수와 구축효과'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var dG=4,dT=0,mpc=.6,co=40;
  S(row,'정부지출 증가 ΔG(조 원)',0,10,.5,dG,fx(1),function(v){dG=v;draw()});S(row,'세금 변화 ΔT(조 원)',-5,5,.5,dT,fx(1),function(v){dT=v;draw()});
  S(row,'한계소비성향 c',.4,.9,.05,mpc,fx(2),function(v){mpc=v;draw()});S(row,'구축효과(이자율↑로 줄어드는 몫, %)',0,100,5,co,function(v){return v+'%'},function(v){co=v;draw()});
  function draw(){var m=1/(1-mpc),gross=m*dG-mpc*m*dT,crowd=gross*co/100,net=gross-crowd;
    barPlot(c,250,'GDP 효과(조 원)',[{v:dG,c:COL.muted,l:'처음 지출',t:f1(dG,1)},{v:Math.max(0,gross),c:COL.s,l:'승수 효과',t:f1(gross,1)},{v:crowd,c:COL.r,l:'구축(민간투자 감소)',t:f1(crowd,1)},{v:Math.max(0,net),c:COL.g,l:'순효과',t:f1(net,1)}],Math.max(1,gross)*1.25);
    K([[f1(m,2),'지출 승수 1 ÷ (1 − c)','i'],[f1(gross,1),'구축 전 GDP 증가','s'],[f1(net,1),'최종 GDP 증가',net>0?'g':'r'],[f1(dG-dT,1),'재정적자 늘어난 정도','a']]);
    E('ΔY = [ΔG − c·ΔT] ÷ (1 − c) × (1 − 구축) = ['+f1(dG,1)+' − '+f1(mpc,2)+'×'+f1(dT,1)+'] × '+f1(m,2)+' × '+f1(1-co/100,2)+' = <i>'+f1(net,1)+'</i>');
    I([['i','정부가 쓴 돈은 누군가의 소득이 되고, 그 일부(c)가 다시 쓰이며 효과가 여러 번 이어져요(승수효과).'],['r','국채를 찍어 돈을 빌리면 이자율이 올라 민간 투자가 줄어요(구축효과). 구축이 100%면 정부지출은 민간 지출을 대신할 뿐 GDP를 늘리지 못해요.']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

SIMS.monetary=function(el,cfg){var c=S0(el,cfg,260,'기준금리에서 경기까지'),row=rows(el),K=kpis(el,4),E=eqline(el),I=insight(el);
  var gap=-3,r=3,dG=0;
  buttons(row,'상황',[[-3,'경기 침체(갭 −3%)'],[3,'경기 과열(갭 +3%)']],gap,function(v){gap=v;draw()});S(row,'기준금리(%)',.5,6,.25,r,fx(2),function(v){r=v;draw()});S(row,'정부지출 변화(조 원)',-3,3,.5,dG,fx(1),function(v){dG=v;draw()});
  function draw(){var dr=r-3,yg=gap-1.2*dr+1.5*dG,inf=2+.6*yg,dep=r+.5,loan=r+2;
    barPlot(c,260,'정책 뒤 GDP 갭과 물가',[{v:Math.abs(gap),c:COL.muted,l:'처음 갭 크기',t:gap+'%'},{v:Math.abs(yg),c:Math.abs(yg)<.6?COL.g:COL.r,l:'정책 뒤 갭',t:f1(yg,1)+'%'},{v:Math.max(0,inf),c:COL.a,l:'물가상승률',t:f1(inf,1)+'%'},{v:loan,c:COL.s,l:'대출금리',t:f1(loan,2)+'%'}],8);
    K([[f1(dep,2)+'% / '+f1(loan,2)+'%','예금 / 대출 금리','i'],[f1(yg,1)+'%','정책 뒤 GDP 갭',Math.abs(yg)<.6?'g':'r'],[f1(inf,1)+'%','물가상승률',inf>3?'r':'g'],[gap<0?(dr<0||dG>0?'확장적':'긴축적'):(dr>0||dG<0?'긴축적':'확장적'),'정책 방향','m']]);
    E('GDP 갭 = 처음 갭 − 1.2 × (금리 변화) + 1.5 × (정부지출 변화) = '+gap+' − 1.2×'+f1(dr,2)+' + 1.5×'+f1(dG,1)+' = <i>'+f1(yg,1)+'</i>');
    I([[gap<0?'g':'a',gap<0?'침체 때는 기준금리를 내려(예금금리↓ 대출금리↓) 소비와 투자를 늘리고, 재정지출을 늘리는 확장 정책을 함께 써요.':'과열 때는 기준금리를 올려 소비·투자를 식히고, 재정지출을 줄이는 긴축 정책을 함께 써요.'],['i','중앙은행은 통화량을 직접 정하지 않고 기준금리로 은행 금리를 움직여 간접적으로 통화량을 조절해요(한국은행 → 은행 → 가계·기업).']])}
  addMod(c,function(dt){if(!dt)draw()});draw()};

/* ===== 조교 대결 ===== */
DUELS.startup=function(){var w=300,inv=10000,rev=13000;return {fly:w*12,robo:rev-inv,say:'1년 뒤 손에 남는 돈: 모델 유지 '+nf(w*12)+'만 원, 쇼핑몰 '+nf(rev-inv)+'만 원(수입 1억3천 − 투입 1억). 창업의 기회비용은 1억3천6백만 원이라 600만 원 손해예요.'}};
DUELS.ppfcost=function(){var F=function(x){return Math.sqrt(10000-x*x)},act=F(60)-F(80),fly=70/F(70)*20,robo=(100-F(20))/20*20;return {fly:Math.abs(fly-act),robo:Math.abs(robo-act),say:'컴퓨터 60→80일 때 실제로 포기하는 자동차는 '+act.toFixed(1)+'대예요. 초파리 조교(그 근처 기울기로 계산) 예측 '+fly.toFixed(1)+'대, 주판봇 조교(처음 20대 때와 같다고 가정) 예측 '+robo.toFixed(1)+'대.'}};
DUELS.pricing=function(){var q=function(p){return Math.min(9-2*p,1+2*p)};return {fly:q(2),robo:q(3),say:'실제 거래량 = 수요량과 공급량 중 작은 쪽. 2만 원이면 5장, 3만 원이면 사려는 사람이 3명뿐이라 3장이에요(4장은 안 팔리고 남아요).'}};
DUELS.raise=function(){var R=function(p){return p*(100-p)};return {fly:R(63),robo:R(77),say:'지금 가격 70, 매출 2,100(탄력성 2.33). 10% 내리면(63) 매출 '+nf(R(63))+', 10% 올리면(77) 매출 '+nf(R(77))+'.'}};
DUELS.ceil=function(){return {fly:5,robo:3,say:'상한 없음: 균형 2만 원에 5가구가 집을 구해요. 상한 1만 원: 집주인이 3채만 내놓아 7가구 중 3가구만 구하고 4가구는 줄을 서요.'}};
DUELS.qmax=function(){var W=function(q){return 80*q-q*q};return {fly:W(40),robo:W(60),say:'총잉여: 균형 거래량 40이면 '+W(40)+', 억지로 60까지 거래하면 '+W(60)+'. 40을 넘는 20단위는 비용이 가치보다 큰 거래예요.'}};
DUELS.laffer2=function(){var R=function(t){return t*(80-t)/2},D=function(t){return t*t/4};return {fly:R(20),robo:R(40),say:'세수: 세금 20이면 '+R(20)+', 40이면 '+R(40)+'. 세수는 주판봇 조교 쪽이 크지만, 사중손실은 '+D(20)+' → '+D(40)+'으로 4배가 돼요.'}};
DUELS.cheat=function(){return {fly:1800,robo:2000,say:'질이 30을 지킬 때: 약속 지키기(30) 이윤 1,800, 몰래 40으로 늘리기 이윤 2,000. 하지만 질도 똑같이 생각해 40으로 늘리면 둘 다 1,600이에요.'}};
DUELS.pigou=function(){var D=20,W=function(q){return 80*q-q*q-D*q};return {fly:W(30),robo:W(40),say:'이웃 피해까지 넣은 사회적 총잉여: 피구세(20)로 30단위면 '+W(30)+', 시장에 맡겨 40단위면 '+W(40)+'.'}};
DUELS.realgdp=function(){var g0=98,N=170,R=110,tr=R/g0-1,nom=N/g0-1;return {fly:0,robo:(nom-tr)*100,fmt:'',say:'실제 생산 증가율(값을 고정한 실질 기준) '+(tr*100).toFixed(1)+'%. 초파리 조교(실질 GDP) 예측 오차 0%p, 주판봇 조교(명목 GDP '+(nom*100).toFixed(1)+'%) 예측 오차 '+((nom-tr)*100).toFixed(1)+'%p.'}};
DUELS.mix=function(){var gap=-3,eff=1.5,fly=gap+1.2*1+eff*1.2,robo=gap+eff*4;return {fly:Math.abs(fly),robo:Math.abs(robo),say:'침체 갭 −3%. 초파리 조교(금리 1%p 인하 + 지출 1.2조) → 갭 '+fly.toFixed(1)+'%, 주판봇 조교(지출 4조 한 번에) → 갭 +'+robo.toFixed(1)+'%로 과열.'}};
