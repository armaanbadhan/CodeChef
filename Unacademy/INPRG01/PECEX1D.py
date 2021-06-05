
def ways(n, x, level, steps, res):
    if level < 0 or level > n:
        return                      # wrong path
    if steps >= x:                  # no more steps
        if level == 0:              # when stps completed and at final position
            res[0] += 1             # add to ans, using a list as they are passed by reference
        return 0                    # will return to line 27 if x == 0
    
    for j in range(-3, 4):
        ways(n, x, level-j, steps+1, res)

    return res[0]


t = int(input())

for _ in range(t):
    n, x = map(int, input().strip().split())
    if (n, x) == (0, 0):
        print(1)
    else:
        print(ways(n, x, n, 0, [0]))