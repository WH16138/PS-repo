s = input()
h = s.count(":-)")
s = s.count(":-(")
if h == s:
    if h == 0:
        print("none")
    else:
        print("unsure")
elif h>s:
    print("happy")
else:
    print("sad")