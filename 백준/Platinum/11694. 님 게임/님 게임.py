n = int(input())
s = list(map(int,input().split()))
if len(s)==1:
    print("cubelover" if s[0]==1 else "koosaga")
elif all(x==1 for x in s):
    print("koosaga" if n%2==0 else "cubelover")
else:
    xor = 0
    for i in s:
        xor ^= i
    print("koosaga" if xor else "cubelover")