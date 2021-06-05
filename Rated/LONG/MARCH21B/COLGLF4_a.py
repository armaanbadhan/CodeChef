
def good():
    return
    # good if => 



t = int(input())

for _ in range(t):
    n, e, h, a, b, c = map(int, input().strip().split())
    cost = 0
    while not good(cost):
        cost += 1
    print(cost-1)
