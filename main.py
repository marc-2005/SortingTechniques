
def selection_sort(arr, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    size = len(arr)
    selection_sort(arr, size)
    print("Sorted array:", arr)