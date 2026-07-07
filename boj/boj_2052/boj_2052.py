from decimal import Decimal, getcontext
import sys

# 정수 N 입력
n = int(sys.stdin.readline())

# 정밀도를 충분히 설정 (N의 최대치인 250보다 여유 있게 설정)
getcontext().prec = 300

# 1 / 2^n 계산
# 0.5의 n제곱으로 계산하거나 1 / (2**n)으로 계산
result = Decimal(1) / (Decimal(2) ** n)

# 'f' 포맷을 사용하여 지수 표기법(e)이 아닌 일반 소수 형태로 출력
# normalize()는 뒤의 불필요한 0을 제거함
print(format(result.normalize(), "f"))
