t = int(input())
for _ in range(t):
    n = input()
    l = list(map(int, input().strip().split()))
    print(2*max(l) - 2*min(l))
# |max - x| + |x - min| = max - min = const for every x b/w [min, max]