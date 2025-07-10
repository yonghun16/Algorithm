import os
import re
from collections import defaultdict
import urllib.parse

MAX_COUNT = 30
OJ_LIST = ['boj', 'programmers', 'goorm', 'jol']

# ✅ 문제 루트 디렉토리 (수동으로 지정)
PROBLEM_ROOT = os.path.join('.', 'Online_Judge_Problems')

def parse_folder_name(folder_name):
    match = re.match(r'^(\w+)_(\d+)_([\w가-힣_]+)$', folder_name)
    if match:
        oj, number, title = match.groups()
        return oj, number, title
    return None

def extract_info_from_file(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith(('.c', '.java', '.cpp', '.py', '.js')):
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if not lines:
                        continue

                    content = "".join(lines[:20])

                    # 주석 블록 추출
                    if filename.endswith('.py'):
                        block = re.search(r"'''(.*?)'''", content, re.DOTALL)
                    else:  # C, C++, Java, JS
                        block = re.search(r"/\*(.*?)\*/", content, re.DOTALL)

                    if block:
                        comment_block = block.group(1)
                        level = re.search(r'Level\s*:\s*(.+)', comment_block)
                        tags = re.search(r'Tag\s*:\s*(.+)', comment_block)
                        link = re.search(r'Link\s*:\s*(.+)', comment_block)
                        return (
                            level.group(1).strip() if level else '',
                            tags.group(1).strip() if tags else '',
                            link.group(1).strip() if link else ''
                        )
    except Exception as e:
        print(f"오류 발생: {folder_path}: {e}")
    return '', '', ''

def collect_all_problems():
    all_problems = []

    for oj in OJ_LIST:
        oj_path = os.path.join(PROBLEM_ROOT, oj)
        if not os.path.isdir(oj_path):
            continue

        for folder in os.listdir(oj_path):
            folder_path = os.path.join(oj_path, folder)
            if not os.path.isdir(folder_path):
                continue

            parsed = parse_folder_name(folder)
            if parsed and parsed[0].lower() == oj.lower():
                mtime = os.path.getmtime(folder_path)
                level, tags, link = extract_info_from_file(folder_path)
                all_problems.append((parsed[0], parsed[1], parsed[2], level, tags, link, mtime))

    return all_problems

def write_readme(path, title, problems_by_oj):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n')
        f.write('최근에 해결한 온라인 저지 문제 목록입니다. \n\n**Online_Judge_Problems** 디렉토리에 문제 풀이 소스가 있습니다.\n\n')

        for oj, problems in problems_by_oj.items():
            if oj == 'boj':
                f.write(f'## 백준 온라인 저지\n\n')
                f.write('<p> <a href="https://solved.ac/profile/yonghun16"><img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=yonghun16" width="348em"></a> <a href="https://www.acmicpc.net/user/yonghun16"><img src="http://mazandi.herokuapp.com/api?handle=yonghun16&theme=warm" width="348em"></a> </p>\n\n')
            elif oj == 'programmers':
                f.write(f'## 프로그래머스\n\n')
                f.write('<img src="https://github.com/yonghun16/Algorithm/blob/main/Online_Judge_Problems/programmers/score.png" width="350em">\n\n')
            elif oj == 'goorm':
                f.write(f'## 구름\n\n')
                f.write('<img src="https://github.com/yonghun16/Algorithm/blob/main/Online_Judge_Problems/goorm/score.png">\n\n')

            f.write('| 온라인 저지 | 번호 | 제목 | 난이도 | 태그 | 풀이 |\n')
            f.write('|------|------|------|--------|------|------|\n')
            for oj, number, title, level, tags, link, _ in problems:
                visible_title = title.replace('_', ' ')
                encoded_title = urllib.parse.quote(title)
                f.write(f'| {oj} | {number} | [{visible_title}]({link}) | {level} | {tags} | [코드](https://github.com/yonghun16/Algorithm/tree/main/Online_Judge_Problems/{oj}/{oj}_{number}_{encoded_title}) |\n')
            f.write('\n')

def main():
    all_problems = collect_all_problems()

    problems_by_oj = defaultdict(list)
    for problem in all_problems:
        problems_by_oj[problem[0]].append(problem)

    for oj in problems_by_oj:
        problems_by_oj[oj] = sorted(problems_by_oj[oj], key=lambda x: x[6], reverse=True)[:MAX_COUNT]

    write_readme('README.md', f'알고리즘 문제 목록 (최근 {MAX_COUNT}개)', problems_by_oj)

if __name__ == '__main__':
    main()

