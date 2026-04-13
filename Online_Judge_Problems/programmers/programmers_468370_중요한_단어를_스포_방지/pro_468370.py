"""
-----------------------------------------------------------
Sub    : [Programmers] 스포일러 방지
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/468370
Level  : Kakao
Tag    : Python, String, Implementation
-----------------------------------------------------------
Details
1. 단어 추출 및 인덱스 범위 계산
2. 스포일러 구간과 겹치는 단어 판별
3. 중요 단어 조건 필터링 (일반 구간 미등장 & 중복 아님)
-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


def get_input_data():
    raw_data = sys.stdin.read().splitlines()

    if not raw_data:
        return None, None

    message = raw_data[0].strip().strip('"')

    spoiler_ranges = []
    for line in raw_data[1:]:
        if line.strip():
            clean_line = (
                line.replace("[", "").replace("]", "").replace(",", " ")
            )
            parts = list(map(int, clean_line.split()))
            if len(parts) == 2:
                spoiler_ranges.append(parts)

    return message, spoiler_ranges


def solution(message, spoiler_ranges):
    if message is None:
        return 0

    # 1. 메시지 내 모든 단어와 위치 파악
    words_info = []
    start = 0
    # 마지막 단어 처리를 위해 임시로 공백 추가
    temp_message = message + " "
    for i, char in enumerate(temp_message):
        if char == " ":
            if start < i:
                words_info.append(
                    {"word": message[start:i], "range": (start, i - 1)}
                )
            start = i + 1

    # 2. 스포일러 단어 판별 및 일반 단어 집합 생성
    spoiler_word_indices = []
    non_spoiler_words = set()

    for idx, info in enumerate(words_info):
        w_start, w_end = info["range"]
        is_spoiler = False

        if spoiler_ranges:
            for s_start, s_end in spoiler_ranges:
                # 두 구간 [w_start, w_end]와 [s_start, s_end]가 겹치는지 확인
                if not (w_end < s_start or w_start > s_end):
                    is_spoiler = True
                    break

        if is_spoiler:
            spoiler_word_indices.append(idx)
        else:
            non_spoiler_words.add(info["word"])

    # 3. 중요 단어 카운트
    answer = 0
    revealed_important_words = set()

    for idx in spoiler_word_indices:
        target_word = words_info[idx]["word"]

        # 일반 영역에 한 번이라도 등장했거나, 이미 중요 단어로 카운트된 경우 제외
        if target_word in non_spoiler_words:
            continue
        if target_word in revealed_important_words:
            continue

        answer += 1
        revealed_important_words.add(target_word)

    return answer


if __name__ == "__main__":
    msg, s_ranges = get_input_data()

    if msg is not None:
        result = solution(msg, s_ranges)
        print(result)
