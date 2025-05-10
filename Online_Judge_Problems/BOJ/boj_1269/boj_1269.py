'''----------------------------------------------------
Sub  : [BOJ] 대칭 차집합 
Link : https://www.acmicpc.net/problem/1269
Level: silver 4
Tag  : Python, 
Memo
----------------------------------------------------'''

# 입력 받기

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 리스트 정렬
A.sort()
B.sort()

# 대칭 차집합 계산 (두 리스트를 투 포인터 방식으로 비교)
i, j = 0, 0

symmetric_difference = 0

while i < n and j < m:
    if A[i] < B[j]:  # A의 원소가 B보다 작은 경우
        symmetric_difference += 1
        i += 1

    elif A[i] > B[j]:  # B의 원소가 A보다 작은 경우
        symmetric_difference += 1
        j += 1

    else:  # A[i] == B[j], 공통 원소이므로 제외
           # symmetric_difference += 1  더하지 않는다.
        i += 1
        j += 1

# 남아있는 원소 처리
symmetric_difference += (n - i) + (m - j)

# 결과 출력
print(symmetric_difference)
