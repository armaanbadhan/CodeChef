n=int(input())


for i in range(n):
    no_safe_house=0
    m,x,y=map(int,input().split())

    cop_house_no=list(map(int,input().split()))      #converting the house no. to a list

    cop_house_no.sort()                              #ascending order of house no.

    start=1                                          #house no. 1
    ran = x*y

    for i in range(m):                               # x*y no. of houses can be searched in both direction
        q1 = cop_house_no[i] - ran                   
        q2 = cop_house_no[i] + ran

        if q1>start:             
            no_safe_house += q1 - start - 1
        
        start=q2

    if start<100:
        no_safe_house += 100 - start
    
    print(no_safe_house)
