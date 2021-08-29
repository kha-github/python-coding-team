k = int(input())

mylist= []

for i in range(k):
  mylist.append(list(map(int, input().split())))

mylist = sorted(mylist, key = lambda x: x[0])
mylist = sorted(mylist, key = lambda x: x[1])

result = 0 
end = 0

for idx in range(len(mylist)):
  if mylist[idx][0] >= end:
    result += 1
    end = mylist[idx][1]

print(result)
