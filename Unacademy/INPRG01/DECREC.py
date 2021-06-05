from itertools import permutations

w = int(input())
words = set()
for i in range(w):
    words.add(input().strip())
encrypted = list(input().strip().split())

ll = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in permutations(ll):
    key = {}
    res = []
    found = True
    for j in range(8):
        key[ll[j]] = i[j]
    for k in encrypted:
        temp_word = ""
        for l in k:
            if l in key:
                temp_word += key[l]
            else:
                temp_word += l
        if temp_word in words:
            res.append(temp_word)
        else:
            found = False
            break
    if found:
        print(*res)
        break
