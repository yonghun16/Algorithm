import http.cookiejar
import json
import os
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from html import escape

MAX_COUNT = 50
OJ_LIST = ["백준", "프로그래머스", "정올"]

SOURCE_EXTS = (".c", ".cpp", ".java", ".py", ".js", ".ts", ".rs")

FONT_STACK = "'Segoe UI', Ubuntu, 'Helvetica Neue', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif"

# ---- 정올 배지 설정 ----
JUNGOL_ID = "yonghun16"
JUNGOL_PROFILE_URL = "https://jungol.co.kr/account/71256"
JUNGOL_BADGE_PATH = "jungol_badge.svg"

# ---- 프로그래머스 배지 설정 ----
# 로그인 정보는 환경변수(또는 .env 파일)에서 읽음
#   PROGRAMMERS_ID=이메일
#   PROGRAMMERS_PW=비밀번호
PROGRAMMERS_NAME = "yonghun16"
PROGRAMMERS_BADGE_PATH = "programmers_badge.svg"
PROGRAMMERS_SIGN_IN_URL = "https://programmers.co.kr/api/v1/account/sign-in"
PROGRAMMERS_RECORD_URL = "https://programmers.co.kr/api/v1/users/record"

TIER_COLORS = {
    "Bronze": "#AD5600",
    "Silver": "#435F7A",
    "Gold": "#EC9A00",
    "Platinum": "#27E2A4",
    "Diamond": "#00B4FC",
    "Ruby": "#FF0062",
}
OTHER_COLOR = "#9AA0A6"


def load_env_file(path=".env"):
    """python-dotenv 없이 .env 파일을 읽어 환경변수로 등록 (이미 있는 값은 유지)."""
    if not os.path.isfile(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(
                key.strip(), value.strip().strip('"').strip("'")
            )


def parse_problem_folder(folder_name):
    """
    문제 폴더명 예시
    - 1000_A+B
    - 178871_달리기_경주
    - 5545_연필_공장
    """
    match = re.match(r"^(\d+)_(.+)$", folder_name)
    if match:
        number, title = match.groups()
        return number, title
    return None


def extract_info_from_file(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and filename.endswith(SOURCE_EXTS):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = "".join(f.readlines()[:20])

                # 주석 형식(/* */, """ """, #)과 상관없이 상단 20줄에서 바로 찾음
                tags = re.search(r"Tag\s*:\s*(.+)", content)
                link = re.search(r"Link\s*:\s*(.+)", content)

                if tags or link:
                    return (
                        tags.group(1).strip() if tags else "",
                        link.group(1).strip() if link else "",
                    )

    except Exception as e:
        print(f"오류 발생: {folder_path}: {e}")

    return "", ""


def collect_all_problems():
    all_problems = []

    for platform in OJ_LIST:
        if not os.path.isdir(platform):
            continue

        # Gold, Silver, Bronze, 1, 2, 3 ...
        for level in os.listdir(platform):
            level_path = os.path.join(platform, level)

            if not os.path.isdir(level_path):
                continue

            # 문제 폴더
            for folder in os.listdir(level_path):
                folder_path = os.path.join(level_path, folder)

                if not os.path.isdir(folder_path):
                    continue

                parsed = parse_problem_folder(folder)
                if not parsed:
                    continue

                number, title = parsed

                tags, link = extract_info_from_file(folder_path)
                mtime = os.path.getmtime(folder_path)

                all_problems.append(
                    (
                        platform,
                        number,
                        title,
                        level,
                        tags,
                        link,
                        mtime,
                    )
                )

    return all_problems


def write_jungol_badge(problems, path=JUNGOL_BADGE_PATH):
    """정올 폴더의 풀이 기록으로 '푼 문제 수 + 난이도 분포' SVG 배지를 만든다."""
    total = len(problems)

    # 난이도 폴더명(예: "Silver 5")의 첫 단어로 티어 분류
    counts = {tier: 0 for tier in TIER_COLORS}
    other = 0
    for p in problems:
        level = p[3]
        tier = level.split()[0].capitalize() if level.strip() else ""
        if tier in counts:
            counts[tier] += 1
        else:
            other += 1

    items = [(t, n, TIER_COLORS[t]) for t, n in counts.items() if n > 0]
    if other > 0:
        items.append(("Other", other, OTHER_COLOR))

    # 레이아웃
    width = 350
    pad = 20
    bar_y = 92
    bar_h = 12
    bar_w = width - pad * 2
    per_row = 3
    col_w = bar_w / per_row
    legend_y = bar_y + bar_h + 26
    rows = max(1, (len(items) + per_row - 1) // per_row)
    height = legend_y + (rows - 1) * 22 + 22

    # 분포 막대
    bar_parts = []
    if total == 0:
        bar_parts.append(
            f'<rect x="{pad}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="6" fill="#E5E7EB"/>'
        )
    else:
        x = pad
        for _, n, color in items:
            w = bar_w * n / total
            bar_parts.append(
                f'<rect x="{x:.2f}" y="{bar_y}" width="{w:.2f}" height="{bar_h}" fill="{color}"/>'
            )
            x += w

    # 범례
    legend_parts = []
    for idx, (name, n, color) in enumerate(items):
        lx = pad + (idx % per_row) * col_w
        ly = legend_y + (idx // per_row) * 22
        legend_parts.append(
            f'<circle cx="{lx + 5:.2f}" cy="{ly - 4}" r="5" fill="{color}"/>'
            f'<text x="{lx + 16:.2f}" y="{ly}" class="legend">{name} {n}</text>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
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
    {''.join(bar_parts)}
  </g>
  {''.join(legend_parts)}
</svg>
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)


def fetch_programmers_record(email, password):
    """프로그래머스에 로그인한 뒤 내 기록(레벨/점수/푼 문제/랭킹)을 가져온다."""
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(jar)
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    # 1) 로그인 → 세션 쿠키가 jar에 저장됨
    body = json.dumps({"user": {"email": email, "password": password}}).encode(
        "utf-8"
    )
    req = urllib.request.Request(
        PROGRAMMERS_SIGN_IN_URL, data=body, headers=headers, method="POST"
    )
    with opener.open(req, timeout=10) as res:
        res.read()

    # 2) 같은 쿠키로 기록 조회
    req = urllib.request.Request(PROGRAMMERS_RECORD_URL, headers=headers)
    with opener.open(req, timeout=10) as res:
        return json.loads(res.read().decode("utf-8"))


def write_programmers_badge(path=PROGRAMMERS_BADGE_PATH):
    """
    프로그래머스 기록으로 2x2 카드 형태의 SVG 배지를 만든다.
    로그인 정보가 없거나 요청이 실패하면 기존 SVG를 그대로 둔다.
    """
    email = os.environ.get("PROGRAMMERS_ID")
    password = os.environ.get("PROGRAMMERS_PW")
    if not email or not password:
        print(
            "프로그래머스: PROGRAMMERS_ID / PROGRAMMERS_PW 가 없어 배지 갱신을 건너뜁니다."
        )
        return

    try:
        data = fetch_programmers_record(email, password)
        level = data["skillCheck"]["level"]
        score = data["ranking"]["score"]
        rank = data["ranking"]["rank"]
        solved = data["codingTest"]["solved"]
    except Exception as e:
        print(
            f"프로그래머스: 기록을 가져오지 못해 기존 배지를 유지합니다. ({e})"
        )
        return

    cards = [
        ("정복 중인 레벨", f"{level}", "레벨"),
        ("현재 점수", f"{score:,}", ""),
        ("해결한 코딩 테스트", f"{solved:,}", "문제"),
        ("나의 랭킹", f"{rank:,}", "위"),
    ]

    # 레이아웃
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

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
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
  {''.join(card_parts)}
</svg>
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("프로그래머스: 배지를 갱신했습니다.")


def write_readme(path, title, problems_by_oj):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(
            "최근에 해결한 온라인 저지 문제 목록입니다.\n\n"
            "**백준**, **프로그래머스**, **정올** 디렉토리에 문제 풀이 소스가 있습니다.\n\n"
        )

        f.write(
            "| 백준 (Solved.ac) | 프로그래머스 (Programmers) | 정올 (JUNGOL) |\n"
            "| :---: | :---: | :---: |\n"
            '| <a href="https://solved.ac/profile/yonghun16"><img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=yonghun16" width="330"/></a> '
            f'| <img src="{PROGRAMMERS_BADGE_PATH}" width="330"/> '
            f'| <a href="{JUNGOL_PROFILE_URL}"><img src="{JUNGOL_BADGE_PATH}" width="330"/></a> |\n\n'
        )

        # OJ_LIST 순서대로 섹션 출력
        for oj in OJ_LIST:
            problems = problems_by_oj.get(oj)
            if not problems:
                continue

            f.write(f"## {oj}\n\n")

            f.write("| 온라인 저지 | 번호 | 문제 | 난이도 | 태그 | 풀이 |\n")
            f.write("|------|------|------|--------|------|------|\n")

            for oj_name, number, title, level, tags, link, _ in problems:
                visible_title = title.replace("_", " ")
                encoded_title = urllib.parse.quote(title)
                encoded_oj = urllib.parse.quote(oj_name)
                encoded_level = urllib.parse.quote(level)

                f.write(
                    f"| {oj_name} | {number} | [{visible_title}]({link}) | {level} | {tags} | "
                    f"[코드](https://github.com/yonghun16/Algorithm/tree/main/{encoded_oj}/{encoded_level}/{number}_{encoded_title}) |\n"
                )

            f.write("\n")


def main():
    load_env_file()

    all_problems = collect_all_problems()

    # 배지는 최근 N개가 아니라 정올 전체 풀이 기준
    write_jungol_badge([p for p in all_problems if p[0] == "정올"])

    # 프로그래머스 배지는 실행 시점의 사이트 기록 기준
    write_programmers_badge()

    problems_by_oj = defaultdict(list)

    for problem in all_problems:
        problems_by_oj[problem[0]].append(problem)

    for oj in problems_by_oj:
        problems_by_oj[oj] = sorted(
            problems_by_oj[oj],
            key=lambda x: x[6],
            reverse=True,
        )[:MAX_COUNT]

    write_readme(
        "README.md",
        f"알고리즘 문제 목록 (최근 {MAX_COUNT}개)",
        problems_by_oj,
    )


if __name__ == "__main__":
    main()
