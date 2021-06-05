arr = [1]*10
arr = [0] + arr

for i in range(1, len(arr)):
    arr[i] += arr[i-1]

print(arr)
