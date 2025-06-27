'''
----------------------------------------------
input data for List
----------------------------------------------
input style:
  ex1)
    >>> 4 1 2 3 4
    [1, 2, 3, 4]
  ex2)
    >>> 4
    >>> 1 2 3 4
    [1, 2, 3, 4]
  ex3)
    >>> 4
    >>> 1 
    >>> 2
    >>> 3
    >>> 4
    [1, 2, 3, 4]
----------------------------------------------
'''

import sys

input = sys.stdin.read
data = input().split()

# 입력 
n = int(data[0])
inputDataList = list(map(int, data[1:n+1]))

# 출력
print(inputDataList)
