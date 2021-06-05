
n = int(input())
myset = set()

for i in range(n):
    myset.add(int(input()))

q = int(input())


print(1)
for i in range(q):
    x = int(input())
    if x in myset:
        print("yes")
    else:
        print("no")