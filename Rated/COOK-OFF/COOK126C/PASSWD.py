from re import search
t = int(input())
for asdf in range(t):
    s = input().strip()
    if len(s) < 10:
        print("NO")
        continue
    if not in s:
        print("NO")
        continue
    s = s[1:-1]
    if not search("[A-Z]", s):
        print("NO")
        continue
    if not search("[0-9]", s):
        print("NO")
        continue
    if not (search("@" or "#" or "%" or "?" or "&", s)):
        print("NO")
        continue
    print("YES")