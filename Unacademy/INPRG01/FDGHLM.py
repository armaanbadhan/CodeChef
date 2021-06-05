
def compute_hcf(x, y):
   while y:
       x, y = y, x % y
   return x

a, b = map(int, input().strip().split())

hcf = compute_hcf(a, b)
lcm = a*b//hcf

print(hcf, lcm)
