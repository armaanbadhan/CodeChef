t = int(input())
for asdf in range(t):
    n = int(input())
    ar = list(map(int, input().strip().split(' ')))
    elements_count = {}
    for element in ar:

        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1

    for key, value in elements_count.items():
        if value % 5 != 0:
            print(f"{key}")