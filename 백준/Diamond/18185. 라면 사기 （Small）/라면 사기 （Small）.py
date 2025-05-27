n = int(input())
ra = list(map(int,input().split()))

cost = 0
for i in range(n-2):
    three = min(ra[i],ra[i+1],ra[i+2])
    ra[i] -= three
    ra[i+1] -= three
    ra[i+2] -= three
    cost += 7*three

    two = min(ra[i],ra[i+1])
    ra[i] -= two
    ra[i+1] -= two
    cost += 5*two

    one = ra[i]
    ra[i] -= one
    cost += 3*one


    if ra[i+1] > ra[i+2]:
        d = ra[i+1]-ra[i+2]
        re = min(three,d)
        ra[i+2] += re
        cost -= 2*re
    #print(f"{three},{two},{one}")

two = min(ra[-2],ra[-1])
cost += 5*two
cost += 3*(max(ra[-2],ra[-1])-two)

print(cost)