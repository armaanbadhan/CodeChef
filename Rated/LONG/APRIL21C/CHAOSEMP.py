
t, q, d = map(int, input().strip().split())

for _ in range(t):
    print(1, 0, 0)
    inter = input().strip()
    xhi, xlo = -int(2e18), int(2e18)
    yhi, ylo = -int(2e18), int(2e18)
    xmid = (xhi + xlo)//2
    ymid = (yhi + ylo)//2
    while inter != "O":
        if inter[0] == "P":
            xlo = xmid + 1 
        if inter[0] == "N":
            xhi = xmid - 1
        
        if inter[1] == "P":
            ylo = ymid + 1
        if inter[1] == "N":
            yhi = ymid - 1
        
        xmid = (xhi + xlo)//2
        ymid = (yhi + ylo)//2
        print(1, xmid, ymid)
        inter = input().strip()
