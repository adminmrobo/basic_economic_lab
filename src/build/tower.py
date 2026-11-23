# -*- coding: utf-8 -*-
"""생활경제 시장 — 3D 첫 화면(시장 안내)

시장 보기 쪽(tower.html)은 시장 전체를, 장 쪽은 그 장이 들어 있는 가게를 3D로 보여 주고
가게 평면(방 = 이 쪽의 단계)과 둘러보는 순서를 안내한다.

- build.py / build_extra.py 가 nav 바로 뒤, 표지 그림 앞에 tower_html(key)를 넣는다.
- 이미 빌드된 HTML에는 add_tower.py 로 같은 블록을 넣거나 갈아 끼운다(표식 <!--tower:start--> … <!--tower:end-->).
- three.js 는 CDN(jsdelivr)에서 불러온다. 불러오지 못하면 오른쪽 안내판만으로 쓸 수 있다.
"""
import os, json, html

B = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(B, 'tower.css'), encoding='utf-8').read()
JS = open(os.path.join(B, 'tower.js'), encoding='utf-8').read()
THREE_VER = '0.170.0'

COMPANY = dict(ko='생활경제 시장', en='Everyday Economics Market', hq='골목 강의 시장',
               motto='골목을 따라 가게를 한 곳씩 들르며 경제를 읽는 강의 시장',
               sign=['ECON MARKET', '생활경제 시장'], plate='생활경제 시장  ·  서울', svg='ECON',
               note='가상의 강의 시장입니다. 가게마다 강의실이 하나 있고, 가게마다 박사가 그 장을 강의합니다.')

CLOCKS = [('서울', 'Asia/Seoul'), ('런던', 'Europe/London'), ('뉴욕', 'America/New_York'), ('싱가포르', 'Asia/Singapore')]

PAL = ['#3f5fa8', '#138a52', '#d23f2c', '#2563c9', '#a8329f', '#b77800', '#14899a', '#7a45d6']

def LES(a, b, c, sa, sb, sc):
    return [('three', '안내 데스크', '3줄 요약'), ('cast', '강의실 입구', '강의실 식구'), ('lv1', a, '단계 ① ' + sa), ('lv2', b, '단계 ② ' + sb), ('lv3', c, '단계 ③ ' + sc),
            ('dash', '전광판', '한눈에 보는 대시보드'), ('duel', '토론 코트', '조교 대결'), ('sum', '정리 칠판', '정리'), ('kg', '자료실', '지식 색인 · 꾸러미')]

REV = [('three', '안내 데스크', '3줄 요약'), ('cast', '강의실 입구', '강의실 식구'), ('summary', '요약 게시판', '1부 요약'), ('orig', '시험장', '2부 원자료 문제'),
       ('calc', '계산 연습실', '3부 생활 계산'), ('score', '점수판', '장별 점수'), ('kg', '자료실', '지식 색인 · 꾸러미')]

IDX = [('micro', '안내 데스크', '경제학 원론이란'), ('map', '가게 안내판', '목차'), ('keys', '한 줄 핵심 게시판', '한 줄 핵심 모음'), ('dash', '종합 전광판', '종합 대시보드'),
       ('path', '개념 계단', '개념 흐름'), ('how', '식구 라운지', '식구 · 사용법'), ('about', '자료 보관실', '자료와 원칙')]

PRAC = [('ticket', '경기장 매표소', '매표소 — 수요·공급·가격상한'), ('shop', '스포츠용품점', '용품점 — 탄력성·매출'), ('city', '시청 정책실', '시청 — 세금·외부효과'), ('bank', '중앙은행 상황실', '중앙은행 — 경기와 정책')]

def CH(key, label, file, dept, en, title, biz, rooms):
    return dict(key=key, label=label, file=file, dept=dept, en=en, branch='생활경제 시장', title=title, ep=title.split(' ')[0], biz=biz, rooms=rooms)

FLOORS = [
 dict(key='lobby', label='입구', file='index.html', dept='시장 입구 · 안내소', en='Market Gate & Directory', branch='생활경제 시장',
      title='목차 — 경제학 원론 연구실', ep='목차', biz='생활경제 시장의 입구 안내소입니다. 가게 안내판에서 강의실(장)을 고르면 그 가게로 걸어갑니다.', rooms=IDX),
 CH('01', '1호', '01_ten_principles.html', '선택 강의실', 'Choice Room', 'CH01 경제학의 10대 원리', '희소성, 기회비용, 한계적 판단을 다루는 첫 강의실이에요.', LES('희소성 진열대', '기회비용 계산대', '한계 판단 트랙', '희소성과 경제문제', '기회비용과 매몰비용', '한계적 판단과 유인')),
 CH('02', '2호', '02_think_like_economist.html', '모형 강의실', 'Model Room', 'CH02 경제학자처럼 생각하기', '현실을 단순하게 만든 모형으로 생각하는 법을 배우는 강의실이에요.', LES('모형 작업대', '생산가능곡선 코트', '토론 테이블', '가정과 모형', '생산가능곡선', '미시·거시와 실증·규범')),
 CH('03', '3호', '03_supply_demand.html', '시장 강의실', 'Market Room', 'CH03 수요와 공급', '사려는 힘과 팔려는 힘이 만나 가격이 정해지는 과정을 다뤄요.', LES('수요 관람석', '공급 관람석', '균형 센터서클', '수요', '공급', '시장균형과 이동')),
 CH('04', '4호', '04_elasticity.html', '탄력성 강의실', 'Elasticity Room', 'CH04 탄력성과 그 응용', '가격이 1% 바뀔 때 몇 % 반응하는지 재고, 매출 결정에 쓰는 강의실이에요.', LES('반응 측정실', '매출 계산대', '탄력성 지도', '가격탄력성', '탄력성과 매출', '소득·교차·공급 탄력성')),
 CH('05', '5호', '05_government_policy.html', '정책 강의실', 'Policy Room', 'CH05 수요·공급과 정부정책', '가격상한·하한과 세금이 시장을 어떻게 바꾸는지 계산해요.', LES('상한선 계단', '하한선 계단', '세금 귀착실', '가격상한제', '가격하한제', '조세의 귀착')),
 dict(key='05m', label='쉼터A', file='05m_midterm_review.html', dept='중간 점검 쉼터', en='Mid-term Review Rest Area', branch='생활경제 시장',
      title='중간 요약정리 및 퀴즈 — CH01~CH05', ep='중간 점검', biz='1~5호 가게 강의를 돌아보며 요약을 보고, 원자료 문제와 생활 계산으로 점검하는 쉼터예요.', rooms=REV),
 CH('06', '6호', '06_market_efficiency.html', '잉여 강의실', 'Surplus Room', 'CH06 소비자·생산자·시장의 효율성', '지불용의와 공급용의로 잉여를 재고, 시장이 효율적인 이유를 봐요.', LES('경매 테이블', '견적 테이블', '총잉여 전광판', '소비자잉여', '생산자잉여', '총잉여와 효율성')),
 CH('07', '7호', '07_cost_of_taxation.html', '조세 강의실', 'Taxation Room', 'CH07 조세의 경제적 비용', '세금이 만드는 사중손실과 세수의 한계를 계산하는 강의실이에요.', LES('잉여 계산대', '탄력성 저울', '래퍼 곡선 언덕', '세금과 잉여', '탄력성과 사중손실', '세금 크기와 세수')),
 CH('08', '8호', '08_market_structure.html', '시장구조 강의실', 'Market Structure Room', 'CH08 시장구조 — 경쟁·독점·과점', '기업 수와 제품 차이로 시장을 나누고, 각 시장의 가격과 효율을 비교해요.', LES('완전경쟁 광장', '독점 매표소', '과점 협상실', '완전경쟁', '독점', '과점과 독점적 경쟁')),
 CH('09', '9호', '09_market_failure.html', '공공경제 강의실', 'Public Economics Room', 'CH09 시장실패와 정부의 역할', '외부효과·공공재·소득분배처럼 시장이 혼자 풀지 못하는 문제를 다뤄요(재정학).', LES('외부효과 측정실', '공공재 공원', '분배 저울', '외부효과', '공공재', '소득분배와 지니계수')),
 CH('10', '10호', '10_macro_economy.html', '국민경제 강의실', 'Macro Room', 'CH10 국민경제와 경기변동', 'GDP·실업·인플레이션으로 나라 경제 전체를 읽는 거시 강의실이에요.', LES('GDP 계기판', '고용 통계실', '물가 관측실', 'GDP', '실업', '인플레이션과 필립스 곡선')),
 CH('11', '11호', '11_economic_policy.html', '경제정책 강의실', 'Policy Mix Room', 'CH11 정부의 경제정책', '재정정책과 통화정책으로 경기를 조절하는 방법을 다뤄요.', LES('총수요 작업대', '재정 계산실', '금리 조종실', '총수요와 총공급', '재정정책', '통화정책과 정책조합')),
 dict(key='11f', label='쉼터B', file='11f_final_review.html', dept='기말 점검 쉼터', en='Final Review Rest Area', branch='생활경제 시장',
      title='기말 요약정리 및 퀴즈 — CH06~CH11', ep='기말 점검', biz='6~11호 가게 강의를 요약하고 퀴즈로 마무리하는 쉼터예요. 골목 끝 광장의 실전 연습장으로 가기 전에 들러요.', rooms=REV),
 dict(key='roof', label='광장', file='practice/index.html', dept='광장 실전 연습장', en='Plaza Practice Arena', branch='생활경제 시장',
      title='마지막 장 · 실전 연습장 — 매표소·용품점·시청·중앙은행', ep='실전 연습장', biz='골목 끝 광장의 경기장이에요. 매표소·용품점·시청·중앙은행을 직접 운영하며 열한 장의 원리를 적용합니다.', rooms=PRAC),
]
for i, f in enumerate(FLOORS):
    f['color'] = '#5d6278' if f['key'] == 'lobby' else ('#138a52' if f['key'] in ('05m', '11f', 'roof') else PAL[(i - 1) % len(PAL)])
KEYS = [f['key'] for f in FLOORS]
BYKEY = {f['key']: f for f in FLOORS}

e = lambda s: html.escape(str(s), quote=True)

def floor_name(f):
    return f'{f["label"]} {f["dept"]}'

def _data(cur, home=''):
    fl = [dict(key=f['key'], label=f['label'], dept=f['dept'], en=f['en'], branch=f['branch'], title=f['title'], ep=f['ep'], file=f['file'],
               biz=f['biz'], color=f['color'], rooms=[dict(id=a, name=b, sec=c) for a, b, c in f['rooms']]) for f in FLOORS]
    return dict(cur=cur, home=home, company=COMPANY, floors=fl)

def _route_items(f):
    o = []
    for i, (a, b, c) in enumerate(f['rooms']):
        tag = '입구' if i == 0 else str(i)
        o.append(f'<li data-i="{i}"><a href="#{a}"><i>{tag}</i><b>{e(b)}</b><span>{e(c)}</span></a></li>')
    return ''.join(o)

def _panel_floor(f):
    i = KEYS.index(f['key'])
    dn = FLOORS[i - 1] if i > 1 else None          # 1호 앞은 시장 입구(목차)
    up = FLOORS[i + 1] if i + 1 < len(FLOORS) else None
    el = []
    el.append(f'<a class="dn" href="{dn["file"]}" title="{e(dn["title"])}">◀ {e(floor_name(dn))}</a>' if dn else '<span class="dn off">◀ 앞 가게 없음</span>')
    el.append('<a class="lob" href="index.html">로비 · 목차</a>')
    el.append(f'<a class="up" href="{up["file"]}" title="{e(up["title"])}">▶ {e(floor_name(up))}</a>' if up else '<span class="up off">▶ 광장이 골목 끝</span>')
    first = '가게 입구로 들어오면 안내 데스크(3줄 요약)부터 들러요. 걷는 사람 표시가 둘러보는 순서를 따라 움직입니다.'
    return f'''<aside class="tw-panel" aria-label="{e(f["label"])} 가게 안내">
<p class="tw-co"><b>{e(COMPANY["ko"])}</b> {e(COMPANY["hq"])} · <span>{e(COMPANY["en"])}</span></p>
<div class="tw-fl"><span class="tw-badge" style="--c:{f["color"]}">{e(f["label"])}</span><div><h2>{e(f["dept"])}</h2><p class="tw-en">{e(f["en"])} · {e(f["branch"])}</p></div></div>
<p class="tw-ep"><b>{e(f["ep"])}</b> {e(f["title"])}</p>
<p class="tw-biz">{e(f["biz"])}</p>
<h3>이 가게 둘러보는 순서</h3>
<p class="tw-tip">{first}</p>
<ol class="tw-route">{_route_items(f)}</ol>
<nav class="tw-elev" aria-label="골목 — 가게 이동">{"".join(el)}</nav>
</aside>'''

def _panel_index(f, standalone=False):
    rows = []
    if standalone:
        rows.append(f'<li data-k="00" class="here"><a href="index.html"><span class="tw-badge" style="--c:{f["color"]}">입구</span><b>시장 입구 · 안내소</b><span>목차 · 경제학 원론 해설 쪽으로</span></a></li>')
    else:
        rows.append(f'<li data-k="00" class="here"><a href="#three"><span class="tw-badge" style="--c:{f["color"]}">입구</span><b>시장 입구 · 안내소</b><span>지금 계신 곳 · 이 목차 쪽</span></a></li>')
    for g in FLOORS[1:]:
        rows.append(f'<li data-k="{g["key"]}"><a href="{g["file"]}"><span class="tw-badge" style="--c:{g["color"]}">{e(g["label"])}</span><b>{e(g["dept"])}</b><span>{e(g["ep"])} · {e(g["title"])}</span></a></li>')
    clocks = ''.join(f'<span data-tz="{tz}"><b>{c}</b><i>--:--</i></span>' for c, tz in CLOCKS)
    return f'''<aside class="tw-panel" aria-label="가게 안내판">
<p class="tw-co"><b>{e(COMPANY["ko"])}</b> {e(COMPANY["hq"])} · <span>{e(COMPANY["en"])}</span></p>
<h2>가게 안내판</h2>
<p class="tw-biz">{e(COMPANY["motto"])}. 열한 강의실이 가게 하나씩을 쓰고, 북쪽 줄 끝 쉼터A와 남쪽 줄 끝 쉼터B에서 요약정리와 퀴즈를, 골목 끝 광장에서 실전 연습장을 봅니다. 시장의 가게를 누르거나 아래 안내판에서 골라 들어가세요.</p>
<div class="tw-clock" aria-label="세계 주요 시장 시각">{clocks}</div>
<ol class="tw-dir">{"".join(rows)}</ol>
<p class="tw-note">{e(COMPANY["note"])}</p>
</aside>'''

def tower_html(key, standalone=False):
    f = BYKEY[key]
    idx = key == 'lobby'
    panel = _panel_index(f, standalone) if idx else _panel_floor(f)
    tools = ('<button type="button" data-v="b" class="on">시장 전체</button><button type="button" data-v="spin" aria-pressed="true">자동 회전</button>' if idx else
             '<button type="button" data-v="b">시장 전체</button><button type="button" data-v="p" class="on">이 가게 평면</button>')
    hint = '드래그로 돌려 보고 가게를 누르면 안내 카드가 열려요' if idx else '방을 누르면 그 단계로 내려갑니다 · 드래그로 돌려 보기'
    cap = (f'{COMPANY["ko"]} 3D 모형: 시장 입구부터 골목 끝 광장까지 가게 15곳, 가게마다 한 강의실(장)' if idx else
           f'{COMPANY["ko"]} 3D 모형에서 {f["label"]} {f["dept"]}의 지붕을 걷어 보여 주는 가게 평면')
    data = json.dumps(_data(key, 'index.html' if standalone else ''), ensure_ascii=False).replace('</', '<\\/')
    imap = json.dumps({'imports': {'three': f'https://cdn.jsdelivr.net/npm/three@{THREE_VER}/build/three.module.js',
                                   'three/addons/': f'https://cdn.jsdelivr.net/npm/three@{THREE_VER}/examples/jsm/'}})
    return f'''<!--tower:start-->
<style>
{CSS}
</style>
<section class="tower{' tw-idx' if idx else ''}" id="tower" data-floor="{key}" aria-label="{e(COMPANY['ko'])} — 시장 안내">
<div class="tw-stage" role="img" aria-label="{e(cap)}">
<div class="tw-cv" aria-hidden="true"></div><div class="tw-labels" aria-hidden="true"></div>
<div class="tw-tools">{tools}</div>
<p class="tw-hint">{hint}</p>
<div class="tw-card" hidden></div>
<div class="tw-err" hidden>3D 시장을 불러오지 못했습니다(인터넷 연결 · WebGL 확인). 오른쪽 안내판으로 그대로 이동할 수 있어요.</div>
<div class="tw-load">시장을 여는 중…</div>
</div>
{panel}
</section>
<script type="application/json" id="towerData">{data}</script>
<script type="importmap">{imap}</script>
<script type="module">
{JS}
</script>
<!--tower:end-->
'''

NAV_LINK = '<a href="#tower">시장 안내</a>'
