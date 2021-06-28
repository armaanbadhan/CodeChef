import bisect

n, q = map(int, input().strip().split())

inp = list(map(int, input().strip().split()))

a = set(inp)

roots = sorted(inp)


for i in range(q):
    inp = int(input())
    if inp in a:
        print(0)
    else:
        index = bisect.bisect_left(roots, inp)
        if n&1:
            if index&1:
                print("POSITIVE")
            else:
                print("NEGATIVE")
        else:
            if index&1:
                print("NEGATIVE")
            else:
                print("POSITIVE")
