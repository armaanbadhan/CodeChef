
n = int(input())

mydict = {}
res = 0

for _ in range(n):
    a, b, name, dir = input().strip().split()
    for j in a, b:
        if j in mydict:
            mydict[j].append(name)
        else:
            mydict[j] = [name]

for i in mydict:
    if len(mydict[i]) == 4 and len(set(mydict[i])) == 2:
        res += 1

print(res)
