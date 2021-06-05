from math import ceil
calc = lambda x, y : ceil((x- y)/60)

n = int(input())

main = {}
res = 0

for i in range(n):
    event = input().strip()
    plate = input().strip()
    time = int(input().strip())
    if event == "entry":
        main[plate] = time
    else:
        res += (calc(time, main[plate])+1)*30

print(res)