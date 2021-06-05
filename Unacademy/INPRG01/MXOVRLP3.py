
t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    arr = []
    for i in range(n):
        l, r = map(int, input().strip().split())
        arr.append([l, 0])
        arr.append([r, 1])
    arr.sort()
    curr = 0
    res = 0
    for i in arr:
        if i[1] == 0:
            curr += 1
        else:
            curr -= 1
        res = max(res, curr)
    print(res)

# O(mlogm)
# storing all entry ans exit
# entry = 0, exit = 1
# calc the max overlap
