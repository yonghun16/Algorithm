import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    G = int(input())
    ids = [int(input()) for _ in range(G)]

    m = 1
    while True:
        seen = set()
        ok = True

        for x in ids:
            r = x % m
            if r in seen:
                ok = False
                break
            seen.add(r)

        if ok:
            print(m)
            break

        m += 1
