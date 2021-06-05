def main():
    t = int(input())

    sub_arrs = lambda x : x*(x+1)//2

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        total = sub_arrs(n)
        lust = [[arr[0], 1]]
        for i in range(1, n):
            if lust[-1][0] == arr[i]:
                lust[-1][1] += 1
            else:
                lust.append([arr[i], 1])
        for i in lust:
            total -= sub_arrs(i[1])
        print(total)

# AC on sub 1 finally

main()
