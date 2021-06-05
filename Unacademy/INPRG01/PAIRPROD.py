
n = int(input())

sum_ = 0
sqsum = 0

for i in range(n):
    ai = int(input())
    sum_ += ai
    sqsum += ai*ai

print(2)
print((sum_*sum_ - sqsum)//2)
