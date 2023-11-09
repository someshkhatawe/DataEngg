def get_index(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        num = arr[mid]
        if x == num:
            return mid
        if x > num:
            start = mid + 1

        if x < num:
            end = mid - 1

    return -1


def get_count(arr, x):
    if x in arr:
        count = 0
        index = get_index(arr, x)-1
        while arr[index] == x:
            count += 1
            index += 1
        return count
    else:
        return 0


arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 10, 40]
x = 4
print(get_count(arr, x))
