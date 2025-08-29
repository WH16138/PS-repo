r = 31
M = 1234567891
def Hash(s):
    return sum((ord(c)-ord("a")+1)*(r**i) for i,c in enumerate(s))
input()
print(Hash(input()))