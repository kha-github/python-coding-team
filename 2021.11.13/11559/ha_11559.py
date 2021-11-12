from collections import deque

mylist = []

for _ in range(12):
  mylist.append(list(input()))

mylist = list(map(list, zip(*mylist)))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y, target):
  myque = deque([])
  op = 0
  pang = 1

  myque.append([x, y])
  mylist[x][y] = '!'

  while len(myque) != op:
    cur = myque[op]
    op += 1
    for idx in range(4):
      cur_x = cur[0] + dx[idx]
      cur_y = cur[1] + dy[idx]
      if cur_x < 6 and cur_x >= 0 and cur_y < 12 and cur_y >= 0 and mylist[cur_x][cur_y] == target and mylist[cur_x][cur_y] != '!':
        myque.append([cur_x, cur_y])
        mylist[cur_x][cur_y] = '!'
        pang += 1
  

  if pang < 4:
    for idx in range(len(myque)):
      mylist[myque[idx][0]][myque[idx][1]] = target

tictok = 0

while (True):
  isFinish = True
  for i in range(6):
    for k in range(12):
      if mylist[i][k] != '.' and mylist[i][k] != '!':
        BFS(i, k, mylist[i][k])
  for i in range(6):
    for k in range(12):
      if mylist[i][k] == '!':
        isFinish = False 
        mylist[i].pop(k)
        mylist[i].insert(0, '.')
  if isFinish:
    print(tictok)
    break
  tictok += 1

