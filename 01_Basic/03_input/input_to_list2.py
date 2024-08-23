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
inputDataList = [int(input()) for _ in range(n)]

# 출력
print(inputDataList)
