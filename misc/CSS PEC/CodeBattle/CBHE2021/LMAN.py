
vov = "aeiou"

t = int(input())

for _ in range(t):
    s = "a" + input().strip() + "a"
    res = ""
    for i in range(1, len(s)-1):
        if s[i] not in vov:
            res += s[i]
        elif s[i-1] in vov or s[i+1] in vov:
            res += s[i]
    print(res)
