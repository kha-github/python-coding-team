n = int(input())
if n == 0:
  print(0)
  exit(0)

mylist = []

for _ in range(n):
  mylist.append(list(map(int, input().split())))

mylist = sorted(mylist, key = lambda x: x[0], reverse = True)

maxday = max(list(zip(*mylist))[1])
lec = [0]*(maxday+1)

for idx in range(n):
  for i in range(maxday, 0, -1):
    if mylist[idx][1] >= i and lec[i] == 0:
      lec[i] = mylist[idx][0]
      break

print(sum(lec))
