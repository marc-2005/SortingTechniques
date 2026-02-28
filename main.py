import random
import time
import copy

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def generate_random_array(size):
    return [random.randint(0, 100001) for _ in range(size)]

def test_sorting_algorithms(size):
    print(f"\nArray Size: {size}")

    original_array = generate_random_array(size)

    # Bubble Sort
    arr1 = copy.copy(original_array)
    start = time.time()
    bubble_sort(arr1)
    end = time.time()
    print(f"Running time for Bubble Sort is {(end - start)*1000:.2f} ms")

    # Selection Sort
    arr2 = copy.copy(original_array)
    start = time.time()
    selection_sort(arr2)
    end = time.time()
    print(f"Running time for Selection Sort is {(end - start)*1000:.2f} ms")

    # Insertion Sort
    arr3 = copy.copy(original_array)
    start = time.time()
    insertionSort(arr3)
    end = time.time()
    print(f"Running time for Insertion Sort is {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    test_sorting_algorithms(size)