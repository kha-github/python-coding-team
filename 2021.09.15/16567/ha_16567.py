import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mylist = list(map(int, input().split()))
mylist.append(0)
dirtycnt = 0

if n == sum(mylist):
  dirtycnt = 1
elif n == 1:
  if mylist[0] == 1:
    dirtycnt = 1
else:
  for idx in range(1, n+1):
    if mylist[idx-1] == 1 and mylist[idx] == 0:
      dirtycnt += 1

for _ in range(m):
  oplist = list(map(int, input().split()))
  if oplist[0] == 0:
    print(dirtycnt)
  else:
    oplist[1] -= 1
    if mylist[oplist[1]] == 0:
      mylist[oplist[1]] = 1
      if n == 2 and mylist[oplist[1]-1] == 1:
        continue
      if oplist[1] > 0 and oplist[1] < n-1 and mylist[oplist[1]-1] == 1 and mylist[oplist[1]+1] == 1:
          dirtycnt -= 1
          continue
      if (oplist[1] > 0 and mylist[oplist[1]-1] == 1) or (oplist[1] < n-1 and mylist[oplist[1]+1] == 1):
        continue
      dirtycnt += 1
