
n = int(input())

cnt = 0

for i in range(n):
    if i&1:
        print(cnt+5, cnt+4, cnt+3, cnt+2, cnt+1)
    else:
        print(cnt+1 ,cnt+2, cnt+3, cnt+4, cnt+5)
    cnt += 5