l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

if l1[0]==l1[2]: #직선1이 y축 평행
    if l2[0]==l2[2]: #직선2도 y축 평행
        print(int(l1[0]==l2[0] and max(l1[1],l1[3])>min(l2[1],l2[3]) and min(l1[1],l1[3])<max(l2[1],l2[3])))
    else:
        dx2 = (l2[3]-l2[1])/(l2[2]-l2[0])
        c2 =  l2[1]-l2[0]*dx2
        print(int(min(l2[0],l2[2])<l1[0]<max(l2[0],l2[2]) and min(l1[1],l1[3])<l1[0]*dx2+c2<max(l1[1],l1[3])))
elif l2[0]==l2[2]: #직선2이 y축 평행
    dx1= (l1[3]-l1[1])/(l1[2]-l1[0])
    c1 = l1[1]-l1[0]*dx1
    print(int(min(l1[0],l1[2])<l2[0]<max(l1[0],l1[2]) and min(l2[1],l2[3])<l2[0]*dx1+c1<max(l2[1],l2[3])))
else:
    dx1= (l1[3]-l1[1])/(l1[2]-l1[0])
    c1 = l1[1]-l1[0]*dx1
    dx2 = (l2[3]-l2[1])/(l2[2]-l2[0])
    c2 =  l2[1]-l2[0]*dx2
    if dx1 == dx2: #두 직선 평행
        print(int(c1==c2 and max(l1[1],l1[3])>min(l2[1],l2[3]) and min(l1[1],l1[3])<max(l2[1],l2[3])))
    else:
        x = (c2-c1)/(dx1-dx2) #교점
        print(int(min(l1[0],l1[2])<x<max(l1[0],l1[2]) and min(l2[0],l2[2])<x<max(l2[0],l2[2])))