
n, y, x = map(int, input().strip().split())

arr = [1]
new = [1]

# for i in range(1, 10): # tle?
#     temp = arr[-1] * x
#     arr.append(temp + arr[-1])
#     new.append(temp)
#     l = len(arr)
#     if l > y:
#         arr[-1] -= new[l - y - 1]


def solve(q):
    if len(arr) > q:
        print(arr[q])
        return
    for i in range(len(arr), q+1):
        temp = arr[-1] * x
        arr.append(temp + arr[-1])
        new.append(temp)
        l = len(arr)
        if l > y:
            arr[-1] -= new[l - y - 1]
    print(arr[q])


# print("tle goes brr")

# print(new, "new patients on ith day")
# pref = [1] + [new[i-1] + new[i] for i in range(1, len(new))]
# print(pref, "prefix sum of new, is equal to arr")
# print(arr, "res")
# pow = [x**i for i in range(10)]
# print(pow, "powers")
# pref = [1] + [pow[i-1] + pow[i] for i in range(1, len(new))]
# print(pref, "prefix of powers")

# exit()

for i in range(n):
    di = int(input())
    solve(di - 1)

# TLE lol

# answer all quieries ar once :pepecool:
