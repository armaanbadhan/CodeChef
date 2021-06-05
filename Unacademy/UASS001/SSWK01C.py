
n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()

heh = arr[0]
lmao = [[heh, 1]]

for i in range(1, n):
    if lmao[-1][0] == arr[i]:
        lmao[-1][1] += 1
    else:
        lmao.append([arr[i], 1])

hehehe = []

for i in lmao:
    hehehe.append(i[1])

hehehe.reverse()

for i in range(1, len(hehehe)):
    hehehe[i] += hehehe[i-1]

hehehe.reverse()

for i in hehehe:
    print(i)
