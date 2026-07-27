"""
------------------------------------------------------------
Sub    : [Programmers] 동영상 재생기
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/340213
Level  :
Tag    : Python, Simulation
------------------------------------------------------------
Approach
- 모든 시간을 초(second)로 변환하여 계산한다.
- 현재 위치가 오프닝 구간이면 op_end로 이동한다.
- 각 명령(prev, next)을 수행한다.
- 명령 수행 후 다시 오프닝 구간인지 검사한다.
- 마지막 위치를 "mm:ss" 형식으로 변환하여 반환한다.
------------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data():
    data = input().split()

    video_len = data[0]
    pos = data[1]
    op_start = data[2]
    op_end = data[3]
    commands = data[4:]

    return video_len, pos, op_start, op_end, commands


# ⚙️ Logic
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


# 🚀 Run Program
if __name__ == "__main__":
    print(solution(*get_input_data()))
