t = int(input())

for _ in range(t):
  n = int(input())
  mylist = []

  for i in range(n):
    mylist.append(input())

  #접두사라면 앞 문자열이 무조건 뒤 문자열을 포함함
  mylist.sort()

  resCheck = False

  for i in range(1, n):
    prev = mylist[i-1]
    cur = mylist[i]
    if prev == cur[0:len(prev)]:
      resCheck = True
      break
  if resCheck == True:
    print("NO")
  else:
    print("YES")
