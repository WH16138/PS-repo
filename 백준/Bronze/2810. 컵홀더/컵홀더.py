n = int(input())
string = input()

s = string.count('S')
l = string.count('L')
a = s+l//2

if l > 0:
    a += 1
print(a)