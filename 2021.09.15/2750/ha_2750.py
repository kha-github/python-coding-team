n = int(input())
mylist = []

for _ in range(n):
  mylist.append(int(input()))

def selection():
  for i in range(n-1, 0, -1):
    pick = mylist[i]
    idx = i
    for k in range(0, i):
      if pick < mylist[k]:
        pick = mylist[k]
        idx = k
    temp = mylist[idx]
    mylist[idx] = mylist[i]
    mylist[i] = temp

selection()
for item in mylist:
  print(item)
