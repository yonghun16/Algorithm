nums: list[int] = list(map(int, input().split()))

sum_odd: int = 0    # 홀수 번째로 입력받은 값의 합
sum_even: int = 0   # 짝수 번째로 입력받은 값의 합

for i in range(len(nums)):
    if (i + 1) % 2 == 1:
        sum_odd += nums[i]
    else:
        sum_even += nums[i]

result: int = abs(sum_odd - sum_even)
print(result)