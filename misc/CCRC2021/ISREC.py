t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr.append(input().strip())
    one_start = -1
    one_end = -1
    verticle_start = False

    i = 0
    while i < n:
        hori
        one = False
        if start == False and arr[i] == "0"*m: # no one encountered
            i += 1
            continue
        j = 0
        while j < m: # save positions for first 1
            start = True
            if arr[i][j] == '1':
                if one == False:
                    one = True
                    one_start = j
                    one_end = j
                else:
                    one_end += 1
            if arr[i][j] == '0' and one == True:
                one = False
                break
        if 

