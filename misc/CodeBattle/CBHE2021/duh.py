from random import randint
for i in range(100):
    base = randint(1, 10)
    exp = randint(3, 10)
    mod = randint(2, exp)

    if not  ((base**exp) % mod ) == (base**(exp%(mod-1)))%mod:
        print(f"{base}^{exp}, {mod}")
