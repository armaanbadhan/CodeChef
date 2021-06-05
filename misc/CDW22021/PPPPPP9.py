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

def exponentMod(A, B, M):
    if B == 0:
        return 1
    if B % 2 == 0:
        temp = exponentMod(2, B//2, M)
        y = temp * temp
        y %= M
    else:
        temp = exponentMod(2, B//2, M)
        y = 2 * temp * temp
        y %= M
    return y


x, k = map(int, input().strip().split())

if x == 0:
    print(0)
    exit()

pew = int(exponentMod(2, k, M))

res = (2*x - 1)*pew + 1
res %= M

print(res)
