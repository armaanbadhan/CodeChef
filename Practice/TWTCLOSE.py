n, k = map(int, input().strip().split(" "))
ar = [0]*n
for _ in range(k):
    z = input()[6:]
    if z == "L":
        ar = [0]*n
    else:
        z = int(z) - 1
        if ar[z] == 0:
            ar[z] = 1
        else:
            ar[z] = 0
    print(sum(ar))
