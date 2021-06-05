
t = int(input())

for _ in range(t):
    s = input().strip()
    while 'party' in s:
        s = s.replace('party', 'pawri')
    print(s)