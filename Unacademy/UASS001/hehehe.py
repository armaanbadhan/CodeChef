
def fun(arr, fin, n, i):
    if i > n:
        return
    if len(arr) == n:
        fin.append(arr)
        return
    for i in range(1, 9):
        fun(arr + [i], fin, n, i+1)
    return fin

print(fun([], [], 2, 0))