"""
-----------------------------------------------------------
Sub    : [BOJ] 김식당
Link   : https://www.acmicpc.net/problem/14612
Level  : Silver 4
Tag    : Python,
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
else:
    lines = sys.stdin.read().splitlines()

input_iter = iter(lines)

try:
    line1 = next(input_iter).split()
    N, M = map(int, line1)
except StopIteration:
    exit()

orders = []  # 주문 포스트잇을 담을 리스트 (각 요소는 {'n': 번호, 't': 시간})

# 4. 명령어 처리 루프
for _ in range(N):
    try:
        query = next(input_iter).split()
        if not query:
            continue

        cmd = query[0]

        if cmd == "order":
            table_n = int(query[1])
            time_t = int(query[2])
            # 주문이 들어오면 리스트 맨 뒤에 추가
            orders.append({"n": table_n, "t": time_t})

        elif cmd == "sort":
            # 정렬 조건: 1순위 시간(t) 오름차순, 2순위 테이블 번호(n) 오름차순
            orders.sort(key=lambda x: (x["t"], x["n"]))

        elif cmd == "complete":
            table_n = int(query[1])
            # 해당 테이블 번호를 가진 포스트잇을 찾아 제거
            for i in range(len(orders)):
                if orders[i]["n"] == table_n:
                    orders.pop(i)
                    break

        if not orders:
            print("sleep")
        else:
            print(*(order["n"] for order in orders))

    except StopIteration:
        break
