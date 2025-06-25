import sys
from decimal import Decimal as D
from decimal import getcontext, ROUND_DOWN
getcontext().prec = 1000
input = sys.stdin.readline

for i in range(int(input().strip())):
    n = D(input())
    a = n ** (D(1)/D(3)) + D(10)**D(-200)
    print(a.quantize(D('1.0000000000'), rounding=ROUND_DOWN))