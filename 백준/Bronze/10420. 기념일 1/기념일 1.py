y,m,d = 2014, 4, 2
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = int(input())-1

while n:
    n -= 1
    d += 1
    if m == 2 and ((y%4==0 and y%100) or y%400==0):
        if d>29:
            d = 1
            m += 1
    else:
        if d > days[m]:
            d = 1
            m += 1
    if m > 12:
        m = 1
        y += 1
print(f"{y}-{m:02}-{d:02}")