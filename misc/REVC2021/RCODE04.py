
t = int(input())

for _ in range(t):
    n = int(input())
    mex = bin(n)[2:]
    for i in range(1, n+1):
        bi = bin(i)[2:]
        bi = "0"*(len(mex) - len(bi)) + bi
        temp = ""
        for j in bi:
            if j == "0":
                temp += "#"
            else:
                temp += "*"
        print(temp)
