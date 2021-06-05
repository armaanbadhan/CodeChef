
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

arr.sort(reverse=True)

res = arr[0] - arr[n-1]

for i in range(1, m-n+1):          # check for every subarray of len n
    temp_res =  arr[i] - arr[i+n-1]
    res = min(res, temp_res)       # if min, res = temp_res

print(res)
