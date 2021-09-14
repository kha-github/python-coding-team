def leftMove(cur):
  if cur == 'd':
    return 'r'
  elif cur == 'l':
    return 'd'
  elif cur == 'r':
    return 'u'
  elif cur == 'u':
    return 'l'

def rightMove(cur):
  if cur == 'd':
    return 'l'
  elif cur == 'l':
    return 'u'
  elif cur == 'r':
    return 'd'
  elif cur == 'u':
    return 'r'

def straightMove(cur, x, y):
  if cur == 'd':
    return [x+1, y]
  elif cur == 'l':
    return [x, y-1]
  elif cur == 'r':
    return [x, y+1]
  elif cur == 'u':
    return [x-1, y]

n = int(input())
k = int(input())
applelist = []
movelist = []
snakelist = [[0, 0], ]
cnt = 1
curMove = 'r'
for _ in range(k):
  temp = list(map(int, input().split()))
  applelist.append([temp[0]-1, temp[1]-1])

movecnt = int(input())

for _ in range(movecnt):
  movelist.append(list(map(str, input().split())))

move = []
idx = 0

while True:
  while idx >= len(movelist) or cnt <= int(movelist[idx][0]):
    move = straightMove(curMove, snakelist[-1][0], snakelist[-1][1])
    if move[0]<0 or move[1]<0 or move[0]>=n or move[1]>=n or move in snakelist:
      print(cnt)
      exit(0)
    if move not in applelist:
      del snakelist[0]
    else:
      applelist.remove(move)
    snakelist.append(move)
    cnt += 1
  if movelist[idx][1] == 'D':
    curMove = rightMove(curMove)
  elif movelist[idx][1] == 'L':
    curMove = leftMove(curMove)

  idx += 1
