import os
import re
import urllib.parse
from collections import defaultdict

MAX_COUNT = 50
OJ_LIST = ["백준", "프로그래머스", "정올"]

SOURCE_EXTS = (".c", ".cpp", ".java", ".py", ".js", ".ts", ".rs")


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


def write_readme(path, title, problems_by_oj):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(
            "최근에 해결한 온라인 저지 문제 목록입니다.\n\n"
            "**백준**, **프로그래머스**, **정올** 디렉토리에 문제 풀이 소스가 있습니다.\n\n"
        )

        f.write(
            "| 백준 (Solved.ac) | 프로그래머스 (Programmers) |\n"
            "| :---: | :---: |\n"
            '| <a href="https://solved.ac/profile/yonghun16"><img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=yonghun16" width="330"/></a> | <img src="https://raw.githubusercontent.com/yonghun16/github-programmers-rank/master/lib/result.svg" width="380"/> |\n\n'
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
