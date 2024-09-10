def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps.append((arr.copy(), n - i - 1, j, j + 1))
    steps.append((arr.copy(), -1, -1, -1))
    return steps

def insertion_sort(arr):
    steps = []
    n = len(arr)
    sorted_indices = set()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        sorted_indices.add(j + 1)
        sorted_indices.add(i)
        steps.append((arr.copy(), sorted_indices.copy(), i))
    sorted_indices.update(range(n))
    steps.append((arr.copy(), sorted_indices.copy(), -1))
    return steps

def selection_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append((arr.copy(), i, min_idx, -1))
    steps.append((arr.copy(), -1, -1, -1))
    return steps
