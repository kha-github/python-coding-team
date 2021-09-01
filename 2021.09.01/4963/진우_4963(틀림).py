w,h = map(int, input().split())
answer = []
while w !=0 or h != 0:
    isl = []
    ans = [[False]*w]*h
    for i in range(h):
        a=list(map(int, input().split()))
        if len(a) != w:
            break
        isl.append(a)
    
    dw = [1,1,1,0,0,-1,-1,-1]
    dh = [0,1,-1,1,-1,1,0,-1]
    cnt = 0
    ev = 0
    for i in range(h):
        for j in range(w):
            if isl[i][j] == 1:
                ev += 1
                ans[i][j] = True
                for p in range(8):
                    x = i + dh[p]
                    y = j + dw[p]
                    if x < 0 or x>=h or y<0 or y>=w:
                        continue
                    if isl[x][y] == 1 and ans[x][y] == False:
                        cnt += 1
                        ans[x][y] = True
    answer.append(ev-cnt)
    w,h = map(int, input().split())
    
#뭐가 문제지....
for i in answer:
    print(i)
