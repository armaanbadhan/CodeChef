def convert(str):
    str = str.replace(":", "").replace(" ", "")
    if str[-2] == "P":
        if str[:2] == "12":
            return int(str[:4])
        return int(str[:4]) + 1200
    else:
        if str[:2] == "12":
            return int(str[2:4])
        return int(str[:4])

t = int(input())
for _ in range(t):
    time_ = convert(input().strip())
    final_ = ""
    n = int(input())
    for asdf in range(n):
        a = input()
        t1 = a[:9]
        t2 = a[-9:]
        if convert(t1.strip()) <= time_ <= convert(t2.strip()):
            final_ += "1"
        else:
            final_ += "0"
    print(final_)
# converting time to int and comparing