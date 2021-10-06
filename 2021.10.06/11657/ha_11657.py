import sys
input = sys.stdin.readline

INF = 1000000000

n, m = map(int, input().split())
mylist = []
costlist = [INF]*(n+1)

for _ in range(m):
  mylist.append(list(map(int, input().split())))

costlist[1] = 0

#최악의 경우 모든 간선을 다 보아야함
#음수 사이클이 없다면 최대 간선-1개만큼 반복
for i in range(0, n):
  for k in range(m):
    #기존것보다 거쳐가는게 더 이득이면
    if costlist[mylist[k][0]] != INF and costlist[mylist[k][1]] > costlist[mylist[k][0]] + mylist[k][2]:
      costlist[mylist[k][1]] = costlist[mylist[k][0]] + mylist[k][2]
      #간선 이상 반복해서 업데이트되면 음수사이클 존재
      if i == n-1:
        print("-1")
        exit(0)

for idx in range(2, n+1):
  if costlist[idx] == INF:
    print("-1")
  else:
    print(costlist[idx])
