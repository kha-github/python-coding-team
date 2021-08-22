from collections import deque

n, m, k, x = map(int, input().split(" "))

mylist = [[-1] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split(" "))
  mylist[a].append(b)

visit = [0]*(n+1)

def BFS(start):

  myq = deque([start, ])
  visit[start] = 0

  while myq:
    cur = myq.popleft()
    for idx in range(1, n+1):
      if visit[idx] == 0 and idx in mylist[cur] and visit[cur] <= k:
        myq.append(idx)
        visit[idx] = visit[cur] + 1

BFS(x)

has_result = False
for idx in range(1, len(visit)):
  if visit[idx] == k and idx != x:
    print(idx)
    has_result = True

if not(has_result):
  print("-1")
