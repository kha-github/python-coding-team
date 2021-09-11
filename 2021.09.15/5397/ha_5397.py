t = int(input())

for _ in range(t):
  mylist = list(input())
  leftlist = []
  rightlist = []
  for idx in range(len(mylist)):
    if mylist[idx] == '<':
      if len(leftlist) > 0:
        rightlist.append(leftlist[-1])
        del leftlist[-1]
    elif mylist[idx] == '>':
      if len(rightlist) > 0:
        leftlist.append(rightlist[-1])
        del rightlist[-1]
    elif mylist[idx] == '-':
      if len(leftlist) > 0:
        del leftlist[-1]
    else:
      leftlist.append(mylist[idx])
    
  rightlist.reverse()
      
  print(''.join(leftlist + rightlist))
