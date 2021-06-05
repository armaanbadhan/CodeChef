
def calc(i, l, var, arr, p):
    if i == l:
        if var:
            arr.append(1)
            arr.append(0)
        else:
            arr.append(0)
            arr.append(1)
        return
    if var:
        calc(i+1, l, 1, arr, p)
        calc(i+1, l, 0, arr, p)
    else:
        calc(i+1, l, 0, arr, p)
        calc(i+1, l, 1, arr, p)

    return arr


l, p = map(int, input().strip().split())

arr = calc(1, l, 0, [], p)
print(arr)
