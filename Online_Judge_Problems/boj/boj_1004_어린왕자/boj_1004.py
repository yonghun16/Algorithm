import sys

input = sys.stdin.readline


def is_inside(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 < r**2


T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        start = is_inside(x1, y1, cx, cy, r)
        end = is_inside(x2, y2, cx, cy, r)

        if start != end:  # 한 점만 원 안에 있을 때
            count += 1

    print(count)
