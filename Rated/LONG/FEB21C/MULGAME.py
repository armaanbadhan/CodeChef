t = int(input())
for _ in range(t):
    n, q, m = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    list = [0]*n


    for asdf in range(q):
        li, ri = map(int, input().strip().split())
        for k in range(li-1, ri):
            list[k] += 1

    print(max(list))
