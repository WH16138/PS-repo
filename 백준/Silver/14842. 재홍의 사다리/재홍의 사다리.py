W,H,N = map(int,input().split())
def s(x):return H*abs(1-2*x/N)
print((N//2)*(s(N//2)+s(1)))