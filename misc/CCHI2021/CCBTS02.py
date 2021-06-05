
t = int(input())

for _ in range(t):
    n = int(input())
    myarr = input().strip().split()
    running = False
    error = False
    for i in myarr:
        if i == 'start':
            running = True
        elif i == 'restart':
            running = True
        else:
            if running == False:
                error = True
                break
            running = False
    if error:
        print(404)
    else:
        print(200)
