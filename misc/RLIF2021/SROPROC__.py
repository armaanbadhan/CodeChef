import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

# for sub 1 -> t = 1, n = 1, p = 0, straight line?

for _ in range(t):
    n, p = map(int, input().strip().split())
    # n -> planets, p -> gravity till
    for i in range(n):
        xi, yi = map(int, input().strip().split())
    print("Yes")
    print("Yes")
    print(round(yi/xi, 1), 0.0 if yi else 0.0)
    print(1 if yi else 0)

# cost -> highest power
