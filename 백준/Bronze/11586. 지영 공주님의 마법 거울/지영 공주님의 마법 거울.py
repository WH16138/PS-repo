n = int(input())
arr = [input() for i in range(n)]
state = input()
if state == "1":
    for s in arr:
        print(s)
elif state == "2":
    for s in arr:
        print(s[::-1])
else:
    for i in range(n):
        print(arr[-(i+1)])