import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a, b, c, d = map(int, input().split())

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
        if cardA[-1]*b*c*d > maxValue:
            maxValue = cardA[-1]*b*c*d
            maxCard = "A"
            cardValue = cardA[-1]
    if cardB:
        if cardB[-1]*a*c*d > maxValue:
            maxValue = cardB[-1]*a*c*d
            maxCard = "B"
            cardValue = cardB[-1]
    if cardC:
        if cardC[-1]*a*b*d > maxValue:
            maxValue = cardC[-1]*a*b*d
            maxCard = "C"
            cardValue = cardC[-1]
    if cardD:
        if cardD[-1]*a*b*c > maxValue:
            maxValue = cardD[-1]*a*b*c
            maxCard = "D"
            cardValue = cardD[-1]

    if maxCard == "A":
        cardA.pop()
        a += cardValue
    elif maxCard == "B":
        cardB.pop()
        b += cardValue
    elif maxCard == "C":
        cardC.pop()
        c += cardValue
    elif maxCard == "D":
        cardD.pop()
        d += cardValue

    cardUse.append(f"{maxCard} {cardValue}")

print("\n".join(cardUse))