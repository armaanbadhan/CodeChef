
def andofsubarrs(arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp = arr[i]
            for k in range(i+1, j+1):
                temp &= arr[k]
            res.append(temp)
    return res


def orofele(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res |= arr[i]
    return res


t = int(input())

for _ in range(t):
    n, q = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(orofele(andofsubarrs(arr)))
    for i in range(q):
        x, v = map(int, input().strip().split())
        arr[x-1] = v
        print(orofele(andofsubarrs(arr)))
