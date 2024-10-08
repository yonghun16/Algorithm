# https://programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    length = len(nums)
    answer = 0

    for i in range(length-2):
        for j in range(i + 1, length-1):
            for k in range(j + 1, length):
                if lsPrime([nums[i], nums[j], nums[k]]):
                    answer += 1
    return answer


def lsPrime(lst):
    sum_lst = sum(lst)
    for i in range(2, sum_lst):
        if sum_lst % i == 0:
            return False
    return True
