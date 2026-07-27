def to_sec(time):
    m, s = map(int, time.split(":"))
    return m * 60 + s


def to_time(sec):
    return f"{sec // 60:02}:{sec % 60:02}"


def solution(video_len, pos, op_start, op_end, commands):
    answer = ""

    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    def skip_opening(cur):
        if op_start <= cur <= op_end:
            return op_end
        return cur

    # 시작 위치에서도 오프닝 체크
    pos = skip_opening(pos)

    for cmd in commands:
        if cmd == "prev":
            pos = max(0, pos - 10)
        else:  # next
            pos = min(video_len, pos + 10)

        pos = skip_opening(pos)

    answer = to_time(pos)

    return answer
