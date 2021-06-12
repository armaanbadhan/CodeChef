
t = int(input())

for _ in range(t):
    try:
        n = int(input())
        s = input().strip()
        cnt = 0
        for i in s:
            if i == "*":
                cnt += 1
        pos = 0
        temp = 0
        for i in range(len(s)):
            if s[i] == "*":
                if temp == cnt//2:
                    pos = i
                temp += 1
        res = 0
        cur = pos - cnt//2
        for i in range(len(s)):
            if s[i] == "*":
                res += abs(cur - i)
                cur += 1
        print(res)
    except:
        pass
