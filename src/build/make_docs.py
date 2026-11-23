#!/usr/bin/env python3
"""docs/AUDIT_REPORT.md(원자료와 다르게 쓴 곳) · docs/IMG_PROMPTS_all.md(표지 그림 지시문) 생성."""
import os, sys, re, importlib.util
B = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(B)); PG = os.path.join(ROOT, 'src', 'pages')
sys.path.insert(0, PG)
def load(f):
    spec = importlib.util.spec_from_file_location('p', os.path.join(PG, f)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.P
strip = lambda s: re.sub('<[^>]+>', '', s)
pages = [load(f) for f in sorted(os.listdir(PG)) if f.startswith('p') and f.endswith('.py')]
os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True)
L = ['# 감사보고서 — 원자료와 다르게 쓴 곳', '', '경제학 원론 연구실 v1.0 · 2026-11-23 · 글 안상선', '',
     '주 자료: 「생활 속의 경제학」 강의노트(2025-2학기, 중간고사 범위), 「경제학의 이해」 기말고사 자료집(2025-2학기). 보충: 「미시경제원론 강의노트 4강(2)」(2015), 「현대경제학원론 강의노트 — 미시편」.', '',
     '원칙: 뜻이 불분명하거나 틀린 표현은 "원자료의 A를 이 페이지에서는 B로 바꿉니다" 형식으로 바꾸고, 각 쪽 바닥글에도 같은 문장을 적었습니다. 모든 예시값은 다시 계산했습니다.', '']
n = 0
for P in pages:
    if not P.get('changes'): continue
    L += [f'## {strip(P["title"])}', '', f'- 파일: `{P["file"]}`']
    for c in P['changes']:
        n += 1; L.append(f'- [{n:02d}] {strip(c)}')
    L.append('')
L += ['## 검산 기록', '', '- CH01 기회비용 1억 + 300만 × 12 = 1억3,600만 원, 경제적 이윤 −600만 원.', '- CH03 9 − 2P = 1 + 2P → P* = 2, Q* = 5. 수요 −4 → P* = 1, Q* = 3. 보충 예제 150 − P = 20 + 8P → P ≈ 14.44.',
      '- CH04 (80 − 100)/100 ÷ (1000 − 500)/500 = −0.2 → 0.2. 중간점 0.333.', '- CH05 아이스크림 세금 $0.5 → 구매자 $3.30, 판매자 $2.80, 거래량 100 → 90(반응 100/3, 50으로 재구성).',
      '- CH06 경매 1장 80달러 CS 20, 2장 70달러 CS 40. 페인트 1채 600달러 PS 100, 2채 800달러 PS 500.', '- CH07 P = 100 − Q, P = 20 + Q, t = 20 → Q 30, 세수 600, 사중손실 100. t = 40 → 800, 400.',
      '- CH08 P = 100 − 7.5Q, MC = 5Q → Q = 5 이윤 250, Q = 8 이윤 160(원자료 그림의 결과와 일치하도록 재구성). 우물 30·30 → 1,800씩, 40·30 → 2,000/1,500, 40·40 → 1,600씩.',
      '- CH10 명목 GDP 2012 = 50×3 + 10×2 = 170, 실질 = 50×2 + 10×1 = 110, 디플레이터 154.5, 실질 성장률 12.2%.', '- CH11 승수 1/(1 − 0.6) = 2.5, 지출 4조 구축 40% → +6조.', '']
open(os.path.join(ROOT, 'docs', 'AUDIT_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(L))

# 그림 지시문(docs/IMG_PROMPTS_all.md)은 make_genspark_pack.py가 만든다.
print('audit items', n)
