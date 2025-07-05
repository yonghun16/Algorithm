import sys
input = sys.stdin.readline


# === 1. 하나를 입력 받아 숫자형 변수에 저장 ===
# 입력
# 3
num = int(input().strip())

print(num)


# === 2. 한 줄 입력받아 각각의 숫자형 변수에 저장 ===
# 입력
# 3 5
num1, num2 = map(int, input().strip().split())  # 문자열 처리 흐름은: 입력 → 공백 제거 → 나누기 → 변환

print(num1, num2)



# === 3. 한 줄 입력 받아 리스트로 저장 ===
# 1 2 3 4 5 6 7 8 9
arr = list(map(int, input().strip().split()))



# === 4. 한 줄 입력받아 각각의 문자열 변수에 저장 ===
# abc def
str1, str2 = input().strip().split()

print(str1, str2)



# === 5. 문자열 여러 줄을 입력받아 1차원 리스트에 저장 ===
# 1차원 배열 형태로 저장, n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
# 리스트 컴프리핸션을 사용하시오.
# 입력
# ABCDEF
# BCDEFA
# CDEFAB
str = [input().strip() for _ in range(3)]

print(str)



# === 6. 공백이 없는 숫자 데이터 여러 줄을 입력받아 2차원 리스트에 저장 ===
# 숫자열 데이터로 변환 후, 2차원 배열 형태로 저장,
# n개의 줄을 입력 받을 지 정할 수 있음. -> range(n)
# 리스트 컴프리핸션을 사용하시오.
# 입력
# 0101
# 1010
# 2020
str = [list(map(int, input().strip())) for _ in range(3)]

print(str)


# === 7. 숫자 데이터의 2차원 배열을 입력받기 ===
# 한 줄에 띄어쓰기가 있는 배열을, 여려 개의 줄을 통해 입력 받을 때, 2차원 배열 형태로 저장
# 리스트 컴프리핸션을 사용하시오.
# 입력
# 0 1 0 1
# 1 0 1 0
# 2 0 2 0
arr = [list(map(int, input().strip().split())) for _ in range(3)]

print(arr)


# === 8. 파일 여러 줄씩 읽기 ===
# 리스트 컴프리핸션을 사용하시오.
# 예: 첫 줄에 테스트 케이스 개수, 이후 줄마다 숫자 한 개씩 들어 있다고 가정
'''--------------
# input.txt 
3
1
2
3
--------------'''
file = open('input.txt', 'r')
lines = file.readlines()
T = int(lines[0].strip())

numbers = [int(lines[i].strip()) for i in range(1, T + 1)]

print(numbers)

file.close()
