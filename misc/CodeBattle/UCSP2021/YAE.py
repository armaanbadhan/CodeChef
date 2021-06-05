import math

t = int(input())

for _ in range(t):
    a = int(input())
    res = 0
    i = 1
    arr = set()
    while i*i <= 100000:
        arr.add(i*i - a)
        i += 1


    for ele in arr:
        if ele > 0:
            for b in range(2 , 320):
                x = math.log(ele , b)
                if x > 0:
                    if x/1 == x//1:
                        if int(x)&1 == 0:
                            print(b, x//2)
                            res += 1

    print(res)
