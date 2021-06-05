
p, q = map(int, input().strip().split())

i = 0
found = False

while i < q:
    if p*i % q == 1:
        found = True
        break
    i += 1

print(i if found else None)
