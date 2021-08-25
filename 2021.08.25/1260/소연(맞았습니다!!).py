from collections import deque

n, m, v = map(int, input().split())
array = [[0]* (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[b][a] = 1
    
dstack = [v]
dfs = []
while dstack:
    s = dstack.pop()
    if s not in dfs:
        dfs.append(s)
        for i in range(n, -1, -1):
            if array[s][i]:
                dstack.append(i)
for i in dfs:
    print(i, end=' ')
print()
bque = deque([v])
bfs = [v]
while bque:
    s = bque.popleft()
    for i in range(n + 1):
        if i not in bfs and array[s][i]:
            bque.append(i)
            bfs.append(i)
for i in bfs:
    print(i, end=' ')
