for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().strip().split()))
    l = list(map(int, input().strip().split()))

    dicl_l = {}
    dicl_ind = {}
    for i in w:
        dicl_l[i] = l[w.index(i)]
        dicl_ind[i] = w.index(i)
    # print(dicl_ind)

    hit = 0
    s = 2
    while s <= n:
        while dicl_ind[s-1] >= dicl_ind[s]:
            dicl_ind[s] +=  dicl_l[s]
            hit += 1
        s += 1
        # print(dicl_ind)
    
    print(hit)
