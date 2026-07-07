# 두 수 비교하기
# https://www.acmicpc.net/problem/1330

a, b = map(int, input().split())

# 두 정수를 비교하고 결과 출력
def compare(a, b):
    if a > b:
        return('>')
    elif a < b:
        return('<')
    else:
        return('==')

print(compare(a, b))


