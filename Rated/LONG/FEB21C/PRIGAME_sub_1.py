# for subtask 1
# y == 1
# ?using Goldbach's conjecture

t = int(input())
for _ in range(t):
    x, y = map(int, input().strip().split())
    if x == 1 or x == 2:
        print('Chef')
    else:
        print('Divyam')

# python go brrrrr
# gave TLE; cpp counterpart got accepted for sub 1