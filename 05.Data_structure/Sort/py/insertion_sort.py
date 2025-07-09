def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 한 칸 밀기
            j -= 1
        arr[j + 1] = key         # 삽입
    return arr

print(insertion_sort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
