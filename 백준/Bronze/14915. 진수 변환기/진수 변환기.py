tmp = "0123456789ABCDEFG"
def conversion(n, k):
    q,r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return conversion(q, k) + tmp[r]

print(conversion(*map(int,input().split())))