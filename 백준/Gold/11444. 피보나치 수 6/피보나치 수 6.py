import sys
sys.setrecursionlimit(100000)
N = int(input())
p = 1000000007

def multiply(A,B):
    row = len(A)
    C = [[0]*row for _ in range(row)]

    for r in range(row):
        for c in range(row):
            s = 0
            for k in range(row):
                s += (A[r][k] * B[k][c])
            C[r][c] = s%p
    
    return C

def square(A, n):
    if n == 1:
        return A
    
    temp = square(A, n//2)
    if n%2:
        return multiply(multiply(temp, temp), A)
    else:
        return multiply(temp, temp)
    
fib_matrix = [[1,1],[1,0]]
print(square(fib_matrix,N)[0][1])