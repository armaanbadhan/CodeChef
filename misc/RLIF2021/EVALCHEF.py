
t = int(input())

for _ in range(t):
    inp = input()
    s = "print(" + inp + ")"
    exec(s)
