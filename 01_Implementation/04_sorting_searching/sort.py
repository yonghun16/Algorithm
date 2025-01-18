'''
----------------------------------------------
[BOJ] 1448. 삼각형 만들기
----------------------------------------------
Link: https://www.acmicpc.net/problem/1448
Tag: py, greedy, sort
Memo:
    sort() 메서드는 리스트 객체의 메서드로, 리스트를 제자리에서(in-place) 정렬합니다. 즉, 원본 리스트가 변경됩니다.
    기본적으로 오름차순으로 정렬되며, 내림차순으로 정렬하려면 reverse=True 옵션을 사용할 수 있습니다.
----------------------------------------------
'''

# 가장 큰 삼각형의 변들의 합 반환
def max_triangle_perimeter(sticks):
    sticks.sort(reverse=True)  # 내림차순으로 정렬
    for i in range(len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            return sticks[i] + sticks[i + 1] + sticks[i + 2]
    return -1

# 입력 받기
import sys

input = sys.stdin.read
data = input().split()

# 입력 
n = int(data[0])
sticks = list(map(int, data[1:n+1]))

# 결과 출력
print(max_triangle_perimeter(sticks))
