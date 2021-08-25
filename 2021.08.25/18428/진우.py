from itertools import combinations
N = int(input())
a = []
X=[]
for i in range(N):
    a.append(list(input().split()))

for i in range(N):
    for j in range(N):
        if a[i][j] == "X":
            X.append([i,j])

cb = list(combinations(X,3))  #세 점을 임의로 뽑기

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(a,x,y,idx):
    if x<0 or x>=N or y<0 or y>=N:
        return True
    elif a[x][y] == "X":
        if not dfs(a, x+dx[idx], y+dy[idx], idx):
            return False
        else:
            return True
    elif a[x][y] == "O":
        return True
    elif a[x][y] == "T":
        return False
    
tf=1

for i in cb:
    for j in range(3):
        x,y = i[j]
        a[x][y] ="O"


    for p in range(N):
        for q in range(N):
            if a[p][q] == "S":
                for k in range(4):
                    if not dfs(a,p+dx[k],q+dy[k],k):
                        tf=0
    if tf==1:
        print("YES")
    
    for j in range(3):
        x,y = i[j]
        a[x][y] = "X"
        
if tf ==0:
    print("NO")
