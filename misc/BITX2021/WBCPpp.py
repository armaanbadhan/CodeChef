while True:
    n = int(input())

    b = 2**n % 5
    c = 3**n % 5
    d = 4**n % 5

    print((1+b+c+d) % 5)

# TLE

