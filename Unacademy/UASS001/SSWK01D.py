
def insertion_sort(arr):
	k = 0
	for i in range(1, len(arr)):		
		key = arr[i]
		j = i - 1 
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
			k += 1
		arr[j+1] = key

	print(k)	    
	return

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split()))
    insertion_sort(A)
