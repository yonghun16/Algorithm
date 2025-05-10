'''----------------------------------------------
Sub : [BOJ] 폰 노이만
Link: https://www.acmicpc.net/problem/9469
level : 브론즈 3
Tag : Python, 
Memo
- 수학적 개념을 한번 먼저 생각해보기
- 거리 = 시간 * 속력
- 시간 = 거리 / 속력
----------------------------------------------'''

# 입력 받기
P = int(input())  # 테스트 케이스 수

results = []

for _ in range(P):
    # 테스트 케이스 입력 처리
    N, D, A, B, F = map(float, input().split())
    N = int(N)  # 테스트 케이스 번호
    
    # 두 기차 충돌 시간 계산
    collision_time = D / (A + B)
    
    # 파리의 이동 거리 계산
    fly_distance = F * collision_time
    
    # 결과 저장
    results.append((N, fly_distance))

# 출력
for N, distance in results:
    print(f"{N} {distance:.6f}")
