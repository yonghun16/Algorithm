# input data for List

import sys
input = sys.stdin.read
data = input().split()

print(data)

n = int(data[0])
testList = list(map(int, data[1:n+1]))
