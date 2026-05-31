"""
-----------------------------------------------------------
Sub    : [BOJ] 노란불 신호등
Link   : https://www.acmicpc.net/problem/468371
Level  : 1
Tag    : Python
-----------------------------------------------------------
Solution
1. 각 신호등의 총 주기(G + Y + R)를 구합니다.
2. 모든 신호등 주기의 최소공배수(LCM)를 구하여, 패턴이 반복되는 최대 시간을 설정합니다.
3. 0초부터 (최소공배수 - 1)초까지 순회하며, 모든 신호등이 노란불 상태(G <= t % Cycle < G + Y)인지 확인합니다.
4. 조건을 만족하는 가장 빠른 시간에 1을 더하여(문제는 1초부터 시작하므로) 반환 및 출력합니다.
-----------------------------------------------------------
"""

import math
import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    signals = []
    try:
        n = int(input().strip())
        for _ in range(n):
            signal = list(map(int, input().strip().split()))
            signals.append(signal)
    except:
        pass
    return signals


# ⚙️ Core Logic
def solution(signals):
    if not signals:
        return -1

    cycles = [g + y + r for g, y, r in signals]

    # 모든 신호등 주기의 최소공배수(LCM) 계산
    max_time = 1
    for c in cycles:
        max_time = math.lcm(max_time, c)

    # 0초부터 (최소공배수 - 1)초까지 시뮬레이션
    for t_prime in range(max_time):
        all_yellow = True

        for g, y, r in signals:
            cycle = g + y + r
            mod_t = t_prime % cycle

            # 노란불 구간인지 확인 (G <= 나머지 < G + Y)
            if not (g <= mod_t < g + y):
                all_yellow = False
                break

        if all_yellow:
            ans = t_prime + 1  # 문제는 1초부터 시작하므로 1을 더해줌
            print(ans)
            return ans

    # 최소공배수 주기 내에 모두 노란불이 되는 경우가 없다면 영원히 없음
    print(-1)
    return -1


# 🚀 Run Program
if __name__ == "__main__":
    signals = get_input_data()
    solution(signals)
