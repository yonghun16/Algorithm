arr = list(map(int, input().split()))

n: int = len(arr)
result: int = 0

for i in range(0,n):
    if arr[i] == 0:
        result = arr[i-1] + arr[i-2] + arr[i-3]
        break;

print(result)

