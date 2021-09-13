from itertools import combinations

n, m = map(int, input().split())
mylist = []
housecnt = 0
chickencnt = 0

for _ in range(n):
  mylist.append(list(map(int, input().split())))
  housecnt += mylist[-1].count(1)
  chickencnt += mylist[-1].count(2)

vallist = [[0]*chickencnt for _ in range(housecnt)]

def fun(cnt, x, y):
  val = 0
  for i in range(n):
    for j in range(n):
      if mylist[i][j] == 1:
        vallist[val][cnt] = abs(i-x) + abs(y-j)
        val += 1

cnt = 0
for i in range(n):
  for j in range(n):
    if mylist[i][j] == 2:
      fun(cnt, i, j)
      cnt += 1

combilist = list(combinations(list(range(0, chickencnt)), m))
resultlist = [0]*len(combilist)
cnt = 0
for idx in range(len(combilist)):
  for i in range(housecnt):
    templist = []
    for j in range(m):
      templist.append(vallist[i][combilist[idx][j]])
    resultlist[idx] += min(templist)

print(min(resultlist))
