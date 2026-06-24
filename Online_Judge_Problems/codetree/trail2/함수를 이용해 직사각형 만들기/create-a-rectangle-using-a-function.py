n, m = map(int, input().split())

def print_rectangle(rows, cols):
    line = "1" * cols
    for _ in range(rows):
        print(line)

print_rectangle(n, m)