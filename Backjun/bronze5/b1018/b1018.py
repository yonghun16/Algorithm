# https://www.acmicpc.net/problem/1018

N = 8
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
pivot1 = [ str1, str2, str1, str2, str1, str2, str1, str2 ]
pivot2 = [ str2, str1, str2, str1, str2, str1, str2, str1 ]
 
def solve():
  a, b = [int(x) for x in input().split()]
  arr = []
  for i in range(a):
    arr.append(input())
  rst = float('inf')
  for i in range(a-N+1):
    for j in range(b-N+1):
      count = 0
      for p in range(N):
        for q in range(N):
          if arr[i+p][j+q] != pivot1[p][q]:
            count += 1
      rst = min(rst, count)
      count = 0
      for p in range(N):
        for q in range(N):
          if arr[i+p][j+q] != pivot2[p][q]:
            count += 1
      rst = min(rst, count)
  print(rst)
 
solve()
