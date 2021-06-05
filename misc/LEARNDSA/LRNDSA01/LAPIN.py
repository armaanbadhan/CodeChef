"""n = int(input())

for i in range(n):
    s1 = list(input())
    l = len(s1)

    if sorted(s1[0: l//2]) == sorted(s1[l - (l//2):l]):
        print("YES")
    else:
        print("NO")"""

'''converting string input to list, length of list, sorted function in cpp'''

s = input()
l = len(s)

char_arr = list(s)
l1, l2 = [], []

for i in range(l//2):
    l1.append(char_arr[i])
    l2.append(char_arr[l-i-1])

l1, l2 = sorted(l1), sorted(l2)

if l1 == l2:
    print("YES")
else:
    print("NO")
