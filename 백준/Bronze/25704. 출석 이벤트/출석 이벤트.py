N = int(input())
P = int(input())
price = [P]
if N >= 5:
    price.append(P - 500)
if N >= 10:
    price.append(P *0.9)
if N >= 15:
    price.append(P -2000)
if N >= 20:
    price.append(P * 0.75)
print(max(0,int(min(price))))