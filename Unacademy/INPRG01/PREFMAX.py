
n = int(input())

max_ = 0
res = 0

for i in range(n):
    ai = int(input())
    if ai > max_:
        max_ = ai
        res += 1

print(2)
print(res)
