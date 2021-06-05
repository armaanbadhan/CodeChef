
s = int(input())

b = bin(s)[2:]

res = 0

for i in b:
    if i == "1":
        res += 1

print(res)
