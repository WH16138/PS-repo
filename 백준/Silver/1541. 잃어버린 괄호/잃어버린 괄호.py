n = [sum(map(int,x.split('+'))) for x in input().split('-')]
print(n[0]-sum(n[1:]))