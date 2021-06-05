
def bubbleSort(arr, n):
    for i in range(n): 
        swapped = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped:
            print(*arr)
        else:
            return
    return

n = int(input())
arr = list(map(int, input().strip().split()))
bubbleSort(arr, n)
