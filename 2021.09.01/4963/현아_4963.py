def DFS(a, b):
  global mylist, w, h

  dx = [0, 0, 1, -1, 1, 1, -1, -1]
  dy = [1, -1, 0, 0, 1, -1, 1, -1]

  mystack = []
  mystack.append([a, b])
  mylist[a][b] = 0

  while mystack:
    
    cur = mystack.pop()
    cur_x = cur[0]
    cur_y = cur[1]

    for idx in range(8):
      
      next_x = dx[idx] + cur_x
      next_y = dy[idx] + cur_y

      if next_x>=0 and next_x<h and next_y>=0 and next_y<w:
        if mylist[next_x][next_y] == 1:
          mylist[next_x][next_y] = 0
          mystack.append([next_x, next_y])

while True:
  w, h = map(int, input().split())
  if w==0 and h==0:
    break
  mylist = []
  cnt = 0

  for _ in range(h):
    mylist.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if mylist[i][j] == 1:
        DFS(i, j)
        cnt +=1

  print(cnt)
