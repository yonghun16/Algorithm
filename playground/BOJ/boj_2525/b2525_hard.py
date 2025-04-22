import sys
input = sys.stdin.readline

# 입력
A, B = map(int, input().strip().split())
C = int(input().strip())

# 계산
total_minute = (A * 60 + B + C) % 1440        # 요리 종료 시간
hour = total_minute // 60
min = total_minute % 60

# 출력
print(hour, min)
