import sys
input = sys.stdin.readline


# === 1. 하나를 입력 받아 숫자형 변수에 저장 ===
# 입력
# 3
num = int(input().strip())



# === 2. 한 줄 입력받아 각각의 숫자형 변수에 저장 ===
# 입력
# 3 5
a, b = map(int, input().strip().split())  # 문자열 처리 흐름은: 입력 → 공백 제거 → 나누기 → 변환



# === 3. 한 줄 입력 받아 리스트로 저장 ===
# 1 2 3 4 5 6 7 8 9
arr = list(map(int, input().strip().split()))



# === 4. 한 줄 입력받아 각각의 문자열 변수에 저장 ===
# abc def
a, b = input().strip().split()

#출력
print(a, b)



# === 5. 문자열 여러 줄을 입력받아 1차원 리스트에 저장 ===
# 1차원 배열 형태로 저장, n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
# 입력
# ABCDEF
# BCDEFA
# CDEFAB
str = [input().strip() for _ in range(3)]

# 출력
print(str)



# === 6. 숫자 데이터 여러 줄을 입력받아 2차원 리스트에 저장 ===
# 숫자열 데이터로 변환 후, 2차원 배열 형태로 저장,
# n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
# 입력
# 0101
# 1010
# 2020
str = [list(map(int, input().strip())) for _ in range(3)]

# 출력
for i in range(3):
    for j in range(4):
        print(str[i][j], end='')
    print()



# === 7. 숫자 데이터의 2차원 배열을 입력받기 ===
# 한 줄에 띄어쓰기가 있는 배열을, 여려 개의 줄을 통해 입력 받을 때, 2차원 배열 형태로 저장
# 입력
# 0 1 0 1
# 1 0 1 0
# 2 0 2 0
arr = [list(map(int, input().strip().split())) for _ in range(3)]

# 출력
for i in range(3):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()
