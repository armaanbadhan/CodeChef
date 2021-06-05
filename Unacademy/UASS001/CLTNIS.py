
def good(mid, bounds__, position, velocity, chef_pos, n):
    return True



t = int(input())

for _ in range(t):
    n = int(input())
    bounds__ = list(map(int, input().strip().split()))
    position = list(map(int, input().strip().split()))
    velocity = list(map(int, input().strip().split()))
    chef_pos = list(map(int, input().strip().split()))
    
    lo, hi = 0, int(1e10)

    for j in range(200):
        mid = (lo+hi)//2
        if good(mid, bounds__, position, velocity, chef_pos, n):
            hi = mid - 1
        else:
            lo = mid + 1
    print(lo)

# WA hehehe
