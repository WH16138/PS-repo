import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A, B, C, D = map(int, input().split())

a = B*C*D
b = A*C*D
c = A*B*D
d = A*B*C

cardA = []
cardB = []
cardC = []
cardD = []

for i in range(N):
    T, U = input().split()
    U = int(U)
    if T == "A":
        cardA.append(U)
    elif T == "B":
        cardB.append(U)
    elif T == "C":
        cardC.append(U)
    elif T == "D":
        cardD.append(U)

cardA.sort()
cardB.sort()
cardC.sort()
cardD.sort()

cardUse = []
for i in range(K):
    maxValue = 0
    maxCard = "?"
    cardValue = 0
    if cardA:
        if cardA[-1]*a > maxValue:
            maxValue = cardA[-1]*a
            maxCard = "A"
            cardValue = cardA[-1]
    if cardB:
        if cardB[-1]*b > maxValue:
            maxValue = cardB[-1]*b
            maxCard = "B"
            cardValue = cardB[-1]
    if cardC:
        if cardC[-1]*c > maxValue:
            maxValue = cardC[-1]*c
            maxCard = "C"
            cardValue = cardC[-1]
    if cardD:
        if cardD[-1]*d > maxValue:
            maxValue = cardD[-1]*d
            maxCard = "D"
            cardValue = cardD[-1]

    if maxCard == "A":
        cardA.pop()
        b += a
        c += a
        d += a
    elif maxCard == "B":
        cardB.pop()
        a += b
        c += b
        d += b
    elif maxCard == "C":
        cardC.pop()
        a += c
        b += c  
        d += c
    elif maxCard == "D":
        cardD.pop()
        a += d  
        b += d
        c += d

    cardUse.append(f"{maxCard} {cardValue}")

print("\n".join(cardUse))