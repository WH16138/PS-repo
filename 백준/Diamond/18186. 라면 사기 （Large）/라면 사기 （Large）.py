n, b, c = map(int,input().split())
ra = list(map(int,input().split()))

if b <= c:
    print(b*sum(ra))
    exit()

cost = 0
for i in range(n-2):
    three = min(ra[i],ra[i+1],ra[i+2])
    ra[i] -= three
    ra[i+1] -= three
    ra[i+2] -= three
    cost += (b+2*c)*three

    two = min(ra[i],ra[i+1])
    ra[i] -= two
    ra[i+1] -= two
    cost += (b+c)*two

    one = ra[i]
    ra[i] -= one
    cost += b*one


    if ra[i+1] > ra[i+2]:
        d = ra[i+1]-ra[i+2]
        re = min(three,d)
        ra[i+2] += re
        cost -= c*re
    #print(f"{three},{two},{one}")

two = min(ra[-2],ra[-1])
cost += (b+c)*two
cost += b*(max(ra[-2],ra[-1])-two)

print(cost)