# from sys import setrecursionlimit

M = 1e9 + 7


'''
def calc(x, i, k, arr):
    if i == k:
        arr.append(x)
        return
    calc(2*x, i+1, k, arr)
    calc(2*x - 1, i+1, k, arr)

    return arr


x, k = map(int, input().strip().split())

A = calc(x, 0, k, [])
print(A)
print(len(A))
res = 0
for i in A:
    res += 2*i/(len(A))
    res %= M
print(res)

'''

def twopow(n):
    M = 1e9 + 7
    res = 1
    for _ in range(n):
        res *= 2
        res %= M
    return res


x, k = map(int, input().strip().split())


pew = int(twopow(k))

print((2*x - 1)*pew + 1)
