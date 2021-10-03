import sys
input = sys.stdin.readline

n = int(input())
mylist = []

for _ in range(n):
  mylist.append(list(map(int, input().split())))

for i in range(n):
  for k in range(n):
    for j in range(n):
      if mylist[k][i]+mylist[i][j] == 2:
        mylist[k][j] = 1

for idx in range(n):
  print(' '.join(list(map(str,mylist[idx]))))
