i = sorted(list(map(int,input().split())))
print(i[0]+i[1]+min(i[0]+i[1]-1,i[2]))