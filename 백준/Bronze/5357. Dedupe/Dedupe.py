for i in range(int(input())):
    s = input()
    char = ''
    result = ''
    for c in s:
        if c != char:
            char = c
            result += c
    print(result)