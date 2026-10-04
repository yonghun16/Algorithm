import os
import re
import urllib.parse
from collections import defaultdict
from html import escape

MAX_COUNT = 50
OJ_LIST = ["백준", "프로그래머스", "정올"]

SOURCE_EXTS = (".c", ".cpp", ".java", ".py", ".js", ".ts", ".rs")

# ---- 정올 배지 설정 ----
JUNGOL_ID = "yonghun16"
JUNGOL_PROFILE_URL = "https://jungol.co.kr/account/71256"
JUNGOL_BADGE_PATH = "jungol_badge.svg"

TIER_COLORS = {
    "Bronze": "#AD5600",
    "Silver": "#435F7A",
    "Gold": "#EC9A00",
    "Platinum": "#27E2A4",
    "Diamond": "#00B4FC",
    "Ruby": "#FF0062",
}
OTHER_COLOR = "#9AA0A6"


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
    .title {{ font: 700 15px 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; fill: #1F2937; }}
    .id {{ font: 400 12px 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; fill: #6B7280; }}
    .num {{ font: 700 26px 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; fill: #1F2937; }}
    .label {{ font: 400 12px 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; fill: #6B7280; }}
    .legend {{ font: 400 12px 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; fill: #374151; }}
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
            '| <img src="https://raw.githubusercontent.com/yonghun16/github-programmers-rank/master/lib/result.svg" width="380"/> '
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
    all_problems = collect_all_problems()

    # 배지는 최근 N개가 아니라 정올 전체 풀이 기준
    write_jungol_badge([p for p in all_problems if p[0] == "정올"])

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
