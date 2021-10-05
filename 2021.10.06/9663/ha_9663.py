n = int(input())
loc = [0]*n
cnt = 0

def check(cur, i):
  for idx in range(cur):
    #겹치는 것이 있는지 확인
    if loc[idx] == i or abs(loc[idx]-i) == abs(idx-cur):
      return False
  return True

def DFS(cur):

  global cnt

  if cur == n:
    cnt += 1
    return
  for idx in range(n):
    #해당 위치에 퀸을 놓음
    loc[cur] = idx
    if check(cur, idx):
      DFS(cur+1)

DFS(0)
print(cnt)
