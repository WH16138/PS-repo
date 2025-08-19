import sys
from decimal import Decimal, getcontext, ROUND_HALF_UP

input = sys.stdin.readline
getcontext().prec = 80

PI = Decimal("3.14159265358979323846264338327950288419716939937510")
TWO_PI = 2*PI

def dec_sin(x):
    z = (x+PI) % TWO_PI - PI
    term = z
    s = z
    k = 1
    z2 = z*z
    tol = Decimal("1e-50")
    while term.copy_abs() > tol:
        term = -term * z2 / (Decimal(2*k) * Decimal(2*k+1))
        s += term
        k += 1
        if k > 1000:
            break
    return s

def cal(a, b, x):
    return a * x + b * dec_sin(x)

def solve(a, b, target):
    l = Decimal(0)
    r = Decimal(10**6)
    error = Decimal("1e-30")
    while r - l > error:
        mid = (l + r) / 2
        if cal(a, b, mid) < target:
            l = mid
        else:
            r = mid
    return (l + r) / 2

x = solve(*map(Decimal, input().split()))
print(x.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))
