def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertionSort(arr):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j =  j - 1

        a[j+1] = key
    

a = [23,34,12,35,28,60,45]
bubbleSort(a)
print(a)
selectionSort(a)
print(a)
insertionSort(a)
print(a)