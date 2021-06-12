
t = int(input())

for _ in range(t):
    s = input().strip()
    if "9" in set(s) or "4" in set(s):
        print(0)
    else:
        i = 1
        cnt = 0
        while i < len(s):
            if s[i-1:i+1] == "22" or s[i-1:i+1] == "33":
                cnt += 1
                i += 1
            i += 1
        print(2**(cnt % int(1e9 + 6)) % int(1e9 + 7))
