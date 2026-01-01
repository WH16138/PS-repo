for i in range(int(input())):
  n = (int(input())-1)%28+1
  bit = min(n,30-n)
  print(bin(bit)[2:].zfill(4).replace("0","V").replace("1","딸기"))