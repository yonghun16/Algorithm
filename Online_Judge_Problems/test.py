import os
import re
from collections import defaultdict

MAX_COUNT = 50
OJ_LIST = ['BOJ', 'Goorm', 'JOL', 'Programmers']

def parse_folder_name(folder_name):
    match = re.match(r'^(\w+)_(\d+)_([\w가-힣_]+)$', folder_name)
    if match:
        oj, number, title = match.groups()
        return oj, number, title.replace('_', ' ')
    return None

def extract_info_from_file(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith(('.py', '.txt', '.cpp', '.js', '.java')):
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if lines and lines[0].startswith("'''") and "Level" in "".join(lines[:10]):
                        block = "".join(lines[:10])
                        level = re.search(r'Level\s*:\s*(.+)', block)
                        tags = re.search(r'Tag\s*:\s*(.+)', block)
                        link = re.search(r'Link\s*:\s*(.+)', block)
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
        oj_path = os.path.join('.', oj)
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
        
        for oj, problems in problems_by_oj.items():
            f.write(f'## {oj}\n\n')
            f.write('| 번호 | 제목 | 난이도 | 태그 | 링크 |\n')
            f.write('|------|------|--------|------|------|\n')
            for _, number, title, level, tags, link, _ in problems:
                f.write(f'| {number} | {title} | {level} | {tags} | [바로가기]({link}) |\n')
            f.write('\n')

def main():
    all_problems = collect_all_problems()

    # 각 온라인 저지별로 정렬 후 50개 선택
    problems_by_oj = defaultdict(list)
    for problem in all_problems:
        problems_by_oj[problem[0]].append(problem)

    # 각 온라인 저지별로 최대 50개 문제를 선택
    for oj in problems_by_oj:
        problems_by_oj[oj] = sorted(problems_by_oj[oj], key=lambda x: x[6], reverse=True)[:MAX_COUNT]

    write_readme('README.md', f'문제 목록 (온라인 저지 별 {MAX_COUNT}개)', problems_by_oj)

if __name__ == '__main__':
    main()
