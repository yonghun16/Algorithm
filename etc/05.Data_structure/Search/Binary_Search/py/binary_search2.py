def b_search(arr, len, target):
    first = 0
    last = len - 1

    while first <= last:
        mid = (first + last) // 2

        if target == arr[mid]:
            return mid
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return -1


arr1 = [1, 3, 5, 7, 9]

idx = b_search(arr1, len(arr1), 7)
if idx == -1:
    print("Not found")
else:
    print("Found at index", idx)


idx = b_search(arr1, len(arr1), 4)
if idx == -1:
    print("Not found")
else:
    print("Found at index", idx)
