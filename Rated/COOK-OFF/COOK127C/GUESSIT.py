
i = 1

arr = []

while i*i <= 1000000:
    arr.append(i*i)
    i += 1


t = int(input())

for _ in range(t):
    print(1)
    j = 1
    while True:
        inp = input().strip()
        if inp == '-1':
            exit()
        if inp == '1':
            break
        print(arr[j])
        j += 1