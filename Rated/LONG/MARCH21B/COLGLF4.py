
def good(x, e, h, a, b, c, n):
    '''e -> eggs, h -> chocolate, given'''
    '''
    2 eggs to make an omelette
    3 chocolate bars for a chocolate milkshake
    1 egg and 1 chocolate bar for a chocolate cake
    '''
    '''e, h -> items(min n) -> price(cacl and check if less than x) -> '''
    '''omelette -> a, chocolate milkshake -> b, chocolate cake -> c'''
    ome = 0
    milk = 0
    cake = 0
    min_price = ome*a + milk*b + cake*c
    items = ome + milk + cake
    boo = n >= items
    return min_price <= x, boo


t = int(input())

for _ in range(t):
    n, e, h, a, b, c = map(int, input().strip().split())
    lo = -1
    hi = int(1e20)
    while lo < hi:
        mid = (lo + hi)/2
        if good(mid, e, h, a, b, c, n):
            hi = mid - 1
        else:
            lo = mid + 1
