input()
i = input()
b = i.count("B")
s = i.count("S")
a = i.count("A")

if b == s:
    if b == a:
        print("SCU")
    elif b > a:
        print("BS")
    else:
        print("A")
else:
    if b > s:
        if b > a:
            print("B")
        elif b == a:
            print("BA")
        else:
            print("A")
    else:
        if s > a:
            print("S")
        elif s == a:
            print("SA")
        else:
            print("A")
    