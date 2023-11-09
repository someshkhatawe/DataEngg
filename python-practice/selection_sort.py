def selection_sort(arr, n):
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr


print(selection_sort([-2, 45, 0, 11, -9,88,-97,-202,747], 9))

