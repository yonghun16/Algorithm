arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def binary_search(arr, target):
    count = 0
    left = 0
    right = len(arr) - 1

    while left <= right:
        count += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            # return mid           # 찾은 경우 인덱스 반환
            return count
        elif arr[mid] < target:
            left = mid + 1        # 오른쪽 반을 탐색
        else:
            right = mid - 1       # 왼쪽 반을 탐색

    return -1  # 찾지 못한 경우


result = binary_search(arr3, 1)
print(result)
