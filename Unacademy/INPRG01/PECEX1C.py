t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sorted(a[i:j+1]) == sorted(b[i:j+1]):
                temp = j-i+1
                if temp > ans:
                    ans = temp
    print(ans)