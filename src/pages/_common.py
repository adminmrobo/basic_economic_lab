CHT = {1: '경제학의 10대 원리', 2: '경제학자처럼 생각하기', 3: '수요와 공급', 4: '탄력성과 그 응용', 5: '수요·공급과 정부정책',
       6: '소비자·생산자·시장의 효율성', 7: '조세의 경제적 비용', 8: '시장구조 — 경쟁·독점·과점', 9: '시장실패와 정부의 역할', 10: '국민경제와 경기변동', 11: '정부의 경제정책'}
AU = [{'family': '안', 'given': '상선'}]
def _r(id, typ, title, year, role, note, url='', venue=''):
    r = {'id': id, 'type': typ, 'title': title, 'author': AU, 'issued': {'date-parts': [[year]]},
         'lab': {'work': f'lab:work/{id}', 'role': role, 'verified': {'title': True, 'authors': True, 'year': True, 'venue': False}, 'checkedBy': '업로드 원본 PDF 대조', 'note': note}}
    if url: r['URL'] = url
    if venue: r['container-title'] = venue
    return r
MID = _r('ahn2025life', 'manuscript', '생활 속의 경제학 강의노트 (2025-2학기, 제1장~제7장)', 2025, 'primary', '한국체육대학교 교양과정 강의노트. 중간고사 범위의 주 자료')
FIN = _r('ahn2025understand', 'manuscript', '경제학의 이해 기말고사 자료집 (2025-2학기)', 2025, 'primary', '한국체육대학교 교양과정 「경제학의 이해」 자료집. 기말고사 범위의 주 자료(시장실패·조세·거시·정책 슬라이드와 제7~9장 노트)')
SUP1 = _r('ahn2015micro4', 'manuscript', '미시경제원론 강의노트 제4장 시장의 수요와 공급(2/2)', 2015, 'background', '균형·균형의 변화 부분을 보충')
SUP2 = _r('eucalyon_modern', 'manuscript', '현대경제학원론 강의노트 — 미시편', 2010, 'background', '탄력도·조세 귀착·가격통제·시장이론 정의를 보충. 작성 연도는 확인 필요')
SUP2['author'] = [{'literal': 'eucalyon'}]; SUP2['lab']['verified']['authors'] = False; SUP2['lab']['verified']['year'] = False
MANKIW = {'id': 'mankiw_principles', 'type': 'book', 'title': 'Principles of Economics', 'author': [{'family': 'Mankiw', 'given': 'N. Gregory'}], 'issued': {'date-parts': [[2021]]},
          'container-title': 'Cengage', 'lab': {'work': 'lab:work/mankiw_principles', 'role': 'background', 'verified': {'title': True, 'authors': True, 'year': False, 'venue': True}, 'checkedBy': '강의노트 예시(음반 경매·페인트칠·우물·아이스크림 세금) 출처 확인', 'note': '강의노트가 따르는 원론 교과서. 본문을 옮기지 않음. 판 차이 있음'}}
def REFS(n):
    base = [MID] if n <= 5 else [FIN]
    return base + ([SUP1] if n == 3 else []) + ([SUP2] if n in (3, 4, 5, 6, 7, 8) else []) + [MANKIW]
SRC_MID = '안상선 (2025). 「생활 속의 경제학」 강의노트(2025-2학기). 한국체육대학교 교양과정. 이 페이지의 주 자료.'
SRC_FIN = '안상선 (2025). 「경제학의 이해」 기말고사 자료집(2025-2학기). 한국체육대학교 교양과정. 이 페이지의 주 자료.'
SRC_SUP1 = '안상선 (2015). 미시경제원론 강의노트 제4장(2/2). 균형과 균형의 변화 보충.'
SRC_SUP2 = '현대경제학원론 강의노트 — 미시편(eucalyon). 탄력도·조세 귀착·가격통제 정의 보충.'
SRC_MK = 'Mankiw, N. G. Principles of Economics. Cengage. 강의노트 예시의 원 교과서(본문을 옮기지 않음).'
def PN(n):
    files = {1: '01_ten_principles.html', 2: '02_think_like_economist.html', 3: '03_supply_demand.html', 4: '04_elasticity.html', 5: '05_government_policy.html', 6: '06_market_efficiency.html',
             7: '07_cost_of_taxation.html', 8: '08_market_structure.html', 9: '09_market_failure.html', 10: '10_macro_economy.html', 11: '11_economic_policy.html'}
    seq = [None] + [(files[i], f'CH{i:02d} {CHT[i]}') for i in range(1, 12)]
    prev = seq[n - 1] if n > 1 else None
    nxt = seq[n + 1] if n < 11 else None
    if n == 5: nxt = ('05m_midterm_review.html', '중간 요약정리 및 퀴즈')
    if n == 6: prev = ('05m_midterm_review.html', '중간 요약정리 및 퀴즈')
    if n == 11: nxt = ('11f_final_review.html', '기말 요약정리 및 퀴즈')
    return dict(prev=prev, next=nxt)
def fix(P):
    for l in P['levels']:
        if l.get('math'): l['math']['try'] = l['math'].pop('try_')
    P.update(PN(int(P['num'])))
    return P
