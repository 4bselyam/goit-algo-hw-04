import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


sizes = [1000, 2000, 5000, 10000]
times_insertion = []
times_merge = []
times_timsort = []

for size in sizes:
    test_data = [random.randint(1, 10000) for _ in range(size)]

    times_insertion.append(
        timeit.timeit("insertion_sort(test_data.copy())", globals=globals(), number=1)
    )
    times_merge.append(
        timeit.timeit("merge_sort(test_data.copy())", globals=globals(), number=1)
    )
    times_timsort.append(
        timeit.timeit("sorted(test_data.copy())", globals=globals(), number=1)
    )

print(times_insertion)
print(times_merge)
print(times_timsort)
