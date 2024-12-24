A = []
B = []
for i in range(5):
    A.append(list(map(int, input().split())))
for i in range(5):
    B.append(list(map(int, input().split())))

C = [0]*5

for x in range(5):
    for y in range(5):
        for i in range(5):
            C[x] += A[x][i] * B[i][y]

name = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
C.reverse()
name.reverse()
print(name[C.index(min(C),)])