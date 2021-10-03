import sys
input = sys.stdin.readline
INF = 100000000000

n = int(input())
buscnt = int(input())
mylist = [[INF]*n for _ in range(n)]

for _ in range(buscnt):
  a, b, cost = map(int, input().split())
  if mylist[a-1][b-1] > cost:
    mylist[a-1][b-1] = cost

for i in range(n):
  for k in range(n):
    for j in range(n):
      if k == j:
        continue
      if mylist[k][i]+mylist[i][j] < mylist[k][j]:
        mylist[k][j] = mylist[k][i]+mylist[i][j]

for i in range(n):
  for j in range(n):
    if mylist[i][j] == INF:
      mylist[i][j] = 0

for idx in range(n):
  print(' '.join(list(map(str,mylist[idx]))))
