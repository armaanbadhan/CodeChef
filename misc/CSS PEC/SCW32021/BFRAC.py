import decimal

num, den, k, n  = map(int, input().strip().split())

if k == 0 or num == 0:
    print(0)
    exit()

decimal.getcontext().prec = 10000005

res = decimal.Decimal(num/den)
res = str(res)

if "." in res:
    res = res.split(".")[1][:k]
    print(int(res)%n)
else:
    print(0)

# WA
