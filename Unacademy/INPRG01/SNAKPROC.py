
t = int(input())

for _ in range(t):
    l = int(input())
    proc = input().strip()
    arr = []
    for i in proc:
        if i != '.':
            arr.append(i)
    comp = ["H", "T"]*(len(arr)//2)
    if arr == comp:
        print("Valid")
    else:
        print("Invalid")
