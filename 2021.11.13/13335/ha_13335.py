n, w, l = map(int, input().split())
mylist = list(map(int, input().split()))

bridge = [0]*w
count = 0
arrivecnt = 0
weight = 0

while bridge:
  arrive = bridge.pop(0)
  weight -= arrive

  if len(mylist) != 0:
    if weight + mylist[0] <= l:
      weight += mylist[0]
      bridge.append(mylist.pop(0))
    else:
      bridge.append(0)
  count += 1

print(count)
