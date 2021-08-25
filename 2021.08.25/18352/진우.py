from collections import deque
q = deque()
N, M, K, X = map(int, input().split())
A={}
for _ in range(M):
    x,y = map(int, input().split())
    if x in A:
        A[x].append(y)
    else:
        A[x] = [y]        
# A = {1: [2, 3], 2: [3, 4]}

def bfs(x,k):
    visited = [False] * (N+1)
    q.append(x)
    visited[x] = True
    while k>0:
        if not q:
            break
        x = q.popleft()
        if x in A:
            for w in A[x]:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
                else:
                    visited[w] = False
            k = k-1
            
    if q:
        while True:
            if visited[q[0]] ==False:
                q.popleft()
            else:
                break
    return

bfs(X,K)

if q:
    for i in q:
        print(i)
else:
    print(-1)
