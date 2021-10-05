import heapq
import sys
input = sys.stdin.readline

INF = 100000000

t = int(input())

for _ in range(t):
  n, d, c = map(int, input().split())
  mylist = [[] for _ in range(n)]
  for i in range(d):
    a, b, s = map(int, input().split())
    mylist[b-1].append([a-1, s])
  
  myheap = []
  heapq.heappush(myheap, [0, c-1])

  costlist = [INF]*n
  costlist[c-1] = 0

  while myheap:
    cur = heapq.heappop(myheap)
    for item in mylist[cur[1]]:
      if costlist[item[0]] > cur[0]+item[1]:
        costlist[item[0]] = cur[0]+item[1]
        heapq.heappush(myheap, [costlist[item[0]], item[0]])

  cnt = 0

  for i in range(n):
    if costlist[i] == INF:
      costlist[i] = -1
    else:
      cnt += 1
  
  print(cnt, max(costlist))
