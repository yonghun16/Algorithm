"""
-----------------------------------------------------------
Sub    : [BOJ] 부울행렬의 부울곱
Link   : https://www.acmicpc.net/problem/14492
Level  : 실버 5
Tag    : Python,
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import sys


def solve():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    # 행렬 A를 비트 숫자로 변환 (각 행을 하나의 큰 정수로 취급)
    # 0101 -> 5와 같은 방식
    matrix_a = []
    current = 1
    for i in range(n):
        row_str = "".join(input_data[current : current + n])
        matrix_a.append(int(row_str, 2))
        current += n

    # 행렬 B를 열(Column) 단위로 비트 숫자로 변환
    # B의 j번째 열을 하나의 숫자로 만들면 A의 행과 바로 AND 연산 가능
    cols_b = [0] * n
    for i in range(n):
        row_values = input_data[current : current + n]
        for j in range(n):
            if row_values[j] == "1":
                # i번째 행의 j번째 열이 1이라면, cols_b[j]의 i번째 비트를 1로 설정
                cols_b[j] |= 1 << (n - 1 - i)
        current += n

    total_ones = 0

    # 부울곱 연산 수행
    for i in range(n):
        row_a = matrix_a[i]
        for j in range(n):
            col_b = cols_b[j]

            # row_a와 col_b를 AND(&) 연산했을 때 0이 아니라면,
            # 공통으로 1인 위치(k)가 존재한다는 뜻이므로 c[i][j]는 1임
            if row_a & col_b:
                total_ones += 1

    print(total_ones)


if __name__ == "__main__":
    solve()
