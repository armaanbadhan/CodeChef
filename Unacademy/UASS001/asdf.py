def main():
    t = int(input())

    for _ in range(t):
        n, r, g, b = map(int, input().strip().split())
        ans = 0
        temp = min(r, b, g)
        r -= temp
        b -= temp
        g -= temp
        while r > 0 and b > 0 and ans+temp < n:
            r -= 1
            b -= 1
            if g > 0:
                g -= 1
            elif b > 0 or r > 0:
                if r < b:
                    b -= 1
                else:
                    r -= 1
            elif b == 0 and r == 0:
                break
            ans += 1
        print(ans + temp)

main()
