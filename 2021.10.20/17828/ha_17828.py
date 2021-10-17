n, target = map(int, input().split())

if n > target:
  print("!")
  exit(0)

cnt = 26
mylist = []
result = []

while target > 0:
  if target >= cnt:
    mylist.append(cnt)
    target -= cnt
  else:
    cnt -= 1

mylist.reverse()

if len(mylist) > n:
  print("!")
  exit(0)


for i in range(len(mylist)):
  cur = mylist[i]
  while n > len(mylist)-i-1:
    n -= 1
    if n == len(mylist)-i-1 or cur == 1:
      result.append(chr(cur+64))
      break
    result.append('A')
    cur -= 1

print(''.join(result))
