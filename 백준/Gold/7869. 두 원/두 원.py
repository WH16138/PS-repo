import math as m
x1,y1,r1,x2,y2,r2 = map(float,input().split())

d = m.dist((x1,y1),(x2,y2))
if d > r1+r2 or r1 == 0 or r2 == 0:
    print('0.000')
elif d > abs(r1-r2):
    a1 = 2*m.acos((d**2+r1**2-r2**2)/(2*d*r1))
    a2 = 2*m.acos((d**2+r2**2-r1**2)/(2*d*r2))
    S1 = 0.5*r1**2*a1+0.5*r2**2*a2
    S2 = 0.5*r1**2*m.sin(a1) + 0.5*r2**2*m.sin(a2)
    S = S1-S2
    print(f'{S:.03f}')
else:
    print(f'{m.pi*min(r1,r2)**2:.03f}')