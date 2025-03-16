n,m = map(int,input().split())

order = []
result = []

for i in range(n):
    order.insert(int(input())-1, i+1)

for o in order[m-1::-1]:
    result.insert(int(input())-1, o)

for o in result[:3]:
    print(o)