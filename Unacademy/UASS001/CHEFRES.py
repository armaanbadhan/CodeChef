from bisect import bisect_right

t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    n_ar = []
    m_ar = []
    for i in range(n):
        x, y = map(int, input().strip().split())
        n_ar.append([x, y])
    for j in range(m):
        m_ar.append(int(input()))
    time = [0]*max(m_ar)
    for i in n_ar:
        time[i[0]] += 1
        time[i[1]] -= 1
    
    print(time)

    for i in range(len(time)-1):
        time[i] += time[i-1]
    
    print(time)
    print([i for i in range(len(time))])

    n_ar.sort()
    print(n_ar)
    print(m_ar)
