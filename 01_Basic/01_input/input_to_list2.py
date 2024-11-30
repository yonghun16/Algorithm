'''
----------------------------------------------
input data for List
----------------------------------------------
input style:
  ex)
    >>> 4
    >>> 1 
    >>> 2
    >>> 3
    >>> 4
    [1, 2, 3, 4]
----------------------------------------------
'''

# 입력
n = int(input())
inputDataList = [int(input()) for _ in range(n)]      # 한 줄 마다 하나씩 받기
#inputDataList = [int(w) for w in input().split()]    # 한 줄에 통으로 받기

# 출력
print(inputDataList)
