t=int(input())
i=0
while i<t:
    i+=1 
    n=int(input())
    y=list(map(int, input().split()))
    
    a=0 
    sum=0
    print(y[0])
    while a<n:
        b=0 
        if a==b:
            b+=1 
        while b<n:
            x=(y[a])*(y[b])  
            s=0
            while x>0:
                z=x%10
                s=s+z
                x=x//10
            if s>sum:
                sum=s
                
            b+=1 
        a+=1 
    print(sum)
