# A+B -3
# https://www.acmicpc.net/problem/10950

# 두 수를 더하는 함수
def getSum(a, b):
    return a + b

answers = []

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    answers.append(getSum(a, b))

for answer in answers:
    print(answer)
