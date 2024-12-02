n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def rsp(win,new):
    if (win == 3 and new == 2) or (win == 2 and new == 1) or (win == 1 and new == 3):
        return True
    else:
        return False

maxseq = 1
seq = 1
win = None
for a,b in zip(A,B):
    if win == None:
        if rsp(a,b):
            win = True
        else:
            win = False
    elif win:
        if rsp(a,b):
            seq += 1
            maxseq = max(maxseq,seq)
        else:
            win = False
            seq = 1
    else:
        if rsp(b,a):
            seq += 1
            maxseq = max(maxseq,seq)
        else:
            win = True
            seq = 1

print(maxseq)