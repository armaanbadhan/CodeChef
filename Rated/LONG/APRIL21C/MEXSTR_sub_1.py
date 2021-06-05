import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())

def p_str(x): sys.stdout.write(x+"\n")

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def solve():
    s = get_inpt()
    l = len(s)
    alll = set(s)
    for i in range(1, (int)(2**l)):
        temp = ""
        for j in range(l):
            if i&(1<<j):
                if temp == "" and s[j] == "0":
                    pass
                else:
                    temp += s[j]
            alll.add(temp)


    i = 0
    while True:
        if bin(i)[2:] not in alll:
            p_str(bin(i)[2:])
            break
        i += 1


t = get_int()

for _ in range(t):
    solve()
