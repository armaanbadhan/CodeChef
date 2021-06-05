
t = int(input())

for _ in range(t):
    u, v = map(int, input().strip().split())
    pos = u + v + 1
    rank = (pos*(pos+1))//2
    rank -= v
    print(rank)
