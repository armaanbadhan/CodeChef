
n, h, x = map(int, input().strip().split())
arr = max(list(map(int, input().strip().split())))

if arr < h-x:
    print("NO")
else:
    print("YES")
