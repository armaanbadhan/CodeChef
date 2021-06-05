def main():
    def good(arr, l, r):
        maxx = max(arr[l:r+1])
        orr, andd = arr[l], arr[l]
        for i in range(l+1, r+1):
            orr = orr|arr[i]
            andd = andd&arr[i]
        if orr^andd < maxx:
            return False
        return True    

    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = 0
        for i in range(n):
            for j in range(i, n):
                if good(arr, i, j):
                    res += 1
        print(res)

main()

# gives correct ans, optimize it
