
t = int(input())

for _ in range(t):
    s = input().strip()
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    if len(s)%2 == 0 and len(s)//2 in dic.values():
        print("YES")
    else:
        print("NO")
