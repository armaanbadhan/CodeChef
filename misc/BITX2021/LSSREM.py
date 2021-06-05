
s = input().strip()
t = input().strip()

res = 0
temp = 0

for i in range(len(s)):
    if s[i] == t[i]:
        temp += 1
    else:
        res = max(res, temp)
        temp = 0

print(res + 1)
