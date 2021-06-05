for _ in range(int(input())):
    n = int(input())
    funny = list(input().strip().split())

    s_funny = set(funny)

    l_fir = []
    l_last = []

    d_fir = {}
    d_last = {}

    for i in funny:
        l_fir.append(i[0])
        l_last.append(i[1:])

        if i[0] in d_fir:
            d_fir[i[0]] += 1
        else:
            d_fir[i[0]] = 1
        
        if i[1:] in d_last:
            d_last[i[1:]] += 1
        else:
            d_last[i[1:]] = 1
    
    print(l_fir)
    print(l_last)
    print(d_fir)
    print(d_last)

    invalid_first_same = n - (len(d_fir))
    invalid_last_same = n - (len(d_last))

    print(invalid_first_same, invalid_last_same)

    total = n*n
    total_funny = n



    ans = total - total_funny - invalid_first_same - invalid_last_same
    print(ans)