"""
온라인 저지 풀이 저장소의 README.md와 배지(SVG 2종)를 자동으로 만드는 스크립트.

[실행 방법]
    저장소 루트(온라인 저지 폴더들이 있는 곳)에서 실행합니다.
        python readme_gen.py

[프로그래머스 배지 설정]
    .env 파일 또는 환경변수에 아래 두 값을 넣으면 실제 기록으로 배지를 갱신합니다.
        PROGRAMMERS_ID=이메일
        PROGRAMMERS_PW=비밀번호
    값이 없거나 요청이 실패하면 기존 배지 파일을 그대로 둡니다.

[폴더 규칙]
    <온라인 저지>/<난이도>/<문제번호>_<제목>/ 구조를 따릅니다.
        예) 백준/Silver/1000_A+B/
    문제 폴더 안 소스 파일 상단 20줄에 아래 주석이 있으면 태그와 링크를 읽습니다.
        Tag  : 구현, 수학
        Link : https://www.acmicpc.net/problem/1000
"""

import http.cookiejar
import itertools
import json
import os
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html import escape

# ============================================================
# 설정
# ============================================================

# 온라인 저지 폴더 이름. README 섹션 순서도 이 리스트 순서를 따른다.
BAEKJOON = "백준"
JUNGOL = "정올"
PROGRAMMERS = "프로그래머스"
OJ_LIST = [BAEKJOON, JUNGOL, PROGRAMMERS]

MAX_COUNT = 50  # 온라인 저지별로 README에 보여줄 최근 문제 수
SOURCE_EXTS = (".c", ".cpp", ".java", ".py", ".js", ".ts", ".rs")
README_PATH = "README.md"
GITHUB_REPO_URL = "https://github.com/yonghun16/Algorithm"

FONT_STACK = (
    "'Segoe UI', Ubuntu, 'Helvetica Neue', 'Apple SD Gothic Neo', "
    "'Malgun Gothic', sans-serif"
)

# 정올 배지
JUNGOL_ID = "yonghun16"
JUNGOL_PROFILE_URL = "https://jungol.co.kr/account/71256"
JUNGOL_BADGE_PATH = "jungol_badge.svg"

# 백준(solved.ac) 배지 - README 표에만 쓰인다
SOLVED_AC_ID = "yonghun16"
SOLVED_AC_PROFILE_URL = f"https://solved.ac/profile/{SOLVED_AC_ID}"
SOLVED_AC_BADGE_URL = (
    f"http://mazassumnida.wtf/api/v2/generate_badge?boj={SOLVED_AC_ID}"
)

# 프로그래머스 배지
PROGRAMMERS_NAME = "yonghun16"
PROGRAMMERS_BADGE_PATH = "programmers_badge.svg"
PROGRAMMERS_SIGN_IN_URL = "https://programmers.co.kr/api/v1/account/sign-in"
PROGRAMMERS_RECORD_URL = "https://programmers.co.kr/api/v1/users/record"

# 난이도(티어)별 색. 난이도 폴더명의 첫 단어(예: "Silver 5" → "Silver")로 찾는다.
TIER_COLORS = {
    "Bronze": "#AD5600",
    "Silver": "#435F7A",
    "Gold": "#EC9A00",
    "Platinum": "#27E2A4",
    "Diamond": "#00B4FC",
    "Ruby": "#FF0062",
}
OTHER_COLOR = "#9AA0A6"


# ============================================================
# 데이터 모델
# ============================================================


@dataclass(frozen=True)
class Problem:
    """풀이 폴더 하나에서 읽어온 정보."""

    platform: str  # 온라인 저지 이름 (예: "백준")
    number: str  # 문제 번호 (예: "1000")
    title: str  # 폴더명에서 번호를 뺀 제목 (예: "A+B")
    level: str  # 난이도 폴더명 (예: "Silver 5")
    tags: str  # 소스 주석의 Tag 값
    link: str  # 소스 주석의 Link 값
    mtime: float  # 폴더 수정 시각 (최근순 정렬에 사용)


# ============================================================
# 공통 유틸
# ============================================================


def load_env_file(path: str = ".env") -> None:
    """python-dotenv 없이 .env 파일을 읽어 환경변수로 등록한다. 이미 있는 값은 유지한다."""
    if not os.path.isfile(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def write_text(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def parse_problem_folder(folder_name: str) -> tuple[str, str] | None:
    """'1000_A+B' 같은 폴더명을 (번호, 제목)으로 나눈다. 형식이 아니면 None."""
    match = re.match(r"^(\d+)_(.+)$", folder_name)
    if not match:
        return None
    number, title = match.groups()
    return number, title


def tier_of(level: str) -> str:
    """'Silver 5' → 'Silver'. 빈 문자열이면 ''."""
    words = level.split()
    return words[0].capitalize() if words else ""


def clean_comment_value(value: str) -> str:
    """
    주석에서 읽은 값의 앞뒤 공백과 블록 주석 닫는 기호(*/)를 제거한다.
    예) '/* Link : https://... */' → 'https://...'
    """
    return re.sub(r"\s*\*/\s*$", "", value).strip()


# ============================================================
# 1. 풀이 폴더 스캔
# ============================================================


def _subdirectories(path: str) -> list[str]:
    if not os.path.isdir(path):
        return []
    return [
        name
        for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name))
    ]


def read_metadata(folder_path: str) -> tuple[str, str]:
    """
    폴더 안 소스 파일 상단 20줄에서 Tag, Link 값을 찾는다.
    (tags, link) 를 돌려주며, 찾지 못하면 빈 문자열을 돌려준다.
    """
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if not (
                os.path.isfile(file_path) and filename.endswith(SOURCE_EXTS)
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                head = "".join(itertools.islice(f, 20))

            # 주석 기호(/* */, """, #)와 상관없이 본문에서 바로 찾는다.
            tag_match = re.search(r"Tag\s*:\s*(.+)", head)
            link_match = re.search(r"Link\s*:\s*(.+)", head)
            if tag_match or link_match:
                tags = (
                    clean_comment_value(tag_match.group(1))
                    if tag_match
                    else ""
                )
                link = (
                    clean_comment_value(link_match.group(1))
                    if link_match
                    else ""
                )
                return tags, link

    except (OSError, UnicodeDecodeError) as e:
        print(f"오류 발생: {folder_path}: {e}")

    return "", ""


def collect_problems() -> list[Problem]:
    """OJ_LIST 폴더 아래의 모든 풀이 폴더를 Problem 목록으로 만든다."""
    problems = []

    for platform in OJ_LIST:
        for level in _subdirectories(platform):
            level_path = os.path.join(platform, level)

            for folder in _subdirectories(level_path):
                parsed = parse_problem_folder(folder)
                if parsed is None:
                    continue

                number, title = parsed
                folder_path = os.path.join(level_path, folder)
                tags, link = read_metadata(folder_path)

                problems.append(
                    Problem(
                        platform=platform,
                        number=number,
                        title=title,
                        level=level,
                        tags=tags,
                        link=link,
                        mtime=os.path.getmtime(folder_path),
                    )
                )

    return problems


# ============================================================
# 2. 정올 배지 (난이도 분포 SVG)
# ============================================================


def jungol_badge_svg(problems: list[Problem]) -> str:
    """정올 풀이 수와 난이도 분포를 담은 SVG 문자열을 만든다."""
    total = len(problems)

    # 티어별 개수 집계
    counts = {tier: 0 for tier in TIER_COLORS}
    other = 0
    for p in problems:
        tier = tier_of(p.level)
        if tier in counts:
            counts[tier] += 1
        else:
            other += 1

    # 개수가 0보다 큰 티어만 막대와 범례에 표시
    segments = [
        (tier, n, TIER_COLORS[tier]) for tier, n in counts.items() if n > 0
    ]
    if other > 0:
        segments.append(("Other", other, OTHER_COLOR))

    # 레이아웃 상수
    width = 350
    pad = 20
    bar_y = 92
    bar_h = 12
    bar_w = width - pad * 2
    per_row = 3  # 범례 한 줄에 놓을 개수
    col_w = bar_w / per_row
    legend_y = bar_y + bar_h + 26
    rows = max(1, (len(segments) + per_row - 1) // per_row)
    height = legend_y + (rows - 1) * 22 + 22

    # 분포 막대 조각
    bar_parts = []
    if total == 0:
        bar_parts.append(
            f'<rect x="{pad}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="6" fill="#E5E7EB"/>'
        )
    else:
        x = pad
        for _, n, color in segments:
            w = bar_w * n / total
            bar_parts.append(
                f'<rect x="{x:.2f}" y="{bar_y}" width="{w:.2f}" height="{bar_h}" fill="{color}"/>'
            )
            x += w

    # 범례
    legend_parts = []
    for idx, (name, n, color) in enumerate(segments):
        lx = pad + (idx % per_row) * col_w
        ly = legend_y + (idx // per_row) * 22
        legend_parts.append(
            f'<circle cx="{lx + 5:.2f}" cy="{ly - 4}" r="5" fill="{color}"/>'
            f'<text x="{lx + 16:.2f}" y="{ly}" class="legend">{name} {n}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .title {{ font: 700 15px {FONT_STACK}; fill: #1F2937; }}
    .id {{ font: 400 12px {FONT_STACK}; fill: #6B7280; }}
    .num {{ font: 700 26px {FONT_STACK}; fill: #1F2937; }}
    .label {{ font: 400 12px {FONT_STACK}; fill: #6B7280; }}
    .legend {{ font: 400 12px {FONT_STACK}; fill: #374151; }}
  </style>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="#FFFFFF" stroke="#E5E7EB"/>
  <text x="{pad}" y="32" class="title">JUNGOL</text>
  <text x="{width - pad}" y="32" class="id" text-anchor="end">{escape(JUNGOL_ID)}</text>
  <text x="{pad}" y="72" class="num">{total}</text>
  <text x="{pad + 14 + len(str(total)) * 15}" y="72" class="label">solved</text>
  <clipPath id="bar"><rect x="{pad}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="6"/></clipPath>
  <g clip-path="url(#bar)">
    {"".join(bar_parts)}
  </g>
  {"".join(legend_parts)}
</svg>
"""


def write_jungol_badge(
    problems: list[Problem], path: str = JUNGOL_BADGE_PATH
) -> None:
    """정올 배지는 최근 N개가 아니라 정올 전체 풀이 기준으로 만든다."""
    write_text(path, jungol_badge_svg(problems))
    print("정올: 배지를 갱신했습니다.")


# ============================================================
# 3. 프로그래머스 배지 (기록 카드 SVG)
# ============================================================


def fetch_programmers_record(email: str, password: str) -> dict:
    """프로그래머스에 로그인한 뒤 내 기록(레벨/점수/푼 문제/랭킹)을 JSON으로 가져온다."""
    # 쿠키 저장소를 가진 opener로 로그인하면 이후 요청에 세션 쿠키가 자동으로 실린다.
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cookie_jar)
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    # 1) 로그인: 응답 쿠키가 cookie_jar에 저장된다.
    body = json.dumps({"user": {"email": email, "password": password}}).encode(
        "utf-8"
    )
    sign_in = urllib.request.Request(
        PROGRAMMERS_SIGN_IN_URL, data=body, headers=headers, method="POST"
    )
    with opener.open(sign_in, timeout=10) as res:
        res.read()

    # 2) 같은 세션으로 기록 조회
    record_req = urllib.request.Request(
        PROGRAMMERS_RECORD_URL, headers=headers
    )
    with opener.open(record_req, timeout=10) as res:
        return json.loads(res.read().decode("utf-8"))


def programmers_badge_svg(level, score, rank, solved) -> str:
    """프로그래머스 기록을 2x2 카드 형태의 SVG 문자열로 만든다."""
    cards = [
        ("정복 중인 레벨", f"{level}", "레벨"),
        ("현재 점수", f"{score:,}", ""),
        ("해결한 코딩 테스트", f"{solved:,}", "문제"),
        ("나의 랭킹", f"{rank:,}", "위"),
    ]

    # 레이아웃 상수
    width = 350
    pad = 20
    gap = 10
    top = 50
    cell_w = (width - pad * 2 - gap) / 2
    cell_h = 62
    height = top + cell_h * 2 + gap + pad

    card_parts = []
    for idx, (label, value, unit) in enumerate(cards):
        cx = pad + (idx % 2) * (cell_w + gap)
        cy = top + (idx // 2) * (cell_h + gap)
        unit_part = (
            f'<tspan class="unit" dx="4">{unit}</tspan>' if unit else ""
        )
        card_parts.append(
            f'<rect x="{cx:.2f}" y="{cy}" width="{cell_w:.2f}" height="{cell_h}" rx="8" fill="#ECF5FF"/>'
            f'<text x="{cx + 14:.2f}" y="{cy + 22}" class="label">{label}</text>'
            f'<text x="{cx + 14:.2f}" y="{cy + 50}" class="value">{value}{unit_part}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .title {{ font: 700 15px {FONT_STACK}; fill: #1F2937; }}
    .id {{ font: 400 12px {FONT_STACK}; fill: #6B7280; }}
    .label {{ font: 700 12px {FONT_STACK}; fill: #0078FF; }}
    .value {{ font: 700 22px {FONT_STACK}; fill: #1F2937; }}
    .unit {{ font: 700 12px {FONT_STACK}; fill: #374151; }}
  </style>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="#FFFFFF" stroke="#E5E7EB"/>
  <text x="{pad}" y="32" class="title">PROGRAMMERS</text>
  <text x="{width - pad}" y="32" class="id" text-anchor="end">{escape(PROGRAMMERS_NAME)}</text>
  {"".join(card_parts)}
</svg>
"""


def write_programmers_badge(path: str = PROGRAMMERS_BADGE_PATH) -> None:
    """
    실행 시점의 프로그래머스 기록으로 배지를 갱신한다.
    로그인 정보가 없거나 요청이 실패하면 기존 배지 파일을 그대로 둔다.
    """
    email = os.environ.get("PROGRAMMERS_ID")
    password = os.environ.get("PROGRAMMERS_PW")
    if not email or not password:
        print(
            "프로그래머스: PROGRAMMERS_ID / PROGRAMMERS_PW 가 없어 배지 갱신을 건너뜁니다."
        )
        return

    try:
        record = fetch_programmers_record(email, password)
        svg = programmers_badge_svg(
            level=record["skillCheck"]["level"],
            score=record["ranking"]["score"],
            rank=record["ranking"]["rank"],
            solved=record["codingTest"]["solved"],
        )
    except Exception as e:  # 네트워크 오류, 응답 형식 변경 모두 포함
        print(
            f"프로그래머스: 기록을 가져오지 못해 기존 배지를 유지합니다. ({e})"
        )
        return

    write_text(path, svg)
    print("프로그래머스: 배지를 갱신했습니다.")


# ============================================================
# 4. README 생성
# ============================================================

# README 상단의 배지 표. 세 열 순서는 OJ_LIST 순서와 맞춘다.
BADGE_TABLE = (
    "| 백준 (Solved.ac) | 정올 (JUNGOL) | 프로그래머스 (Programmers) |\n"
    "| :---: | :---: | :---: |\n"
    f'| <a href="{SOLVED_AC_PROFILE_URL}"><img src="{SOLVED_AC_BADGE_URL}" width="330"/></a> '
    f'| <a href="{JUNGOL_PROFILE_URL}"><img src="{JUNGOL_BADGE_PATH}" width="330"/></a> '
    f'| <img src="{PROGRAMMERS_BADGE_PATH}" width="330"/> |\n\n'
)


def _problem_row(problem: Problem) -> str:
    visible_title = problem.title.replace("_", " ")
    code_url = (
        f"{GITHUB_REPO_URL}/tree/main/"
        f"{urllib.parse.quote(problem.platform)}/"
        f"{urllib.parse.quote(problem.level)}/"
        f"{problem.number}_{urllib.parse.quote(problem.title)}"
    )
    # 링크가 없으면 제목만 보여 준다 (빈 링크 [제목]() 방지)
    title_cell = (
        f"[{visible_title}]({problem.link})" if problem.link else visible_title
    )
    return (
        f"| {problem.platform} | {problem.number} | "
        f"{title_cell} | {problem.level} | {problem.tags} | "
        f"[코드]({code_url}) |\n"
    )


def build_readme(problems_by_oj: dict[str, list[Problem]]) -> str:
    """README 전체 내용을 문자열로 만든다. 문제가 없는 온라인 저지 섹션은 생략한다."""
    parts = [
        f"# 알고리즘 문제 목록 (최근 {MAX_COUNT}개)\n\n",
        "최근에 해결한 온라인 저지 문제 목록입니다.\n\n"
        "**백준**, **프로그래머스**, **정올** 디렉토리에 문제 풀이 소스가 있습니다.\n\n",
        BADGE_TABLE,
    ]

    for oj in OJ_LIST:
        problems = problems_by_oj.get(oj)
        if not problems:
            continue

        parts.append(f"## {oj}\n\n")
        parts.append("| 온라인 저지 | 번호 | 문제 | 난이도 | 태그 | 풀이 |\n")
        parts.append("|------|------|------|--------|------|------|\n")
        parts.extend(_problem_row(p) for p in problems)
        parts.append("\n")

    return "".join(parts)


def write_readme(path: str, problems_by_oj: dict[str, list[Problem]]) -> None:
    write_text(path, build_readme(problems_by_oj))


# ============================================================
# 실행
# ============================================================


def main() -> None:
    load_env_file()

    problems = collect_problems()

    # 배지
    write_jungol_badge([p for p in problems if p.platform == JUNGOL])
    write_programmers_badge()

    # README: 온라인 저지별로 최근 수정순 MAX_COUNT개
    problems_by_oj = {}
    for oj in OJ_LIST:
        recent_first = sorted(
            (p for p in problems if p.platform == oj),
            key=lambda p: p.mtime,
            reverse=True,
        )
        problems_by_oj[oj] = recent_first[:MAX_COUNT]

    write_readme(README_PATH, problems_by_oj)


if __name__ == "__main__":
    main()
