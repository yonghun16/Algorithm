N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.

arr = []
result = []

for i in range(N):
    if command[i] == "push_back":
        arr.append(num[i])
    elif command[i] == "pop_back":
        arr.pop()
    elif command[i] == "size":
        result.append(len(arr))
    elif command[i] == "get":
        result.append(arr[num[i]-1])

print('\n'.join(map(str, result)))