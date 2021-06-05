def main():
    t = int(input())
    for _ in range(t):
        n, r, g, b = map(int, input().strip().split())
        lo, hi = 0, min(r, b, n)
        while lo <= hi:
            mid = (lo + hi)//2
            if r + g + b >= mid + 2*min(r, b, mid):
                lo = mid + 1
            else:
                hi = mid - 1
        print(hi)

main()
