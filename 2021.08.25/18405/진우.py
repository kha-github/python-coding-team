from collections import deque
N,k = map(int,input().split())
test=[]
vi=[]
for i in range(N):
    test.append(list(map(int,input().split())))
    for j in range(N):
        if test[i][j] != 0:
            vi.append([test[i][j],i+1,j+1,0]) #바이러스값, x좌표, y좌표, 카운트

S,X,Y = map(int,input().split())


vi.sort()
q = deque(vi)


dx = [-1,1,0,0]
dy = [0,0,-1,1]


while q:
    a=q.popleft()
    if a[3]==S:
        break
    for i in range(4):
        x = a[1]+dx[i]
        y = a[2]+dy[i]
        if 0<x<=N and 0<y<=N: #움직인 좌표가 표안에 존재
            if test[x-1][y-1]==0: #동시에 좌표에 바이러스가 감염되지 않았다면
                test[x-1][y-1]=a[0] #해당 좌표를 해당바이러스로 감염
                q.append([a[0],x,y,a[3]+1]) #해당 바이러스 정보를 새로운 좌표 및 카운트로 큐에 삽입

print(test[X-1][Y-1])
