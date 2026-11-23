#!/usr/bin/env python3
"""Genspark 요청 꾸러미 생성: docs/genspark/ (요청문·체크리스트) + docs/IMG_PROMPTS_all.md + 배포용 zip.
사용: python3 make_genspark_pack.py <fruitfly-lab-expressions 경로> [zip 출력 경로]"""
import os, sys, shutil, zipfile, subprocess
B = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(B))
CHR = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/adminmrobo/fruitfly-lab-expressions')
ZIP = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'docs', 'genspark_pack.zip')

STYLE = ('16-bit SNES-era RPG pixel art, crisp hard-edged pixels on a clear pixel grid (draw at 480x270 logical pixels, then scale 4x with no smoothing), '
         'limited bright palette, bright DAYTIME university lecture room with a PURE WHITE background wall, big windows with soft daylight, '
         'a white board at the front, light wooden desks in rows. Composition 16:9 (1920x1080). '
         'ABSOLUTELY NO text, letters, numbers, logos or signatures anywhere (keep boards, screens, signs blank or use simple icons).')
CAST = {
 'doctor': 'the PROFESSOR: spiky black hair with one white streak, small ponytail, teal rectangular glasses, white lab coat over black vest and tie',
 'haru': 'HARU (student): long pink hair with navy-blue streaks and two buns, blue eyes, lavender hoodie under a white lab coat',
 'fruitfly': 'the FRUIT-FLY TA: black fruit-fly body, big red compound eyes, blue round helmet with pink and blue tubes, white lab coat, clear wings',
 'jupanbot': 'the ABACUS-ROBOT TA: beige boxy CRT-monitor head with a green smiling face and a small antenna, gray arms, holds a brown wooden abacus, tank treads',
 'sia': 'SIA (student): long straight black hair, black maid-style dress with white frills and a gray bow',
 'moa': 'MOA (student): long light-brown hair, white frilled headband with ribbon, red plaid bow, tan cardigan over white blouse',
 'x1': 'X1 (back-row student): fully black cute silhouette, white dot eyes, pink cheeks, pink hair bow and ponytail',
 'x2': 'X2 (back-row student): fully black cute silhouette, black beret, round teal glasses, white dot eyes',
 'x3': 'X3 (back-row student): fully black cute silhouette in a cat-ear hood with two yellow pom-pom strings',
}
ALL = list(CAST)
def cast(keys): return 'Characters (match the attached reference sheet EXACTLY, same faces, hair, outfits): ' + '; '.join(CAST[k] for k in keys) + '.'
# key, 제목, 등장인물, 장면(행동·소품), 표정 메모
COVERS = [
 ('idx', '목차 — 경제학 원론 연구실', ALL, 'the whole class posing together in front of the white board like a class photo; the professor in the center, the two TAs on both sides, three students in front, three silhouettes peeking from the back row; through the window a stadium-shaped school building in sunshine', '모두 밝게 웃는 단체 사진'),
 ('01', 'CH01 경제학의 10대 원리', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'x1'], 'the professor points at a single last slice of cake under a glass dome on the desk (scarcity); Haru weighs a dumbbell in one hand and a coin in the other (opportunity cost); the robot TA happily holds a stack of coins, the fruit-fly TA raises one finger in doubt', '하루는 고민하는 얼굴'),
 ('02', 'CH02 경제학자처럼 생각하기', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'sia'], 'a toy globe and a plastic body model on the desk; on the board a simple curve bowing outward between a tiny computer icon and a tiny car icon; the robot TA pushes toy cars, the fruit-fly TA traces the curve with a pointer', '시아가 곡선을 관찰'),
 ('03', 'CH03 수요와 공급', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'moa'], 'two crossing straight lines (one blue going down, one red going up) on the board meeting at a glowing green dot; a stack of vinyl records on one side, a small crowd of tiny figurines with raised hands on the other; tug-of-war rope on the floor', '균형점에 모두 시선 집중'),
 ('04', 'CH04 탄력성과 그 응용', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'x2'], 'a giant stretched rubber band between two posts on the desk; a sports drink bottle and an ice cream cone; the robot TA pulls the band hard and looks surprised, the fruit-fly TA measures it with a ruler', '주판봇은 놀란 얼굴'),
 ('05', 'CH05 수요·공급과 정부정책', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'sia', 'moa'], 'a small stadium ticket-booth model with a long queue of tiny figurines; a velvet rope barrier drawn as a horizontal orange line across the board lines; an ice-cream cart with a blank price tag; the professor holds a small gavel', '줄 서기 장면이 보이게'),
 ('05m', '중간 요약정리 및 퀴즈', ['doctor', 'haru', 'moa', 'x1', 'fruitfly', 'jupanbot'], 'a bright review lounge: five closed binders in a row, blank quiz cards pinned on a cork board, a small score board with empty colored bars; Moa holds a clipboard like a referee, students cheering', '응원하는 분위기'),
 ('06', 'CH06 소비자·생산자·시장의 효율성', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'sia'], 'an auction gavel and a blank vinyl record cover on the desk; a paint bucket and brush; on the board a green triangle above a horizontal line and a blue triangle below it, glowing softly', '하루가 경매 팻말을 듦(글자 없음)'),
 ('07', 'CH07 조세의 경제적 비용', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'x3'], 'a wooden wedge stuck between two crossing lines on the board with a small red triangle beside it; a hill-shaped curve next to it; a coin jar; the robot TA happily drops coins into the jar while the fruit-fly TA points at the red triangle', '주판봇이 이긴 판: 주판봇 기뻐함, 초파리 한숨'),
 ('08', 'CH08 시장구조 — 경쟁·독점·과점', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'moa'], 'on the desk: one big shop model facing many tiny identical shop models; two small water wells with buckets; a 2x2 floor grid of four colored tiles; the robot TA secretly carries an extra bucket of water behind his back', '주판봇이 몰래 더 퍼 가는 장면'),
 ('09', 'CH09 시장실패와 정부의 역할', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'sia', 'x1'], 'a small factory model puffing gray smoke toward a laundry line; a little park with a bench and tree; on the board a sagging curve under a diagonal line; the fruit-fly TA holds a small blank tag tied to the factory chimney', '공원 앞에서 함께 고민'),
 ('10', 'CH10 국민경제와 경기변동', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'x2'], 'a large wall dashboard with three blank round gauges (needles only); a sweet potato crate and a soy milk carton crate on the desk; a seesaw model; the robot TA holds up a very tall bar while the fruit-fly TA holds a shorter one', '계기판을 올려다봄'),
 ('11', 'CH11 정부의 경제정책', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'moa'], 'a central-bank style control panel with two big round knobs (one blue, one orange) and a level gauge; a small bridge construction model; the robot TA cranks one knob all the way, the fruit-fly TA turns both knobs a little', '초파리가 두 손잡이를 조금씩'),
 ('11f', '기말 요약정리 및 퀴즈', ['doctor', 'haru', 'sia', 'x3', 'fruitfly', 'jupanbot'], 'a sunny review lounge with six closed binders, blank quiz cards on a cork board, an open door at the back glowing toward a rooftop stadium; Sia raises a small starting flag (no text)', '마지막 응원'),
 ('prac', '마지막 장 · 실전 연습장', ['doctor', 'haru', 'fruitfly', 'jupanbot', 'x2'], 'ROOFTOP mini stadium under blue sky (keep it bright and white-toned): four small booths: a ticket booth, a sports shoe shop, a city-hall desk with a tiny factory model, a central-bank desk with two knobs; characters running each booth', '각자 부스를 운영'),
]
TITLE = {k: t for k, t, *_ in COVERS}
CONV = [('대화 1 — 그림체 확정', ['idx']), ('대화 2', ['01', '02', '03', '04']), ('대화 3', ['05', '05m', '06']), ('대화 4', ['07', '08', '09', '10']), ('대화 5', ['11', '11f', 'prac'])]

def prompt(k):
    _, t, who, scene, memo = next(c for c in COVERS if c[0] == k)
    return f'{STYLE} {cast(who)} Scene: {scene}. Mood: cheerful, clean, educational, everyone clearly visible, no one cut off at the edges.'

def write_docs(out):
    os.makedirs(out, exist_ok=True)
    R = ['# Genspark 요청문 — 경제학 원론 연구실 표지 15장', '',
         '## 순서', '',
         '1. **대화 1**을 먼저 엽니다. `refs/` 폴더의 `cast_sheet.png`와 캐릭터 9장을 모두 올리고 목차 표지 1장을 받습니다.',
         '2. 그림체(픽셀 크기, 흰 배경, 캐릭터 얼굴)가 마음에 들 때까지 대화 1에서 다시 그립니다.',
         '3. 확정한 목차 표지(`cover_idx.png`)를 **대화 2~5에 참고 그림으로 함께** 올립니다. 대화 하나에 3~4장, 모두 16:9입니다.',
         '4. 받은 그림은 `체크리스트.md`의 이름으로 저장하고, 저장소의 `src/build/covers_in/`에 넣은 뒤 `python3 src/build/import_covers.py`를 실행합니다(픽셀 격자를 찾아 NEAREST 정수배로 1920×1080 무손실 WebP로 바꿉니다).', '',
         '## 공통 주의', '', '- 그림 안에 글자·숫자·로고가 들어가면 다시 요청합니다("remove all text").', '- 캐릭터 얼굴·머리·옷이 참고 그림과 다르면 "match the reference sheet exactly"로 다시 요청합니다.', '- 흐릿하게(매끄럽게) 나오면 "hard-edged pixels, no anti-aliasing"을 덧붙입니다.', '']
    for name, ks in CONV:
        R += [f'## {name} ({len(ks)}장)', '', '첨부: `refs/cast_sheet.png` + 캐릭터 9장' + (' + 확정한 `cover_idx.png`' if ks != ['idx'] else ''), '']
        if ks != ['idx']:
            R += ['첫 메시지 맨 앞에 붙일 문장:', '', '```', 'Use the attached cover_idx.png as the STYLE REFERENCE (same pixel size, palette, white daytime classroom, same character designs). Make the following images one by one, 16:9 each.', '```', '']
        for k in ks:
            R += [f'### cover_{k} — {TITLE[k]}', '', '```', prompt(k), '```', '']
    open(os.path.join(out, '요청문.md'), 'w', encoding='utf-8').write('\n'.join(R))
    C = ['# 저장 이름 체크리스트', '', '| ☐ | 대화 | 저장 이름 | 쪽 | 표정·장면 확인 |', '|---|---|---|---|---|']
    for name, ks in CONV:
        for k in ks:
            memo = next(c for c in COVERS if c[0] == k)[4]
            C.append(f'| ☐ | {name.split(" —")[0]} | `cover_{k}.png` | {TITLE[k]} | {memo} |')
    C += ['', '받은 뒤 점검: ① 글자 없음 ② 흰 배경·낮 ③ 캐릭터 얼굴이 참고 그림과 같음 ④ 4배 확대해도 픽셀 경계가 또렷함 ⑤ 등장인물이 잘리지 않음']
    open(os.path.join(out, '체크리스트.md'), 'w', encoding='utf-8').write('\n'.join(C))
    P = ['# 그림 지시문 모음 — 경제학 원론 연구실 (Genspark용)', '', '표지 15장. 16비트 RPG 픽셀아트, 낮의 강의실(흰 배경). 대화별 순서와 첨부 목록은 `docs/genspark/요청문.md`에 있습니다.', '']
    for k, t, *_ in COVERS:
        P += [f'## cover_{k} — {t}', '', '```', prompt(k), '```', '']
    open(os.path.join(ROOT, 'docs', 'IMG_PROMPTS_all.md'), 'w', encoding='utf-8').write('\n'.join(P))

def make_refs(dst):
    os.makedirs(dst, exist_ok=True)
    names = {'doctor': '박사', 'haru': '하루', 'fruitfly': '초파리', 'jupanbot': '주판봇', 'sia': '시아', 'moa': '모아', 'x1': 'X1', 'x2': 'X2', 'x3': 'X3'}
    files = []
    for k in CAST:
        s = os.path.join(CHR, 'images', k, 'E13_neutral.png'); d = os.path.join(dst, f'ref_{k}.png'); shutil.copy(s, d); files.append(d)
    subprocess.run(['montage', *files, '-tile', '5x2', '-geometry', '360x360+10+10', '-background', 'white', os.path.join(dst, 'cast_sheet.png')], check=True)

if __name__ == '__main__':
    out = os.path.join(ROOT, 'docs', 'genspark'); write_docs(out)
    tmp = '/tmp/genspark_pack'; shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    make_refs(os.path.join(tmp, 'refs'))
    for f in ('요청문.md', '체크리스트.md'): shutil.copy(os.path.join(out, f), tmp)
    with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(tmp):
            for f in fs: p = os.path.join(r, f); z.write(p, os.path.join('경제학원론연구실_genspark', os.path.relpath(p, tmp)))
    print(ZIP, os.path.getsize(ZIP) // 1024, 'KB')
