N = int(input())
tree = {}
for i in range(N):
    p,l,r = input().split()
    tree[p] = (l,r)

def solL(m):
    if m == '.':
        return ""
    l,r = tree[m]
    return m+solL(l)+solL(r)  

def solM(m):
    if m == '.':
        return ""
    l,r = tree[m]
    return solM(l)+m+solM(r)

def solR(m):
    if m == '.':
        return ""
    l,r = tree[m]
    return solR(l)+solR(r)+m 

print(solL('A'))
print(solM('A'))
print(solR('A'))