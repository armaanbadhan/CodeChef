
tree = {}
MOD = int(1e9 + 7)
calc = lambda x : ((x*x + x)//2)%MOD


class Node: 
    def __init__(self, data=None): 
        self.key = data
        self.child = []


def solve(node, res):
    if tree.get(node) is None:
        return
    res[0] += calc(len(tree[node]))%MOD
    for i in tree[node]:
        solve(i, res)    
    return res


t = int(input())

for _ in range(t):
    n, x = map(int, input().strip().split())
    tree = {}
    for i in range(n-1):
        a, b = map(int, input().strip().split())
        if a in tree:
            tree[a].add(b)
        else:
            tree[a] = {b}
    
    res = solve(1, [1])
    print(*res)

# gcd = parent
# sum minimum gcd*1, gcd*2, ... gcd*last
# 
 