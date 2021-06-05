
n = input().strip()

ch = int(n[-1])

try:
    ch1 = int(n[-2])
except:
    ch1 = 0

ch1 = ch1%2

num = ch1*10 + ch

if num == 0 or num == 12 or num == 4 or num == 16 or num == 8:
    print(4)
else:
    print(0)
