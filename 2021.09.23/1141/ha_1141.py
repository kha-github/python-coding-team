n = int(input())
mylist = []

for i in range(n):
  mylist.append(input())

mylist.sort(key=len)

#하나의 집합으로 일단 다 묶음
result = len(mylist)

for i in range(n):
  cur = mylist[i]
  for j in range(i+1, n):
    if cur == mylist[j][0:len(cur)]:
      #같은 집합에 넣을 수 없으면 내쫓음
      result -= 1
      break

print(result)
