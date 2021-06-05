
t = int(input())

calc = lambda x : x*(x+1)//2

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    con = [[arr[0], 1]]
    for i in range(1, n):
        if arr[i-1] == arr[i]:
            con[-1][1] += 1
        else:
            con.append([arr[i], 1])
    res = 0
    for i in con:
        if i[1] != 1:
            res += i[1]-1 
    print(res)
