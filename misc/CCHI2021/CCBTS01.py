
t = int(input())

for i in range(t):
    mystr = input().strip()
    myset = set()
    for i in mystr:
        myset.add(i)
    if len(myset) == 3:
        print('YES')
    else:
        print('NO')