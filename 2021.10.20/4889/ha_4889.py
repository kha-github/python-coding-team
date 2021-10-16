inputcnt = 1

while(True):
  mylist = list(input())
  if mylist[0] == '-':
    break
  mystack = []
  for idx in range(len(mylist)):
    if len(mystack) > 0 and mystack[-1] == "{" and mylist[idx] == "}":
      mystack.pop()
    else:
      mystack.append(mylist[idx])

  cnt = 0
  for idx in range(0, len(mystack), 2):
    if mystack[idx] == '}':
      cnt += 1
    if mystack[idx+1] == '{':
      cnt += 1
  print(str(inputcnt)+". "+str(cnt))
  
  inputcnt += 1
