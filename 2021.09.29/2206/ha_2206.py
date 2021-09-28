from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visitlist = [[[0] * 2 for _ in range(m)] for _ in range(n)]
mylist = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
  mylist.append(list(map(int, input().rstrip())))

def BFS():
  myq = deque([[0, 0, 0], ])

  while myq:
    cur = myq.popleft()
    cur_x = cur[0]
    cur_y = cur[1]
    is_break = cur[2]
    if cur_x == n-1 and cur_y == m-1:
      return visitlist[cur_x][cur_y][is_break]+1
    for idx in range(4):
      next_x = cur_x + dx[idx]
      next_y = cur_y + dy[idx]

      if 0 <= next_x and next_x < n and 0 <= next_y and next_y < m:
        if is_break == 0 and mylist[next_x][next_y] == 1 and visitlist[next_x][next_y][1] == 0: #아직까지 부신 벽이 없으면 한번 부셔봄
          visitlist[next_x][next_y][1] = visitlist[cur_x][cur_y][0] + 1
          myq.append([next_x, next_y, 1])
        elif visitlist[next_x][next_y][is_break] == 0 and mylist[next_x][next_y] == 0:
          visitlist[next_x][next_y][is_break] = visitlist[cur_x][cur_y][is_break] + 1
          myq.append([next_x, next_y, is_break])
  return -1

print(BFS())
