input()
i = input()
s = i.count('s')
b = i.count('b')

if s == b:
    print("bigdata? security!")
elif s > b:
    print("security!")
else:
    print("bigdata?")