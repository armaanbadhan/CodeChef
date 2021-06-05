import sys

sys.stdout = open("input.txt", "w")
print = sys.stdout.write

def generator(arr, i, final):
    if i == 10:
        final.append(arr)
        arr = []
        return
    generator(arr + ["O"], i+1, final)
    generator(arr + ["X"], i+1, final)
    generator(arr + ["_"], i+1, final)
    return final

res = generator([], 1, [])
j = 1

print(str(len(res)) + "\n")

for i in res:
    print("   " + str(j) + "\n")
    print("".join(i[0:3]) + "\n")
    print("".join(i[3:6]) + "\n")
    print("".join(i[6:9]) + "\n")
    j += 1
