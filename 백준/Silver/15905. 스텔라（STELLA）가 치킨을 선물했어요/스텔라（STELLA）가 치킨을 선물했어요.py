s = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:(-x[0],x[1]))
print(len(list(filter(lambda x:x[0] == s[4][0], s[4:])))-1)