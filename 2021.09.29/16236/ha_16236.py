import heapq

n = int(input())
mylist = []
visitlist = [[0]*n for _ in range(n)]
cur_size = 2
eat_cnt = 0
tictok = 0

def resetVisitList():
  for i in range(n):
    for j in range(n):
      visitlist[i][j] = 0

def BFS(x, y):

  global tictok

  myq = [[0, x, y], ]
  visitlist[x][y] = 1
  step_x = [-1, 0, 0, 1]
  step_y = [0, -1, 1, 0]
  while True:
    if len(myq)==0:
      print(tictok)
      exit(0)
    cur = heapq.heappop(myq)
    cur_tictok = cur[0]
    cur_x = cur[1]
    cur_y = cur[2]
    if mylist[cur_x][cur_y] != 0 and mylist[cur_x][cur_y] < cur_size:
      return [cur_x, cur_y, cur_tictok]
    else:
      for i in range(4):
        next_x = cur_x + step_x[i]
        next_y = cur_y + step_y[i]
        if next_x >= 0 and next_y >= 0 and next_x < n and next_y < n and visitlist[next_x][next_y] == 0 and mylist[next_x][next_y] <= cur_size:
          heapq.heappush(myq, (cur_tictok+1, next_x, next_y))
          visitlist[next_x][next_y] = 1

for idx in range(n):
  mylist.append(list(map(int, input().split())))
  if 9 in mylist[-1]:
    cur_x = idx
    cur_y = mylist[-1].index(9)
    mylist[cur_x][cur_y] = 0

while True:
  temp = BFS(cur_x, cur_y)
  eat_cnt += 1
  if eat_cnt == cur_size:
    cur_size += 1
    eat_cnt = 0
  mylist[temp[0]][temp[1]] = 0
  cur_x = temp[0]
  cur_y = temp[1]
  tictok += temp[2]
  resetVisitList()
