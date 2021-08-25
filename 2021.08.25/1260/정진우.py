from collections import deque
N, M, V = map(int,input().split())
road = dict()
for i in range(M):
    x,y = map(int,input().split())
    if x not in road:
        road[x] = set([y])
    else:
        road[x].add(y)

    if y not in road:
        road[y] = set([x])
    else:
        road[y].add(x)

def dfs(graph,root):
    visited=[]
    stack = [root]
    while stack:
        n=stack.pop()
        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n]-set(visited),reverse=True)
    return visited

def bfs(graph,root):
    visited =[]
    q = deque([root]) 
    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q += graph[n]-set(visited)
    return visited

for i in dfs(road,V):
    print(i, end=" ")
print()
for i in bfs(road,V):
    print(i, end=" ")
