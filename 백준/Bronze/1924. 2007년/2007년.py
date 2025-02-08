days = [31,28,31,30,31,30,31,31,30,31,30,31]

m,d = map(int,input().split())
while m > 1:
    d += days[m-2]
    m -= 1
print(['SUN','MON','TUE','WED','THU','FRI','SAT'][d%7])