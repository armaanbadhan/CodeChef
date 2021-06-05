t = int(input())
for _ in range(t):
    n = int(input())
    i = int(((8*n + 1)**0.5 - 1)/2)           
    print((i*(i+1)*(2*i + 1)//6) + (i+1)*(n - i*(i+1)//2))


"""
t = int(input())
for _ in range(t):
    n = int(input())
    i = int(((8*n + 1)**0.5 - 1)/2)     # ith term
    sum = i*(i+1)*(2*i + 1)//6          # sum till ith term    # formula for summision n**2
    x = n - i*(i+1)//2                  # extra numbers remaining with value (i+1)
                                        # numbers till ith term are 1(1 time) + 1(2 times) + ... + 1(i times)
    diff = (i+1)*x                      # multiplying the extra numbers with (i+1)
    print(sum + diff)                   # final sum
"""

"""
brute
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    cnt = 1
    final = 0
    while n:
        if ans == cnt:
            cnt += 1
            ans = 0
        ans += 1
        final += cnt
        n -= 1
    print(final)
"""