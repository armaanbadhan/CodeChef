def main():
    slope = lambda x1, y1, x2, y2 : (y2-y1)/(x2-x1)

    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = 1
        i = 0
        while i < n-1:
            temp_res = 1
            fori = slope(i, arr[i], i+1, arr[i+1])
            j = i+2
            next = i+1
            while j < n:
                x = slope(i, arr[i], j, arr[j])
                if x >= fori:
                    fori = x
                    temp_res = j-i
                    next = j
                j += 1
            res = max(temp_res, res)
            i = next
        print(res)


main()
# sub 2 passed
# only 1 task gave tle pepecri

#same code PyPy3 got AC