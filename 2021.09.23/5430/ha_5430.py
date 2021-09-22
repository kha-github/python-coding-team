t = int(input())

def opFun(op, n):
  mylist = [0, n, 0] #순서대로 앞 자르는 개수, 뒤 자르는 개수, reverse 여부
  reverse = False
  for idx in range(len(op)):
    if op[idx] == 'R':
      reverse = not(reverse)
    if op[idx] == 'D':
      if reverse:
        mylist[1] -= 1
      else:
        mylist[0] += 1
  if reverse:
    mylist[2] = -1
  else:
    mylist[2] = 1
  return mylist

for _ in range(t):
  op = input()
  n = int(input())
  mylist = input().replace('[','').replace(']','').split(',')
  result = opFun(op, n)
  if result[0] > result[1]:
    print("error")
  else:
    mylist = mylist[result[0]:result[1]]
    if result[2] == -1:
      mylist.reverse()
    print("[" + ",".join(mylist) + "]")
