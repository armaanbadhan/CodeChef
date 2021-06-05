n = int(input())

max = 0

ar = list(map(int, input().strip().split(' ')))

for i in range(n):
    ele = ar[i] + max
    print(ele, end=' ')
    if ele > max:
        max = ele
