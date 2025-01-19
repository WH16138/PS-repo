s = input()
n = len(s)

l = []

for i in range(1,n-1):
    for j in range(i+1,n):
        l.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])
        
print(sorted(l)[0])