/* 경제학 원론 연구실 — 장별 동적 대시보드 (설명용 모형, 숫자는 예시값) */
function rd(v,d){return +(+v).toFixed(d==null?0:d)}
DASHES['01']={tag:'CH01',title:'창업할까, 계속 일할까 — 기회비용 대시보드',sub:'모델 월급과 쇼핑몰 1년 수입·투입비용(만 원)',play:'rev',playLabel:'쇼핑몰 수입을 8,000→18,000으로',
  params:[['w','모델 월급',100,600,10,300,String],['inv','쇼핑몰 투입비용',5000,15000,500,10000,String],['rev','쇼핑몰 1년 수입',8000,18000,500,13000,String]],
  f:function(p){var oc=p.inv+12*p.w,acc=p.rev-p.inv,eco=p.rev-oc,xs=seqv(8000,18000,41);
    return {k:[[nf(acc),'회계상 이윤',acc>=0?'i':'r'],[nf(12*p.w),'암묵적 비용(포기한 연봉)','m'],[nf(oc),'기회비용 합','a'],[nf(eco),'경제적 이윤',eco>=0?'g':'r']],
      c:[{t:'line',title:'수입에 따른 회계상 이윤과 경제적 이윤',xs:xs,ys:[{n:'회계상',c:COL.i,d:xs.map(function(r){return r-p.inv})},{n:'경제적',c:COL.g,d:xs.map(function(r){return r-oc})}],hline:0,hlabel:'0',mark:{x:p.rev,y:eco,l:'지금'},xl:'쇼핑몰 1년 수입',fx:function(v){return nf(v)}},
        {t:'bar',title:'수입과 기회비용 비교',vals:[p.rev,p.inv,12*p.w,oc],labels:['수입','명시적 비용','암묵적 비용','기회비용'],cols:[COL.g,COL.s,COL.m,COL.r],fy:function(v){return nf(v)}}],
      note:[[eco>=0?'g':'r',eco>=0?'경제적 이윤이 0 이상이에요. 포기한 월급까지 넣어도 창업이 낫습니다.':'회계상 이윤은 '+nf(acc)+'만 원이지만, 포기한 연봉 '+nf(12*p.w)+'만 원을 넣으면 '+nf(-eco)+'만 원 손해예요.'],['i','수입이 기회비용('+nf(oc)+'만 원)을 넘는 지점이 창업의 손익분기점이에요.']]}}};

DASHES['02']={tag:'CH02',title:'생산가능곡선 대시보드',sub:'컴퓨터² + 자동차² = (100 × 성장)²',play:'x',playLabel:'컴퓨터를 0→100으로',
  params:[['x','컴퓨터 생산량',0,100,5,60,String],['g','경제성장(%)',0,30,5,0,function(v){return '+'+v+'%'}],['e','자원 활용도(%)',50,100,5,100,function(v){return v+'%'}]],
  f:function(p){var s=1+p.g/100,F=function(x){return Math.sqrt(Math.max(0,1e4*s*s-x*x))},y=F(p.x)*p.e/100,xs=seqv(0,100*s,51),oc=function(x){return F(x)-F(Math.min(x+10,100*s))};
    return {k:[[rd(y,1),'자동차 생산',p.e<100?'r':'g'],[rd(oc(p.x),1)+'대','컴퓨터 10대 더 → 포기할 자동차','a'],[p.e<100?'비효율':'효율','곡선 위인가',p.e<100?'r':'g'],[rd(F(p.x)-y,1),'놀리는 자원으로 더 만들 수 있는 자동차','i']],
      c:[{t:'line',title:'생산가능곡선과 지금 생산점',xs:xs,ys:[{n:'처음 곡선',c:COL.muted,dash:[5,4],d:xs.map(function(x){return Math.sqrt(Math.max(0,1e4-x*x))})},{n:'지금 곡선',c:COL.s,d:xs.map(F)}],ymin:0,ymax:135,mark:{x:p.x,y:y,l:'생산점'},xl:'컴퓨터'},
        {t:'line',title:'컴퓨터 10대를 더 만들 때의 기회비용',xs:seqv(0,90,46),ys:[{c:COL.a,d:seqv(0,90,46).map(oc)}],ymin:0,mark:{x:p.x,y:oc(p.x),l:'지금'},xl:'지금 컴퓨터 생산량'}],
      note:[['a','컴퓨터를 많이 만들수록 10대 더 만들 때 포기하는 자동차가 늘어나요(기회비용 체증).'],[p.g?'g':'i',p.g?'기술 진보로 곡선이 바깥으로 옮겨 가 둘 다 더 만들 수 있어요(경제성장).':'성장 슬라이더를 올리면 곡선 자체가 바깥으로 이동해요.']]}}};

DASHES['03']={tag:'CH03',title:'음반 시장 수요·공급 대시보드',sub:'Qd = 9 − 2P + 수요 이동 · Qs = 1 + 2P + 공급 이동 (P는 만 원)',play:'p',playLabel:'가격을 0.5→4로',
  params:[['p','지금 가격',.5,4,.25,3,function(v){return v.toFixed(2)}],['d','수요 이동',-4,4,1,0,String],['s','공급 이동',-4,4,1,0,String]],
  f:function(p){var Pe=(8+p.d-p.s)/4,Qe=9+p.d-2*Pe,qd=Math.max(0,9+p.d-2*p.p),qs=Math.max(0,1+p.s+2*p.p),ps=seqv(.25,4.5,40);
    return {k:[[rd(Pe,2),'균형가격','g'],[rd(Qe,1),'균형거래량','g'],[rd(qd,1)+' / '+rd(qs,1),'수요량 / 공급량','i'],[qd>qs?'초과수요':qd<qs?'초과공급':'균형','상태',qd===qs?'g':'r']],
      c:[{t:'fn',draw:function(cv,H){var P=plot(cv,H,{xlo:0,xhi:14,ylo:0,yhi:5,T:46,xl:'수량',yl:'가격',title:'수요(파랑)·공급(빨강)·지금 가격(주황)'});P.fn(function(Q){return (9+p.d-Q)/2},COL.s,2.4,null,0,9+p.d);P.fn(function(Q){return (Q-1-p.s)/2},COL.r,2.4,null,Math.max(0,1+p.s),14);P.seg(0,p.p,14,p.p,COL.a,1.5,[4,3]);P.dot(Qe,Pe,COL.g,5,'E');stamp(P.ctx,P.W,'예시값')}},
        {t:'bar',title:'지금 가격에서',vals:[qd,qs,Math.min(qd,qs)].map(function(v){return rd(v,1)}),labels:['수요량','공급량','실제 거래량'],cols:[COL.s,COL.r,COL.g]}],
      note:[[qd===qs?'g':'a',qd>qs?'모자라니 가격이 올라가요.':qd<qs?'남으니 가격이 내려가요.':'수요량 = 공급량이에요.'],['i','수요와 공급이 함께 움직이면 가격과 거래량 중 하나는 방향이 불분명할 수 있어요. 둘 다 +2로 올려 보세요(가격 그대로, 거래량 증가).']]}}};

DASHES['04']={tag:'CH04',title:'가격과 매출 대시보드',sub:'직선 수요 Q = A − P · 매출 = P × Q',play:'p',playLabel:'가격을 5→95로',
  params:[['p','가격',5,95,1,70,String],['A','수요 크기 A',60,140,5,100,String]],
  f:function(p){var q=Math.max(0,p.A-p.p),e=q>0?p.p/q:Infinity,ps=seqv(1,p.A-1,60),R=function(x){return x*Math.max(0,p.A-x)};
    return {k:[[isFinite(e)?rd(e,2):'∞','가격탄력성',e>1?'r':'i'],[nf(R(p.p)),'매출','g'],[p.A/2,'매출이 가장 큰 가격(탄력성 1)','a'],[e>1?'내리면 매출↑':e<1?'올리면 매출↑':'그대로가 최대','가격 전략','m']],
      c:[{t:'line',title:'가격별 매출',xs:ps,ys:[{c:COL.g,d:ps.map(R)}],ymin:0,mark:{x:p.p,y:R(p.p),l:'지금'},xl:'가격'},
        {t:'line',title:'가격별 탄력성 (1 위는 탄력적)',xs:ps,ys:[{c:COL.r,d:ps.map(function(x){return Math.min(6,x/(p.A-x))})}],ymin:0,ymax:6,hline:1,hlabel:'탄력성 1',mark:{x:p.p,y:Math.min(6,e),l:'지금'},xl:'가격'}],
      note:[[e>1?'r':'i',e>1?'탄력적 구간: 값을 올리면 손님이 더 크게 줄어 매출이 줄어요.':'비탄력적 구간: 값을 올리면 매출이 늘어요.'],['a','매출이 가장 큰 곳은 탄력성이 정확히 1인 가격이에요.']]}}};

DASHES['05']={tag:'CH05',title:'가격 규제 대시보드',sub:'Qd = 9 − 2P · Qs = 1 + 2P · 균형 2만 원·5개',play:'pc',playLabel:'규제 가격을 0.5→3.5로',
  params:[['pc','규제 가격(만 원)',.5,3.5,.25,1,function(v){return v.toFixed(2)}],['mode','규제 종류(0 상한 · 1 하한)',0,1,1,0,function(v){return v?'하한(최저가격)':'상한(최고가격)'}]],
  f:function(p){var P=p.mode?Math.max(p.pc,2):Math.min(p.pc,2),qd=9-2*P,qs=1+2*P,tr=Math.min(qd,qs),bind=p.mode?p.pc>2:p.pc<2;
    return {k:[[bind?'실효 있음':'실효 없음','규제의 효과',bind?'r':'g'],[rd(P,2),'실제 거래 가격','i'],[rd(tr,1),'실제 거래량','m'],[bind?(p.mode?'초과공급 ':'초과수요 ')+rd(Math.abs(qd-qs),1):'없음','남거나 모자란 양',bind?'r':'g']],
      c:[{t:'fn',draw:function(cv,H){var G=plot(cv,H,{xlo:0,xhi:12,ylo:0,yhi:5,T:46,xl:'수량',yl:'가격',title:'규제선(주황)과 시장'});G.fn(function(Q){return (9-Q)/2},COL.s,2.4,null,0,9);G.fn(function(Q){return (Q-1)/2},COL.r,2.4,null,1,11);G.seg(0,p.pc,12,p.pc,COL.a,2,[5,4]);if(bind)G.seg(Math.min(qd,qs),P,Math.max(qd,qs),P,COL.r,5);G.dot(5,2,COL.g,5,'균형');stamp(G.ctx,G.W,'예시값')}},
        {t:'bar',title:'규제 가격에서',vals:[qd,qs,tr].map(function(v){return rd(v,1)}),labels:['수요량','공급량','거래량'],cols:[COL.s,COL.r,COL.g]}],
      note:[[bind?'r':'g',bind?(p.mode?'최저가격이 균형보다 높아 남는 물건(노동시장이면 실업)이 생겨요.':'최고가격이 균형보다 낮아 모자람이 생기고 줄서기·암시장이 나타나요.'):'규제선이 시장가격 쪽에 있지 않아 효과가 없어요.'],['i','상한은 균형보다 낮을 때, 하한은 균형보다 높을 때만 실효가 있어요.']]}}};

DASHES['06']={tag:'CH06',title:'잉여와 효율성 대시보드',sub:'수요 P = A − Q · 공급 P = 20 + Q · 거래량을 정해 보기',play:'q',playLabel:'거래량을 0→70으로',
  params:[['q','거래량',0,70,1,40,String],['A','수요 크기 A',70,130,5,100,String]],
  f:function(p){var Qe=(p.A-20)/2,Pe=p.A-Qe,q=p.q,CS=q<=Qe?q*q/2+(p.A-q-Pe)*0+(Pe-(p.A-q))*0:0,W=function(x){return (p.A-20)*x-x*x},cs=Math.max(0,q<=Qe?(p.A-Pe)*Qe/2-(Qe-q)*(Qe-q)/2:(p.A-Pe)*Qe/2),ws=W(Math.max(0,q)),xs=seqv(0,70,71);
    return {k:[[rd(Qe,1),'균형 거래량','g'],[rd(W(Qe),0),'최대 총잉여','g'],[rd(ws,0),'지금 총잉여',Math.abs(q-Qe)<.5?'g':'a'],[rd(W(Qe)-ws,0),'잃은 잉여','r']],
      c:[{t:'line',title:'거래량별 총잉여',xs:xs,ys:[{c:COL.g,d:xs.map(W)}],mark:{x:q,y:ws,l:'지금'},xl:'거래량'},
        {t:'bar',title:'균형에서 잉여 나누기',vals:[(p.A-Pe)*Qe/2,(Pe-20)*Qe/2,W(Qe)-ws].map(function(v){return rd(v,0)}),labels:['소비자잉여','생산자잉여','지금 잃은 잉여'],cols:[COL.g,COL.s,COL.r]}],
      note:[[Math.abs(q-Qe)<.5?'g':'r',Math.abs(q-Qe)<.5?'균형에서 총잉여가 가장 커요. 자유로운 시장이 효율적인 이유예요.':q<Qe?'균형보다 적게 거래하면 서로 이득인 거래가 막혀요.':'균형보다 많이 거래하면 비용이 가치보다 큰 거래까지 하게 돼요.'],['i','효율은 파이의 크기, 형평은 파이를 나누는 방식이에요. 이 그림은 효율만 말해 줘요.']]}}};

DASHES['07']={tag:'CH07',title:'세금의 크기 대시보드',sub:'수요 P = 100 − Q · 공급 P = 20 + s·Q',play:'t',playLabel:'세금을 0→80으로',
  params:[['t','1단위당 세금',0,80,2,20,String],['s','공급 기울기 s(클수록 비탄력)',.25,4,.25,1,function(v){return v.toFixed(2)}]],
  f:function(p){var Q0=80/(1+p.s),Q=function(t){return Math.max(0,(80-t)/(1+p.s))},R=function(t){return t*Q(t)},D=function(t){return t*(Q0-Q(t))/2},ts=seqv(0,80,41);
    return {k:[[rd(Q(p.t),1),'거래량(세전 '+rd(Q0,1)+')','i'],[rd(R(p.t),0),'세수','g'],[rd(D(p.t),0),'사중손실','r'],[Math.round(p.s/(1+p.s)*100)+'%','판매자 부담 몫','a']],
      c:[{t:'line',title:'세금 크기별 세수(초록)와 사중손실(빨강)',xs:ts,ys:[{n:'세수',c:COL.g,d:ts.map(R)},{n:'사중손실',c:COL.r,d:ts.map(D)}],ymin:0,mark:{x:p.t,y:R(p.t),l:'지금'},xl:'세금'},
        {t:'bar',title:'지금 세금에서',vals:[R(p.t),D(p.t)].map(function(v){return rd(v,0)}),labels:['세수','사중손실'],cols:[COL.g,COL.r]}],
      note:[['r','사중손실은 세금의 제곱에 비례해 커져요. 세금을 두 배로 하면 손실은 네 배예요.'],['a','공급이 탄력적일수록(s가 작을수록) 같은 세금에 거래가 더 많이 줄어 사중손실이 커요.']]}}};

DASHES['08']={tag:'CH08',title:'기업 수와 시장 성과 대시보드',sub:'물 수요 P = 120 − Q · 한계비용 0 · n개 기업이 생산량으로 경쟁(꾸르노)',play:'n',playLabel:'기업 수를 1→20으로',
  params:[['n','기업 수 n',1,20,1,2,String],['a','수요 크기',80,160,10,120,String]],
  f:function(p){var Q=function(n){return n*p.a/(n+1)},P=function(n){return p.a-Q(n)},ns=seqv(1,20,20),q=Q(p.n),pr=P(p.n),dwl=(p.a-q)*(p.a-q)/2;
    return {k:[['$'+rd(pr,1),'시장가격','i'],[rd(q,1),'총생산(경쟁이면 '+p.a+')','m'],[nf(rd(pr*q,0)),'기업 이윤 합','a'],[nf(rd(dwl,0)),'사중손실','r']],
      c:[{t:'line',title:'기업 수가 늘수록 가격은 한계비용(0)으로',xs:ns,ys:[{c:COL.s,d:ns.map(P)}],ymin:0,mark:{x:p.n,y:pr,l:'지금'},xl:'기업 수'},
        {t:'bar',title:'잉여 나누기',vals:[q*q/2,pr*q,dwl].map(function(v){return rd(v,0)}),labels:['소비자잉여','이윤','사중손실'],cols:[COL.g,COL.a,COL.r],fy:function(v){return nf(v)}}],
      note:[['i',p.n===1?'기업이 하나면 독점: 생산을 반으로 줄이고 가격을 올려요.':p.n<=3?'소수 기업(과점)은 독점과 경쟁 사이 어딘가에서 멈춰요.':'기업이 많아질수록 완전경쟁에 가까워져 가격이 비용 수준으로 내려가요.'],['a','담합하면 기업 수가 많아도 독점처럼 행동해요. 그래서 공정거래법이 담합을 금지해요.']]}}};

DASHES['09']={tag:'CH09',title:'소득분배와 재분배 대시보드',sub:'10개 소득 계층의 로렌츠 곡선과 지니계수 (설명용 분포)',play:'tau',playLabel:'재분배를 0→60%로',
  params:[['k','소득 격차 정도',0,4,.1,2,function(v){return v.toFixed(1)}],['tau','재분배 정도(%)',0,60,5,0,function(v){return v+'%'}]],
  f:function(p){var L=lorenz(p.k,p.tau/100),L0=lorenz(p.k,0),xs=seqv(0,1,11);
    return {k:[[rd(L0.gini,3),'지니계수(재분배 전)','i'],[rd(L.gini,3),'지니계수(재분배 후)','g'],[rd(L.dec,2),'10분위분배율','a'],[(L.sh[9]*100).toFixed(1)+'%','상위 10% 소득 몫','r']],
      c:[{t:'line',title:'로렌츠 곡선',xs:xs,ys:[{n:'평등선',c:COL.muted,dash:[4,4],d:xs},{n:'재분배 전',c:COL.s,d:L0.cum},{n:'재분배 후',c:COL.g,d:L.cum}],ymin:0,ymax:1,xl:'인구 누적',fx:function(v){return Math.round(v*100)+'%'},fy:function(v){return Math.round(v*100)+'%'}},
        {t:'bar',title:'계층별 소득 몫(%)',vals:L.sh.map(function(v){return rd(v*100,1)}),labels:['1','2','3','4','5','6','7','8','9','10'],cols:L.sh.map(function(v,i){return i<4?COL.g:i>7?COL.r:COL.s})}],
      note:[['i','지니계수는 0(완전평등)~1(완전불평등), 10분위분배율은 2(평등)~0(불평등)이에요. 방향이 반대예요.'],['a','재분배는 형평을 높이지만 세금이 일할 유인을 줄일 수 있어요. 얼마나 할지는 사회의 가치 선택이에요.']]}}};

DASHES['10']={tag:'CH10',title:'고용지표 대시보드',sub:'15세 이상 인구 100명 마을',play:'d',playLabel:'실망실업자를 0→10명으로',
  params:[['E','취업자',40,80,1,60,String],['U','구직 중인 실업자',0,15,1,6,String],['d','구직 포기(실망실업자)',0,10,1,0,String]],
  f:function(p){var U=Math.max(0,p.U-p.d),ur=U/(p.E+U),ds=seqv(0,Math.min(10,p.U),Math.min(10,p.U)+1);
    return {k:[[(ur*100).toFixed(1)+'%','실업률',ur<.04?'g':'r'],[p.E+'%','고용률','g'],[(p.E+U)+'%','경제활동참가율','i'],[100-p.E-U+'명','비경제활동인구','m']],
      c:[{t:'line',title:'구직 포기가 늘 때 실업률(빨강)과 고용률(초록)',xs:ds,ys:[{n:'실업률',c:COL.r,d:ds.map(function(d){var u=p.U-d;return u/(p.E+u)*100})},{n:'고용률',c:COL.g,d:ds.map(function(){return p.E})}],ymin:0,mark:{x:p.d,y:ur*100,l:'지금'},xl:'실망실업자 수'},
        {t:'bar',title:'마을 사람 나누기',vals:[p.E,U,100-p.E-U],labels:['취업자','실업자','비경제활동'],cols:[COL.g,COL.r,COL.muted]}],
      note:[['a','구직을 포기하면 실업자에서 빠져 실업률이 떨어지지만 고용률은 그대로예요. 실업률 하나만 보면 경기가 좋아진 것처럼 착각할 수 있어요.'],['i','고용률·참가율을 함께 봐야 일자리 사정을 바로 읽을 수 있어요.']]}}};

DASHES['11']={tag:'CH11',title:'경기 조절 대시보드',sub:'처음 GDP 갭 −3% · 금리 1%p 인하 = 갭 +1.2%p · 지출 1조 = 갭 +1.5%p',play:'r',playLabel:'기준금리를 6→0.5%로',
  params:[['r','기준금리(%)',.5,6,.25,3,function(v){return v.toFixed(2)}],['g','정부지출 변화(조 원)',-3,4,.5,0,function(v){return v.toFixed(1)}],['gap','처음 GDP 갭(%)',-4,4,1,-3,String]],
  f:function(p){var Y=function(r,g){return p.gap-1.2*(r-3)+1.5*g},y=Y(p.r,p.g),inf=2+.6*y,rs=seqv(.5,6,23);
    return {k:[[rd(y,1)+'%','정책 뒤 GDP 갭',Math.abs(y)<.6?'g':'r'],[rd(inf,1)+'%','물가상승률',inf>3?'r':'g'],[rd(p.r+2,2)+'%','대출금리','i'],[y<-.5?'아직 침체':y>.5?'과열':'안정','경기','m']],
      c:[{t:'line',title:'기준금리별 GDP 갭(지금 정부지출 유지)',xs:rs,ys:[{c:COL.s,d:rs.map(function(r){return Y(r,p.g)})}],hline:0,hlabel:'잠재 GDP',mark:{x:p.r,y:y,l:'지금'},xl:'기준금리(%)'},
        {t:'bar',title:'정책 효과 나누기(%p)',vals:[-1.2*(p.r-3),1.5*p.g,y].map(function(v){return rd(v,1)}),labels:['금리 효과','재정 효과','최종 갭'],cols:[COL.i,COL.a,Math.abs(y)<.6?COL.g:COL.r]}],
      note:[[p.gap<0?'g':'a',p.gap<0?'침체: 금리 인하 + 지출 확대(확장 정책조합)로 갭을 0으로 메워 보세요.':'과열: 금리 인상 + 지출 축소(긴축 정책조합)로 갭을 0으로 줄여 보세요.'],['r','너무 세게 하면 반대쪽(과열·침체)으로 넘어가요. 정책은 세기와 시점이 중요해요.']]}}};
