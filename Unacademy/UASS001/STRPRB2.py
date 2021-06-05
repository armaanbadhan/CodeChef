n = int(input())
given = list(map(int, input().strip().split()))

myarr = []
for i in given:
    myarr.append([{i}, 1])

cnt = 0

while len(myarr) != 1:

    temp = []
    for i in range(0, len(myarr), 2):
        x = (myarr[i][0])|(myarr[i+1][0])
        temp.append([x, len(x)])
        if (myarr[i][1] + myarr[i+1][1]) == temp[i//2][1]:
            cnt += 1
    myarr = temp

print(cnt)
