n, k = map(int, input().split())

mylist = [[0]*n for _ in range(n)]
myq = []
stepx = [0, 0, 1, -1]
stepy = [1, -1, 0, 0]

for i in range(n):
  temp = list(map(int, input().split()))
  for j in range(n):
    if temp[j] != 0:
      mylist[i][j] = temp[j]
      myq.append([temp[j], i, j])

myq.sort()

s, x, y = map(int, input().split())

def BFS():
  prev = -1
  day = 1
  while myq:
    cur = myq.pop(0)
    if prev == 3 and cur[0] == 1:
      day += 1
    if day > s:
      break
    prev = cur[0]
    for i in range(4):
      next_x = cur[1]+stepx[i]
      next_y = cur[2]+stepy[i]
      if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
        if mylist[next_x][next_y] == 0:
          mylist[next_x][next_y] = cur[0]
          myq.append([cur[0], next_x, next_y])

BFS()
print(mylist[x-1][y-1])
