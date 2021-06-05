
n, m = map(int, input().strip().split())

cross = []

for i in range(n):
    cross.append(input().strip())

w = int(input())

words = {}

for i in range(w):
    x = input().strip()
    words[len(x)] = x

horizontal_x_y_start = []
# finding all horizontal points and length
for i in range(n):
    cnt = 0
    flag = False
    for j in range(m):
        if cross[i][j] == 'b' or cross[i][j] == 'r':
            cnt += 1
            if not flag:
                horizontal_x_y_start.append([i, j])
                flag = True
            else:
                horizontal_x_y_start[-1].append(cnt)
                cnt = 0
                flag = False
        elif flag and (cross[i][j] == '.' or cross[i][j] == 'c'):
            cnt += 1

verticle_x_y_start = []
# verticals points with length
for i in range(m):
    cnt = 0
    flag = False
    for j in range(n):
        if cross[j][i] == 'b' or cross[j][i] == 'c':
            cnt += 1
            if not flag:
                verticle_x_y_start.append([j, i])
                flag = True
            else:
                verticle_x_y_start[-1].append(cnt)
                cnt = 0
                flag = False
        elif flag and (cross[j][i] == '.' or cross[j][i] == 'r'):
            cnt += 1


resh = []
# filling all horizontal words
i = 0
while i < n:
    j = 0
    temp = []
    while j < m:
        ele = cross[i][j]
        if ele == '#':
            temp.append('#')
            j += 1
        elif ele == 'b' or ele == 'r':
            for k in horizontal_x_y_start:
                if k[0] == i and k[1] == j:
                    leng = k[2]
                    horizontal_x_y_start.remove([i, j, leng])
                    char_cnt = 0
                    while char_cnt < leng:
                        temp.append(words[leng][char_cnt])
                        j += 1
                        char_cnt += 1
                    del words[leng]
        else:
            temp.append('-')
            j += 1
    resh.append(''.join(temp))
    i += 1


resv = []
# filling all verticaal words
i = 0
while i < m:
    j = 0
    temp = []
    while j < n:
        ele = cross[j][i]
        if ele == '#':
            temp.append('#')
            j += 1
        elif ele == 'b' or ele == 'c':
            for k in verticle_x_y_start:
                if k[0] == j and k[1] == i:
                    leng = k[2]
                    verticle_x_y_start.remove([j, i, leng])
                    char_cnt = 0
                    while char_cnt < leng:
                        temp.append(words[leng][char_cnt])
                        j += 1
                        char_cnt += 1
                    del words[leng]
        else:
            temp.append('-')
            j += 1
    resv.append(''.join(temp))
    i += 1


transposed = []
# cross word with verticle words is transposed
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(resv[j][i])
    transposed.append(''.join(temp))


res = [] # final

for i in range(n):
    temp_res = ""
    for j in range(m):
        hh = resh[i][j]
        vv = transposed[i][j]
        if hh == vv:
            temp_res += hh
        elif (hh == '-') and (vv in "qwertyuiopasdfghjklzxcvbnm"):
            temp_res += vv
        elif (vv == '-') and (hh in "qwertyuiopasdfghjklzxcvbnm"):
            temp_res += hh
        else:
            print('Invalid')
            exit()
    res.append(temp_res)

for i in res:
    print(i)
