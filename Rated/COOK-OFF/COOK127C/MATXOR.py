
def debug(a) : return # print("lol", a)

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().strip().split())
    a = min(n, m)
    b = max(n, m)
    if a == b:
        res = 0
        for i in range(2, b+a+2, 2):
            debug(i)
            res ^= (i+k)
        print(res)
    else:
        if a%2 == 0 and b%2 == 0: # E E
            res = 0
            for i in range(2, a+2, 2):
                res ^= (i+k)
            for i in range(b+2, b+a+2, 2):
                debug(i)
                res ^= (i+k)
            print(res)
        elif a%2 and b%2: # O O
            res = 0
            for i in range(2, a+3, 2):
                debug(i)
                res ^= (i+k)
            for i in range(a+2, b+1):
                debug(i)
                res ^= (i+k)
            for i in range(b+1, b+a+2, 2):
                res ^= (i+k)
            print(res)
        elif a%2 == 0 and b%2: # E O
            res = 0
            for i in range(2, a+2, 2):
                res ^= (i+k)
            for i in range(b+2, b+a+2, 2):
                res ^= (i+k)
            print(res)
        else: # O E
            res = 0
            for i in range(2, a+3, 2):
                debug(i)
                res ^= (i+k)
            for i in range(a+2, b+1):
                debug(i)
                res ^= (i+k)
            for i in range(b+1, b+a+2, 2):
                debug(i)
                res ^= (i+k)
            print(res)

# ffffffffffffffffffffffffffffffffffff
# fuck
# (i+k) insted if i fuckkkk meeeeeeeeee
# fuck

# https://www.codechef.com/viewsolution/44029556
# https://www.codechef.com/viewsolution/44027347
