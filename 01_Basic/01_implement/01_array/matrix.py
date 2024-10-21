'''
rows(행) : i값이 올라가면 가로행이 하나씩 올라감.
cols(열) : j값이 올라가면 세로열이 하나씩 올라감.
'''

# 2차원 리스트의 크기를 정의
rows, cols = 3, 3

# 빈 2차원 리스트 생성
matrix = []

# 사용자로부터 값을 입력받아 2차원 리스트를 생성
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"matrix[{i}][{j}] 값을 입력하세요: "))
        row.append(value)
    matrix.append(row)

# 입력된 2차원 리스트 출력
print("입력된 2차원 리스트:")
for row in matrix:
    print(row)
