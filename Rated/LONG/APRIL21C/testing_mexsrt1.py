from sys import stdout

t = 20

stdout = open("input.txt", "w")

stdout.write(str(t) + "\n")

for i in range(t):
    stdout.write(bin(i)[2:])
    stdout.write("\n")
