import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
sumlist = [[0]*(n+1) for _ in range(n+1)]

# 입력 시간초과
# for idx in range(n):
#   templist = list(map(int, sys.stdin.readline().split()))
#   mylist.append(templist)

for idx in range(1, n+1):
  for i in range(1, n+1):
    sumlist[idx][i] = sumlist[idx-1][i] + sumlist[idx][i-1] + mylist[idx-1][i-1] - sumlist[idx-1][i-1]

for i in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(sumlist[x2][y2] - sumlist[x1-1][y2] - sumlist[x2][y1-1] + sumlist[x1-1][y1-1])
