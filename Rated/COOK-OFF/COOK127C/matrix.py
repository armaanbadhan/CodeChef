
n = int(input())
m = int(input())
main = set()
for i in range(1, n+1):
    for j in range(1, m+1):
        if i+j in main:
            main.remove(i+j)
        else:
            main.add(i+j)

print(*sorted(list(main)))
