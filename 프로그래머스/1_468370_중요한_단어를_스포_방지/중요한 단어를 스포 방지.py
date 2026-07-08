def solution(message, spoiler_ranges):
    # 1. 메시지 내 모든 단어와 그 위치(인덱스 범위) 파악
    words_info = []
    start = 0
    for i, char in enumerate(
        message + " "
    ):  # 마지막 단어 처리를 위해 공백 추가
        if char == " ":
            if start < i:
                words_info.append(
                    {"word": message[start:i], "range": (start, i - 1)}
                )
            start = i + 1

    # 2. 각 단어가 스포일러 단어인지 판별
    # 단어의 인덱스 중 하나라도 스포일러 구간에 걸치면 스포일러 단어
    spoiler_word_indices = []
    non_spoiler_words = set()

    for idx, info in enumerate(words_info):
        w_start, w_end = info["range"]
        is_spoiler = False

        for s_start, s_end in spoiler_ranges:
            # 단어 범위 [w_start, w_end]와 스포일러 범위 [s_start, s_end]가 겹치는지 확인
            if not (w_end < s_start or w_start > s_end):
                is_spoiler = True
                break

        if is_spoiler:
            spoiler_word_indices.append(idx)
        else:
            # 어떤 스포일러 구간에도 속하지 않는 단어들 (중요 단어 후보 탈락용)
            non_spoiler_words.add(info["word"])

    # 3. 순서대로 공개하며 중요한 단어 카운트
    answer = 0
    revealed_spoiler_words = set()  # 이전에 공개된 스포일러 단어 기록

    for idx in spoiler_word_indices:
        target_word = words_info[idx]["word"]

        # 조건 1: 스포 방지 구간이 아닌 구간에 등장한 적이 없어야 함
        if target_word in non_spoiler_words:
            continue

        # 조건 2: 이전에 공개된 스포 방지 단어와 중복되지 않아야 함
        if target_word in revealed_spoiler_words:
            continue

        # 모든 조건 만족 시 중요한 단어
        answer += 1
        revealed_spoiler_words.add(target_word)

    return answer
