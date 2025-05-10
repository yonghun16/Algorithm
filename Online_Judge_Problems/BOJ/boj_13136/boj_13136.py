import math

# 입력 값 받기
R, C, N = map(int, input().split())

# 필요한 CCTV의 개수 계산
vertical_cctv_count = (R + N - 1) // N
horizontal_cctv_count = (C + N - 1) // N

# 전체 CCTV의 개수
total_cctv_count = vertical_cctv_count * horizontal_cctv_count

# 결과 출력
print(total_cctv_count)
