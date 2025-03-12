# 파이썬에서 입력 받는 방법

# === 1. 하나를 입력 받기 ===
# 입력
# 3
num = int(input())


# === 2. 한 줄을 입력받기 ===
# 입력
# 3 5
a, b = map(int, input().split())


# === 3. 리스트를 통해 한 줄을 입력받기 ===
# 1 2 3 4 5 6 7 8 9
arr = list(map(int, input().split()))


# === 4. 한 줄로 문자열 변수 여려 개를 입력받기 ===
# abc def
a, b = input().split()


# === 5. 문자열 여러 줄을 입력받기 ===
# 입력
# ABCDEF
# BCDEFA
# CDEFAB
str = [input() for _ in range(3)]

# 2) 
# 2차원 배열 형태로 저장,  n개의 줄을 입력 받을 지 정할 수 있음.
# 변수명 = [list(map(int, input())) for _ in range(n)]
# 입력
# 0101
# 1010
# 2020
str = [list(map(int, input())) for _ in range(3)]


# === 6. 2차원 배열을 입력받기 ===
# 한 줄에 띄어쓰기가 있는 배열을, 여려 개의 줄을 통해 입력 받을 때, 2차원 배열 형태로 저장
# 입력
# 0 1 0 1
# 1 0 1 0
# 2 0 2 0
arr = [list(map(int, input().split())) for _ in range(4)]
