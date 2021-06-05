import sys

sys.stdin = open("output.txt", "r")

arr = []

for i in range(19683):
    arr.append(int(input()))


sys.stdin = open("output2.txt", "r")

for i in range(19683):
    x = int(input())
    if x != arr[i]:
        print(i)
        break
