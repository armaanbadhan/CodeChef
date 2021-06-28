
n, k = map(int, input().strip().split())

if n == 0:
    print(0)
    exit()


inbin = bin(n)[2:]

k = min(k, inbin.count("1"))
tk = k
idx = 0

for i in inbin:
    if i == "1":
        k -= 1
    idx += 1
    if k == 0:
        break

print(int(inbin[idx:] + "1"*tk, 2))
