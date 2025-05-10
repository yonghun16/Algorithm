import os
import re

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

def collect_problems_in_directory(oj_dir):
    """저지 폴더 내 문제 목록 수집"""
    problems = []

    if not os.path.isdir(oj_dir):
        return problems

    for folder in os.listdir(oj_dir):
        folder_path = os.path.join(oj_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        parsed = parse_folder_name(folder)
        if parsed and parsed[0].lower() == oj_dir.lower():
            mtime = os.path.getmtime(folder_path)
            level, tags, link = extract_info_from_file(folder_path)
            problems.append((parsed[0], parsed[1], parsed[2], level, tags, link, mtime))
    
    return problems

def write_readme(path, title, problems):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n')
        f.write('| 온라인 저지 | 번호 | 제목 | 난이도 | 태그 | 링크 |\n')
        f.write('|-------------|------|------|--------|------|------|\n')
        for oj, number, title, level, tags, link, _ in problems:
            f.write(f'| {oj} | {number} | {title} | {level} | {tags} | [바로가기]({link}) |\n')

def main():
    all_problems = []

    for oj in OJ_LIST:
        problems = collect_problems_in_directory(oj)

        # 개별 README 생성
        problems_sorted = sorted(problems, key=lambda x: x[6], reverse=True)[:MAX_COUNT]
        readme_path = os.path.join(oj, 'README.md')
        write_readme(readme_path, f'{oj} 문제 목록 (최근 {MAX_COUNT}개)', problems_sorted)

        # 통합용 문제 수집
        all_problems.extend(problems)

    # 통합 README 생성
    all_problems_sorted = sorted(all_problems, key=lambda x: x[6], reverse=True)[:MAX_COUNT]
    write_readme('README.md', f'통합 문제 목록 (최근 {MAX_COUNT}개)', all_problems_sorted)

if __name__ == '__main__':
    main()
