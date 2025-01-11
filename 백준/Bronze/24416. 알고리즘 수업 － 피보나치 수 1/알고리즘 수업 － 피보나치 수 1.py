fibo = [1,1]

n = int(input())
for i in range(2,n):
    fibo.append(fibo[-1]+fibo[-2])

print(fibo[-1], n-2)