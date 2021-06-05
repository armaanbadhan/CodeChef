
def fun(i, n, s, fleft, res):
    if i == n:
        return
    
    fun(i+1, n, s, fleft - 1, [0])
    fun(i+1, n, s, fleft, [0])

    return res




t = int(input())

for _ in range(t):
    n, f = map(int, input().strip().split())
    s = input().strip()
    print(fun(0, n, s, f, [0]))
