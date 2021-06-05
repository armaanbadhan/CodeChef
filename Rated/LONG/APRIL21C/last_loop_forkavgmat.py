
n, m = map(int, input().strip().split())

arr = []
for i in range(n):
    temp = list(map(int, input().strip().split()))
    arr.append(temp)



for i in range(n-1, -1, -1):
    # check for min(n-i, m) elements
    # first element is arr[i][0]
    # gen element is arr[i+k][k]
    for j in range(min(n-i, m)):
        print(arr[i+j][j], end=' ')
    print()

for i in range(1, m):
    for j in range(min(n, m-i)):
        print(arr[j][i+j], end=' ')
    print()

# bullshit
