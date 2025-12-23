"""
-----------------------------------------------------------
Sub    : [BOJ] 킹
Link   : https://www.acmicpc.net/problem/1063
Level  : 실버 3
Tag    : Python, 구현
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

# 이동 명령 정의
moves = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}

# 입력
king_pos, stone_pos, N = input().split()
N = int(N)

# 좌표 변환 (문자 -> 숫자)
kx, ky = ord(king_pos[0]) - ord("A"), int(king_pos[1]) - 1
sx, sy = ord(stone_pos[0]) - ord("A"), int(stone_pos[1]) - 1


def in_board(x, y):
    return 0 <= x < 8 and 0 <= y < 8


# 명령 처리
for _ in range(N):
    cmd = input().strip()
    dx, dy = moves[cmd]

    nkx, nky = kx + dx, ky + dy

    # 킹이 밖으로 나가면 무시
    if not in_board(nkx, nky):
        continue

    # 돌과 충돌하는 경우
    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy
        # 돌이 밖으로 나가면 무시
        if not in_board(nsx, nsy):
            continue
        # 돌 이동
        sx, sy = nsx, nsy

    # 킹 이동
    kx, ky = nkx, nky

# 결과 출력 (숫자 -> 문자)
print(f"{chr(kx + ord('A'))}{ky + 1}")
print(f"{chr(sx + ord('A'))}{sy + 1}")
