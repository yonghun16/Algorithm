n = int(input())

num = 1

for _ in range(n):
    row = []

    for _ in range(n):
        row.append(str(num))
        num = (num % 9) + 1

    print(" ".join(row))