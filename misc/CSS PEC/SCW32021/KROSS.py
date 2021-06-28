
t = int(input())

for _ in range(t):
    path = input()
    n, e = 0, 0
    cord = [0]
    for dir in path:
        if dir == "N": n += 1
        if dir == "E": e += 1
        if dir == "W": e -= 1
        if dir == "S": n -= 1

        cord.append(n*100000 + e)
    
    if len(cord) == len(set(cord)):
        print(0)
    else:
        print(1)
