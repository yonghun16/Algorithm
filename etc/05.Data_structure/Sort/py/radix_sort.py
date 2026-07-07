def counting_sort(arr, digit):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        idx = (num // digit) % 10
        count[idx] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        idx = (arr[i] // digit) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    digit = 1
    while max_val // digit > 0:
        counting_sort(arr, digit)
        digit *= 10
    return arr

print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
