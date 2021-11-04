import sys
w, h = map(int,sys.stdin.readline().split())

cnt = int(sys.stdin.readline())

arr1=[]
for _ in range(cnt):
    arr1.append(list(map(int,sys.stdin.readline().split())))

myPoint = list(map(int,sys.stdin.readline().split()))      #내위치

ans=0   #정답
r=2*h+2*w   #둘레길이

if myPoint[0]==1:            # 현재 나의 위치가 북쪽일때

    for p, l in arr1:
        if p == 1:             #북
            ans+=abs(myPoint[1]-l)
        elif p == 2:           #남
            ans+=min(h+myPoint[1]+l,r-(h+myPoint[1]+l))
        elif p == 3:           #서
            ans+= l + myPoint[1]
        else:                  #동
            ans+= l + (w-myPoint[1])

elif myPoint[0]==2:            # 현재 나의 위치가 남쪽일때

    for p, l in arr1:

        if p == 1:  # 북
            ans += min(h + myPoint[1] + l, r - (h + myPoint[1] + l))
        elif p == 2:  # 남
            ans += abs(myPoint[1] - l)

        elif p == 3:  # 서
            ans += (h-l) + myPoint[1]
        else:  # 동
            ans += (h-l) + (w - myPoint[1])

elif myPoint[0]==3:               # 현재 나의 위치가 서쪽일때

    for p, l in arr1:
        if p == 1:  # 북
            ans += myPoint[1]+l
        elif p == 2:  # 남
            ans += (h-myPoint[1])+l
        elif p == 3:  # 서
            ans += abs(myPoint[1] - l)
        else:  # 동
            ans += min(l + myPoint[1] + w, r - (w + myPoint[1] + l))

else:                               # 현재 나의 위치가 동쪽일때

    for p, l in arr1:
        if p == 1:  # 북
            ans += (w-l) + myPoint[1]
        elif p == 2:  # 남
            ans += (w-l)+(h-myPoint[1])
        elif p == 3:  # 서
            ans += min(l + myPoint[1] + w, r - (w + myPoint[1] + l))
        else:  # 동
            ans += abs(myPoint[1] - l)


print(ans)
#print(arr1)
