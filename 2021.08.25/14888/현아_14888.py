n = int(input())
mylist = list(map(int, input().split(" ")))
oplist = list(map(int, input().split(" ")))
resultlist = []

def DFS(add, sub, mul, div, idx, val):

  if idx == n:
    resultlist.append(val)
    return
  if add >= 1:
    DFS(add-1, sub, mul, div, idx+1, val+mylist[idx])
  if sub >= 1:
    DFS(add, sub-1, mul, div, idx+1, val-mylist[idx])
  if mul >= 1:
    DFS(add, sub, mul-1, div, idx+1, val*mylist[idx])
  if div >= 1:
    DFS(add, sub, mul, div-1, idx+1, int(val/mylist[idx]))


DFS(oplist[0], oplist[1], oplist[2], oplist[3], 1, mylist[0])
print(max(resultlist))
print(min(resultlist))
