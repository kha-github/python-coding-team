from collections import deque

n = int(input())
k = int(input())

mylist = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
  a, b = map(int, input().split())
  mylist[a][b] = 1
  mylist[b][a] = 1

def BFS(start):
  myq = deque([start, ])
  visit = [0]*(n+1)
  result = 0
  
  while myq:
    cur = myq.popleft()

    for idx in range(1, n+1):
      if visit[idx] == 0 and mylist[cur][idx] == 1:
        myq.append(idx)
        visit[idx] = 1
        result += 1

  return result

print(BFS(1)-1)
