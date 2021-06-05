t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    ranks = list(map(int, input().strip().split()))
    student = list(map(int, input().strip().split()))
    for i in range(m):
        