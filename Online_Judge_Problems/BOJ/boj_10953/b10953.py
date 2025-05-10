# A+B - 6
# https://www.acmicpc.net/problem/10953

def getSum(a, b):
    return a + b

results = []

n = int(input())

for _ in range(n):
    line = input()

    a, b = map(int, line.split(','))

    results.append(getSum(a, b))

for result in results:
    print(result)