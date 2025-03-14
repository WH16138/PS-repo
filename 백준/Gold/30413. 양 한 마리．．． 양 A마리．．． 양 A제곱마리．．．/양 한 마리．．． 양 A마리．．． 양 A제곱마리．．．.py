q = 10**9 + 7

a,b = map(int,input().split())

if a == 1:
    print(b%q)
    quit()

#분할 정복을 통한 거듭제곱
def exponentiation_by_Squaring(x, n):
    result = 1
    while n:
        if n % 2:
            result = (result * x) % q
        x = pow(x,2,q)
        n //= 2
    return result

# pow(a, b) - 1 
numerator = (exponentiation_by_Squaring(a, b) - 1) % q
# a-1의 역수
denominator_inverse = exponentiation_by_Squaring(a-1, q-2)

result = (numerator * denominator_inverse) % q
print(result)