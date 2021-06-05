for _ in range(int(input())):
    n = int(input())
    l = list(input().strip().split())
    total_pairs = n*(n-1)
    invalid_pair = 0

    for i in range(n):
        for j in range(i+1, n):
            if (l[i][0]+l[j][1:] in l) or (l[j][0]+l[i][1:] in l):
                invalid_pair += 1
                print(l[i], l[j])
    print(total_pairs - (invalid_pair*2))
    
# TLE on sub 2