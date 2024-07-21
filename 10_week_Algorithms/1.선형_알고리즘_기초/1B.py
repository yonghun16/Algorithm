# 문제1B-원소의 합 구하기


# 입력된 정수 배열의 합을 계산하는 함수
def getSum(inputNumbers):
    sum = 0
    for i in inputNumbers:
        sum += i
    return sum

# 첫 번째 줄에서 데이터의 수n을 읽습니다.
n = int(input().strip())

# 두 번째 줄에서 공백으로 구분된 n개의 정수를 읽어 옵니다.
inputNumbers = list(map(int, input().strip().split(' ')))

# 합계 계산
answer = getSum(inputNumbers)

# 결과 출력
print(answer)
