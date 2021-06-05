import sys
 
def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())
# --------------------- Do not touch anything above this line ----------------------
 
# A sample function that computes (2 * a) % m using add(a, b)
def modm(a):
    return add(a//2, a-(a//2))
 
def multi(p, q):
    res = 0
    for i in range(q):
        res += p
        res = modm(res)
    return res


def pwr(a, b):
    res = 1
    for i in range(b):
        res = multi(res, a)
        res = modm(res)
    return res
 
# --------------------- Do not touch anything below this line ----------------------
 
 
a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)
 