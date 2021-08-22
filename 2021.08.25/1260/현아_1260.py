from collections import deque

n, m, v = map(int, input().split(" "))

mylist = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split(" "))
  mylist[a][b] = mylist[b][a] = 1

visit = [0]*(n+1)

def DFS(node):
  print(node, end=' ')
  visit[node] = 1
  for idx in range(1, n+1):
    if visit[idx] != 1 and mylist[node][idx] == 1:
      DFS(idx)

def BFS(first):
  myq = deque([first, ])
  visit[first] = 0

  while myq:
    cur = myq.popleft()
    print(cur, end=' ')
    for idx in range(1, n+1):
      if visit[idx] != 0 and mylist[cur][idx] == 1:
        myq.append(idx)
        visit[idx] = 0

DFS(v)
print("")
BFS(v)
