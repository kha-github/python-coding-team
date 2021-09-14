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

visit = [0] * (N+1)

def bfs(x,k):
    q.append(x)
    while q:
        cur = q.popleft()
        for idx in range(1,N+1):
            if visit[idx] == 0 and cur in A and visit[cur] <= k:
                if idx in A[cur]:
                    q.append(idx)
                    visit[idx] = visit[cur]+1

bfs(X,K)

result = False
for idx in range(1,N+1):
    if visit[idx] == K and idx !=X:
        print(idx)
        result = True

if not(result):
    print(-1)
