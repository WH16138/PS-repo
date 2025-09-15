A,B,C = map(int,input().split())
i,j,k = map(int,input().split())

mc = min(A/i,B/j,C/k)
print(A-mc*i, B-mc*j, C-mc*k)