# A+B -4
# https://www.acmicpc.net/problem/10951
# 한줄에 여려 번수를 입력받음

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
