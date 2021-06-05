t = int(input())
for asdf in range(t):
    a, b = map(int, input().strip().split(" "))
    print(2*(b-a) + 1)