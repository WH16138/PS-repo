count = 1
while True:
    i = input()
    a, b, c = i.split()
    if b == "E":
        break
    else:
        if eval(i):
            print(f"Case {count}: true")
        else:
            print(f"Case {count}: false")
        count += 1
