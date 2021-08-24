from itertools import combinations

n = int(input())
mylist = [[0]*n for _ in range(n)]
empty_loc = []

for i in range(n):
  mylist[i] = list(map(str, input().split()))
  for j in range(n):
    if mylist[i][j] == "X":
      empty_loc.append([i, j])

object_list = list(combinations(empty_loc, 3))


def fun(i, j):

  for x in range(i, -1, -1):
    if mylist[x][j] == "O": break
    elif mylist[x][j] == "S": return 0
  
  for x in range(i, n):
    if mylist[x][j] == "O": break
    elif mylist[x][j] == "S": return 0

  for y in range(j, -1, -1):
    if mylist[i][y] == "O": break
    elif mylist[i][y] == "S": return 0

  for y in range(j, n):
    if mylist[i][y] == "O": break
    elif mylist[i][y] == "S": return 0
  
  return 1

def check():
  for i in range(n):
    for j in range(n):
      if mylist[i][j] == "T":
        if fun(i, j) == 0:
          return False
    
  return True

for item in object_list:
  for idx in range(3):
    mylist[item[idx][0]][item[idx][1]] = "O"

  if check():
    print("YES")
    exit(0)

  for idx in range(3):
    mylist[item[idx][0]][item[idx][1]] = "X"

print("NO")
