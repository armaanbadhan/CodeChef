
tmp = [0]*200200

def count_inversions(arr, l, n):
    if n == 1:
        return 0
    m = n - n//2
    ans = count_inversions(arr, l, n//2)
    ans += count_inversions(arr, l+n//2, m)
    j = 0
    k = 0

    for i in range(l, l+n//2):
        while j < m and arr[l + n//2 + j] < arr[i]:
            tmp[k] = arr[l + n//2 + j]
            j += 1
        tmp[k] = arr[i]
        ans += j
    
    while j < m:
        tmp[k] = arr[l + n//2 + j]
        j += 1
        k += 1
    
    for i in range(n):
        arr[l+i] = tmp[i]
    
    return ans

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    inversions = count_inversions(arr, 0, n)
    print(inversions)


t = int(input())

for _ in range(t):
    solve()
