
n = int(input())

if n%3:
    print(-1)
else:
    if n&1:
        print(1)
    else:
        print(0)
