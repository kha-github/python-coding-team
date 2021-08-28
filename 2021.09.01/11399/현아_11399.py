n = int(input())
mylist = list(map(int, input().split()))

mylist.sort()

cnt = 0
reuslt = 0

for item in mylist:
  cnt += item
  reuslt += cnt

print(reuslt)
