
def bubble(x):
    sw = 0
    res = []
    while True:
        swap = False
        j = 1
        for i in range(len(x)-j):
            ele1 = x[i]
            ele2 = x[i+1]
            if ele1 > ele2:
                x[i], x[i+1] = ele2, ele1
                sw += 1
                res.append(i)
                swap = True
        if not swap:
            return sw, res
        j += 1


def main():
    n = int(input())
    myarr = list(map(int,input().strip().split()))
    sw, res = bubble(myarr)
    print(sw)
    print(*res)


main()

# AC?