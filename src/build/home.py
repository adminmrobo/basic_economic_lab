# -*- coding: utf-8 -*-
"""목차(index) 첫 화면 = 경제학 원론 해설 + 시장 보기 썸네일.

- index.html : 표지 → 머리말(미시경제학 설명) → 미시경제학이란 → 목차 카드 → 시장으로 둘러보기(썸네일) → …
- tower.html : 생활경제 시장 3D(시장 전체 · 가게 안내판)를 따로 보는 쪽
build_extra.index() 와 patch_home.py(이미 빌드된 index.html 고치기)가 함께 쓴다.
"""
import base64, html, re, json
import tower

e = html.escape
strip = lambda s: re.sub('<[^>]+>', '', s)
DATE = '2026-11-23'
WHO_PAGE = 'https://adminmrobo.github.io/who_am_i/who_am_i.html'

LEAD = ('<b>경제학</b>은 한정된 자원(희소성) 안에서 사람·기업·정부가 무엇을 고르고, 그 선택이 시장에서 만나 <b>가격</b>과 <b>거래량</b>, '
        '나아가 나라 전체의 <b>생산·물가·고용</b>을 어떻게 정하는지 다룹니다. 이 강의는 1부(CH01~CH05)에서 선택의 원리·수요와 공급·탄력성·가격규제와 세금을, '
        '2부(CH06~CH11)에서 시장의 효율성·조세의 비용·시장구조·시장실패와 재정·국민경제와 경기변동·재정정책과 통화정책을 다룹니다. '
        'CH05와 CH11 뒤에는 요약정리와 퀴즈가, 마지막에는 경기장 매표소부터 중앙은행까지 네 곳을 운영해 보는 실전 연습장이 있어요.')
BASIS = ('본 강의는 <b>한국체육대학교 교양과정</b>의 「경제학의 이해」, 「생활 속의 경제학」 강의노트를 기반으로 제작됐습니다. '
         '중간고사 범위는 「생활 속의 경제학」(2025-2학기) 강의노트, 기말고사 범위는 「경제학의 이해」(2025-2학기) 자료집을 뼈대로 하고, '
         '부족한 부분은 저자의 「미시경제원론 강의노트 4강(2)」(2015)와 「현대경제학원론 강의노트 — 미시편」으로 보충했습니다.')

def byline():
    return (f'<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{WHO_PAGE}" target="_blank" rel="noopener">저자 소개</a>'
            f' · {DATE} 처음 공개</p>'
            f'<p class="basis">{BASIS}</p>')

# ---------- 시장 썸네일 (픽셀풍 SVG) ----------
def tower_svg(w=192, h=108):
    """16비트 RPG 픽셀아트 느낌의 생활경제 시장 그림. 가게 차양 색은 tower.FLOORS 와 같다."""
    r = []
    R = lambda x, y, ww, hh, c: r.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{c}"/>')
    R(0, 0, 192, 108, '#f3f7fd'); R(0, 56, 192, 44, '#e8f0fb')
    for cx, cy in ((22, 12), (150, 8), (110, 18)):
        R(cx, cy, 14, 3, '#ffffff'); R(cx + 3, cy - 2, 7, 2, '#ffffff')
    R(0, 100, 192, 8, '#a9c48a'); R(0, 100, 192, 1, '#8fb070')
    # 아케이드 지붕(반원 느낌 계단형)
    for i, (dy, ww) in enumerate(((0, 128), (2, 132), (4, 136))):
        R(16 - i * 2, 30 + dy, ww, 2, '#c9d8ec')
    R(14, 36, 136, 2, '#9aa8be')
    for x in range(18, 150, 18): R(x, 30, 1, 8, '#9aa8be')
    # 가게 일곱 곳이 늘어선 앞줄(북쪽 줄) — 차양 줄무늬 + 간판 + 진열대
    north = [f for f in tower.FLOORS if f['key'] in ('lobby', '01', '02', '03', '04', '05', '05m')]
    sx, sw = 16, 19
    for i, f in enumerate(north):
        x = sx + i * sw
        R(x, 40, sw - 1, 58, '#f4ecdc')                    # 가게 몸체
        R(x + 2, 42, sw - 5, 6, f['color']); R(x + 3, 44, sw - 7, 2, '#ffffff')   # 간판
        for k in range(0, sw - 1, 4):                       # 줄무늬 차양
            R(x + k, 50, 2, 6, f['color']); R(x + k + 2, 50, 2, 6, '#ffffff')
        R(x, 56, sw - 1, 1, '#00000022')
        R(x + 3, 84, sw - 7, 10, '#d9c7a6'); R(x + 3, 84, sw - 7, 1, '#b8a382')  # 진열대
        for k, c in enumerate(('#d23f2c', '#f3c969', '#6fae84')): R(x + 4 + k * 4, 81, 3, 3, c)
    # 시장 문(왼쪽)
    R(6, 34, 3, 66, '#8f5f00'); R(6, 26, 30, 6, '#8f5f00'); R(8, 27, 26, 4, '#f3c969')
    r.append('<text x="21" y="30.4" font-size="4.2" font-family="monospace" font-weight="700" text-anchor="middle" fill="#8f5f00">MARKET</text>')
    # 골목 끝 광장 경기장(오른쪽)
    R(156, 72, 34, 4, '#dfe5ee'); R(154, 76, 38, 20, '#dfe5ee'); R(158, 78, 30, 14, '#8fcf9f'); R(172, 78, 1, 14, '#ffffff')
    R(156, 96, 34, 4, '#c9d1de'); R(164, 62, 18, 7, '#138a52')
    r.append('<text x="173" y="67.4" font-size="4.2" font-family="monospace" font-weight="700" text-anchor="middle" fill="#ffffff">PLAZA</text>')
    # 나무 · 사람
    for tx in (146, 186):
        R(tx + 2, 96, 2, 4, '#7a5530'); R(tx, 90, 6, 6, '#3f8f4e')
    for px, c in ((40, '#d0457f'), (92, '#3f5fa8'), (120, '#138a52')):
        R(px, 95, 2, 2, '#f1c9a5'); R(px, 97, 2, 3, c)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 108" width="{w}" height="{h}" shape-rendering="crispEdges" '
            f'role="img" aria-label="픽셀 그림: 시장 문으로 들어가 줄무늬 차양 가게들이 늘어선 골목 끝에 광장 경기장이 있는 {e(tower.COMPANY["ko"])}">' + ''.join(r) + '</svg>')

def tower_svg_uri():
    return 'data:image/svg+xml;base64,' + base64.b64encode(tower_svg().encode('utf-8')).decode()

# ---------- CSS ----------
CSS = '''
.th-tower{background-image:url(%s);image-rendering:pixelated}
.ihero .byline{font-size:14px;color:var(--muted);margin:0}
.ihero .basis{font-size:14px;margin:0;padding:10px 14px;border-left:4px solid var(--seq);background:rgba(63,95,168,.07);border-radius:0 10px 10px 0}
.ihero .lead2{color:var(--text);max-width:68ch}
.mosaic .mt.bld{outline:2px solid var(--seq);outline-offset:-2px}
.mosaic .mt.bld span{background:var(--seq);color:#fff}
.bys{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;counter-reset:bys}
.bys>div{position:relative;background:var(--panel);border:1px solid var(--rule);border-radius:12px;padding:18px 18px 16px;display:flex;flex-direction:column;gap:6px}
.bys>div b{font-size:17px}
.bys>div .en{font-size:12px;color:var(--muted);letter-spacing:.02em}
.bys>div:nth-child(1){border-top:4px solid var(--seq)}
.bys>div:nth-child(2){border-top:4px solid var(--amber)}
.bys>div:nth-child(3){border-top:4px solid var(--gfp)}
.byfx{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px;font-weight:700;font-size:clamp(16px,2.2vw,21px);padding:16px;border:1px dashed var(--rule);border-radius:12px;background:#fff}
.byfx span{padding:6px 12px;border-radius:8px}
.byfx .p{background:rgba(63,95,168,.10);color:var(--seq)}.byfx .l{background:rgba(183,120,0,.12);color:var(--amber)}.byfx .q{background:rgba(19,138,82,.12);color:var(--gfp)}
.byfx i{font-style:normal;color:var(--muted)}
.bylab{background:var(--panel);border:1px solid var(--rule);border-radius:12px;padding:18px;display:flex;flex-direction:column;gap:12px}
.bylab .row{display:flex;flex-wrap:wrap;gap:10px 22px;align-items:center}
.bylab label{display:flex;align-items:center;gap:8px;font-size:14px;flex:1 1 220px}
.bylab label input{flex:1}
.bylab output{min-width:42px;font-weight:700;text-align:right}
.bymeter{position:relative;height:30px;border-radius:8px;background:#fff;border:1px solid var(--rule);overflow:hidden}
.bymeter i{position:absolute;left:0;top:0;bottom:0;background:linear-gradient(90deg,var(--gfp),#2fb37a);transition:width .35s}
.bymeter b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:14px}
.byhist{display:flex;flex-wrap:wrap;gap:6px;font-size:13px}
.byhist span{padding:3px 8px;border-radius:6px;background:#fff;border:1px solid var(--rule)}
.byhist span.up{border-color:rgba(19,138,82,.5)}.byhist span.dn{border-color:rgba(210,63,44,.5)}
.chapx{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.chapx a{display:flex;flex-direction:column;gap:6px;background:var(--panel);border:1px solid var(--rule);border-radius:12px;padding:16px;color:var(--text);text-decoration:none;min-width:0}
.chapx a:hover{border-color:var(--seq);box-shadow:0 4px 12px rgba(30,35,60,.10)}
.chapx a .ct{display:block;aspect-ratio:16/9;margin:-16px -16px 8px;border-radius:11px 11px 0 0;background-size:cover;background-position:center;border-bottom:1px solid var(--rule)}
.chapx a>b{color:var(--seq);font-size:13px}
.chapx a>strong{font-size:16px;line-height:1.35}
.chapx a>small{color:var(--muted)}
.chapx a ol{margin:2px 0 0;padding-left:20px;font-size:14px;color:var(--text)}
.chapx a ol li.duel{list-style:none;margin-left:-20px;color:var(--c-fly)}
.chapx a.review{border-color:rgba(183,120,0,.55);background:rgba(183,120,0,.06)}
.chapx a.review>b{color:var(--amber)}
.bldcard{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:22px;align-items:center;background:linear-gradient(180deg,#eef3fb,#fff);border:1px solid var(--rule);border-radius:14px;padding:18px;color:var(--text);text-decoration:none}
.bldcard:hover{border-color:var(--seq);box-shadow:0 6px 16px rgba(30,35,60,.12)}
.bldcard .pic{border-radius:10px;overflow:hidden;border:1px solid var(--rule);background:#f3f7fd}
.bldcard .pic svg{display:block;width:100%;height:auto;image-rendering:pixelated}
.bldcard h3{margin:0 0 6px}
.bldcard ul{margin:8px 0 12px;padding-left:20px;font-size:15px}
.bldcard .go{display:inline-block;background:var(--seq);color:#fff;font-weight:700;padding:9px 16px;border-radius:9px}
@media (max-width:860px){.bys,.chapx{grid-template-columns:repeat(2,minmax(0,1fr))}.bldcard{grid-template-columns:1fr}}
@media (max-width:520px){.bys,.chapx{grid-template-columns:1fr}}
'''

def css():
    return '<style>' + CSS.replace('url(%s)', 'url(' + tower_svg_uri() + ')', 1) + '</style>'

# ---------- 미시경제학이란 ----------
LAB_JS = ""

def micro_section(say):
    """say(who, mood, text) -> html (캐릭터 대사)."""
    talk = (say('doc', 'front', '경제학의 질문은 늘 같아요. "무엇이 부족한가(희소성)? 그래서 무엇을 포기하나(기회비용)? 그 선택들이 만나면 가격은 어디서 멈추나?"')
            + say('fly', 'point', '숫자 하나를 들으면 "무엇을 고정했나, 한 단위 더 하면 무엇이 늘고 주나"부터 묻는 거야. 조교로서 하는 첫 잔소리.')
            + say('robo', 'coin', '난 크고 높은 숫자가 좋은데… 일단 아래 실험부터 돌려 볼게!')
            + say('asst', 'smile', '맨 앞자리 하루예요. 아래 대시보드에서 수요·원가·세금 슬라이더를 하나씩만 움직여 보세요. 그림의 면적과 막대가 함께 바뀌어요.')
            + say('x1', 'wow', '뒷자리 X1이에요. ▶ 재생을 누르니 세금이 오르면서 빨간 삼각형이 점점 커져요!'))
    rows = [('다루는 대상', '한 사람·한 기업·한 시장의 선택과 가격', '나라 전체의 생산(GDP)·물가·실업·금리'),
            ('대표 질문', '이 가격에 몇 개를 살까·팔까? 세금은 누가 낼까?', '경기는 왜 오르내릴까? 정부와 중앙은행은 무엇을 할까?'),
            ('핵심 도구', '수요·공급, 탄력성, 잉여', '총수요·총공급, 실업률·물가지수, 재정·통화정책'),
            ('이 강의에서', 'CH01~CH09 (CH09는 재정학: 외부효과·공공재·분배)', 'CH10~CH11 (국민경제·경기변동·경제정책)')]
    tb = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    return f"""<section class="level" id="micro"><div class="wrap stack">
<div class="lvhead"><h2>경제학 원론이란? — 희소성 → 선택 → 시장 → 나라 경제</h2><p class="lead">경제학은 "부족한 것을 어떻게 나눌까"를 숫자로 다뤄요. 한 사람의 선택에서 시작해 시장의 가격, 정부의 세금과 규제, 나라 전체의 경기까지 같은 원리로 이어집니다. 세 가지 재료만 알면 됩니다.</p></div>
<div class="bys">
<div><span class="en">① SCARCITY · 희소성</span><b>무엇이 부족할까</b><p>시간·돈·자원은 원하는 만큼 많지 않아요. 그래서 무엇을 얼마나 만들고, 어떻게 만들고, 누구에게 나눌지 골라야 해요.</p></div>
<div><span class="en">② CHOICE · 선택</span><b>무엇을 포기할까</b><p>하나를 고르면 다른 것을 포기해요(기회비용). 한 단위 더 할 때의 편익과 비용을 비교하고(한계), 사람들은 유인에 반응해요.</p></div>
<div><span class="en">③ MARKET · 시장과 정부</span><b>어디서 멈출까</b><p>사려는 양과 팔려는 양이 같아지는 곳에서 가격이 멈춰요(균형). 시장이 실패하거나 경기가 흔들리면 정부가 세금·지출·금리로 개입해요.</p></div>
</div>
<div class="byfx" aria-label="경제학을 말로 쓴 식"><span class="p">희소성</span><i>→</i><span class="l">선택(기회비용)</span><i>→</i><span class="q">시장 균형</span><i>→</i><span class="p">정책과 나라 경제</span></div>
<details open class="more"><summary>수식으로 보면</summary><p style="margin:10px 0 0">시장균형: 수요량 Q<sub>d</sub>(P) = 공급량 Q<sub>s</sub>(P)를 만족하는 가격 P*. 예) Q<sub>d</sub> = 150 − P, Q<sub>s</sub> = 20 + 8P → 9P = 130, P* ≈ 14.4, Q* ≈ 135.6. 나라 경제: 총수요 AD = C + I + G + NX. 자세한 풀이는 <a href="03_supply_demand.html">CH03 수요와 공급</a>과 <a href="11_economic_policy.html">CH11 정부의 경제정책</a>에 있어요.</p></details>
<div class="talk">{talk}</div>
<div class="dash panel" data-dash="mk" id="mclab" aria-label="직접 해 보기: 수요·원가·세금을 바꿔 시장 균형 보기 대시보드"></div>
<h3>미시경제학과 거시경제학</h3>
<div class="tw"><table class="tb"><tr><th></th><th>미시경제학</th><th>거시경제학</th></tr>{tb}</table></div>
<p class="muted" style="font-size:14px">둘은 같은 경제를 다른 배율로 보는 두 렌즈예요. 미시 부분을 더 깊이 보려면 <a href="https://adminmrobo.github.io/micro_economics/" target="_blank" rel="noopener">미시경제학 연구실</a>로 이어집니다.</p>
</div></section>
{LAB_JS}"""

# ---------- 목차 카드 ----------
def chl(n): return f'CH{n}'
MID = ['01', '02', '03', '04', '05']; FIN = ['06', '07', '08', '09', '10', '11']; CHS = MID + FIN
def toc_section(L):
    def card(n):
        Q = L[n]
        topic = Q['short_title']
        lis = ''.join(f'<li>{e(strip(l["title"]))}</li>' for l in Q['levels'])
        lis += f'<li class="duel">⚔ 조교 대결: {e(strip(Q["duel"]["question"]))}</li>'
        return (f'<a href="{Q["file"]}"><span class="ct th-{n}" aria-hidden="true"></span><b>{chl(n)} · {e(topic)}</b>'
                f'<strong>{e(strip(Q["title"]))}</strong><small>{e(strip(Q["question"]))}</small><ol>{lis}</ol></a>')
    def rv(k, f, t, items, label='요약 · 퀴즈'):
        lis = ''.join(f'<li>{x}</li>' for x in items)
        return f'<a class="review" href="{f}"><span class="ct th-{k}" aria-hidden="true"></span><b>{label}</b><strong>{t}</strong><ol>{lis}</ol></a>'
    p1 = ''.join(card(n) for n in MID) + rv('05m', '05m_midterm_review.html', '중간 요약정리 및 퀴즈 (CH01~CH05)', ['장별 요약정리', '원자료 확인 문제 25문항', '생활 계산 문제 5개', '장별 점수'])
    p2 = ''.join(card(n) for n in FIN) + rv('11f', '11f_final_review.html', '기말 요약정리 및 퀴즈 (CH06~CH11)', ['장별 요약정리', '원자료 확인 문제 30문항', '생활 계산 문제 6개', '장별 점수'])
    p3 = rv('prac', 'practice/index.html', '마지막 장 · 실전 연습장', ['경기장 매표소 — 수요·공급·가격상한', '스포츠용품점 — 탄력성·매출', '시청 정책실 — 세금·외부효과', '중앙은행 상황실 — 경기와 정책'], '시뮬레이터')
    steps = ('<div class="steps"><div><b>이런 분께</b><p>뉴스에서 "기준금리·실업률·최저임금·세금"을 듣지만, 그것이 내 생활과 어떻게 이어지는지 숫자로 보고 싶은 분. 수식을 몰라도 됩니다.</p></div>'
             '<div><b>읽는 순서</b><p>CH01 → CH11 순서가 기본이에요. 앞 장의 한계가 다음 장의 이유가 되도록 이어 두었어요. 시험 대비라면 중간·기말 정리 쪽부터 봐도 됩니다.</p></div>'
             '<div><b>시장으로 둘러보기</b><p>장마다 가상의 「생활경제 시장」의 가게 하나(강의실)가 됩니다. 아래 <a href="#building">시장 보기</a>에서 3D 시장과 가게 안내판으로 장을 골라도 돼요.</p></div></div>')
    return (f'<section class="level" id="map"><div class="wrap stack"><div class="lvhead"><h2>목차</h2><p class="lead">11장과 요약·퀴즈 두 쪽, 그리고 마지막 장 실전 연습장입니다. 카드마다 그 장에서 다루는 세 가지 주제와 조교 대결 질문을 적어 두었어요.</p></div>'
            f'<h3>1부 · 생활 속의 경제학 — 선택의 원리에서 정부정책까지 (CH01~CH05, 중간고사 범위)</h3><div class="chapx">{p1}</div>'
            f'<h3>2부 · 경제학의 이해 — 시장의 효율성에서 경제정책까지 (CH06~CH11, 기말고사 범위)</h3><div class="chapx">{p2}</div>'
            f'<h3>마지막 장</h3><div class="chapx">{p3}</div>{steps}</div></section>')

def building_section():
    return f"""<section class="level" id="building"><div class="wrap stack">
<div class="lvhead"><h2>시장으로 둘러보기 — 생활경제 시장</h2><p class="lead">같은 열네 쪽을 시장 골목으로도 볼 수 있어요. 가상의 강의 시장 「생활경제 시장」에서 장 하나가 강의실 하나, 강의실 하나가 가게 하나입니다. 수요와 공급이 만나는 곳이 시장이니까요.</p></div>
<a class="bldcard" href="tower.html"><div class="pic">{tower_svg(384, 216)}</div><div><h3>시장 보기 — 3D 생활경제 시장</h3><p class="muted" style="margin:0">시장 문 안내소부터 골목 끝 광장 실전 연습장까지 15곳</p><ul><li>시장을 드래그로 돌려 보고, 가게를 누르면 강의실(장) 안내 카드가 열려요.</li><li>가게 안내판에서 바로 그 가게로 들어갈 수 있어요.</li><li>각 장 쪽 맨 위에서는 그 가게의 지붕을 걷어 가게 평면과 둘러보는 순서를 보여 줘요.</li></ul><span class="go">건물 보기 →</span></div></a>
</div></section>"""

def mosaic_tile():
    return '<a class="mt th-tower bld" href="tower.html" title="시장 보기 · 생활경제 시장"><span>시장</span><i class="sr">시장 보기 · 생활경제 시장 3D</i></a>'

def practice_tile():
    return '<a class="mt th-prac" href="practice/index.html" title="마지막 장 · 실전 연습장"><span>실전</span><i class="sr">마지막 장 · 실전 연습장</i></a>'

THUMB_KEYS = CHS + ['05m', '11f', 'idx', 'prac']

NAV = [('micro', '경제학 원론이란'), ('map', '목차'), ('building', '시장 보기'), ('keys', '한 줄 핵심'), ('dash', '종합 대시보드'), ('path', '개념 흐름'), ('how', '식구·사용법'), ('about', '자료와 원칙')]

def nav_html(label):
    a = ''.join(f'<a href="{"tower.html" if i == "building" else "#" + i}">{e(t)}</a>' for i, t in NAV)
    return f'<nav class="top" aria-label="섹션 바로가기"><div class="wrap"><a class="logo" href="index.html"><i></i>{e(label)}</a><div class="links">{a}</div></div></nav>\n'

# ---------- 시장 보기 쪽(tower.html) ----------
def tower_page(base_css, site):
    blk = tower.tower_html('lobby', standalone=True)
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>시장 보기 — 생활경제 시장 · 경제학 원론 연구실</title>
<meta name="description" content="경제학 원론 연구실 열네 쪽과 실전 연습장을 가상의 강의 시장 「생활경제 시장」의 가게 15곳으로 둘러보는 3D 시장 안내.">
<meta property="og:title" content="시장 보기 — 생활경제 시장">
<meta property="og:image" content="{site}assets/og/cover_idx.jpg">
<meta property="og:url" content="{site}tower.html">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M8 0l7 4v8l-7 4-7-4V4z' fill='%239ab0d0'/%3E%3C/svg%3E">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap">
<style>
{base_css}
</style>
</head>
<body>
<nav class="top" aria-label="바로가기"><div class="wrap"><a class="logo" href="index.html"><i></i>경제학 원론 연구실</a><div class="links"><a href="index.html">← 목차</a><a href="index.html#map">장 목록</a><a href="01_ten_principles.html">CH01부터</a></div></div></nav>
{blk}
<section class="level"><div class="wrap stack">
<div class="lvhead"><h2>이 시장은</h2><p class="lead">{e(tower.COMPANY["motto"])}. 「경제학 원론 연구실」 11장이 11개 가게로, 쉼터A와 쉼터B가 중간·기말 요약정리 및 퀴즈로, 골목 끝 광장이 실전 연습장으로 들어 있어요. 본 강의는 한국체육대학교 교양과정 「경제학의 이해」, 「생활 속의 경제학」 강의노트를 기반으로 제작됐습니다. 층을 누르거나 오른쪽 안내판에서 골라 올라가세요.</p></div>
<p class="muted" style="font-size:14px">{e(tower.COMPANY["note"])} 3D는 three.js(jsdelivr CDN)로 그립니다. 불러오지 못하면 안내판만으로 그대로 이동할 수 있어요.</p>
<p><a href="index.html">← 목차로 돌아가기</a></p>
</div></section>
<footer id="footer"><div class="wrap stack"><p>글 · 안상선 ((주)M-Robo 대표) · <a href="{WHO_PAGE}" target="_blank" rel="noopener">저자 소개</a> · <a href="https://github.com/adminmrobo/basic_economic_lab" target="_blank" rel="noopener">GitHub 저장소</a><br>캐릭터 이름·설정·그림의 저작권은 안상선(개인)에게 있으며 허락 없이 쓸 수 없습니다.</p></div></footer>
</body>
</html>
"""
