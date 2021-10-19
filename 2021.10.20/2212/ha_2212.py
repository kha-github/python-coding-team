n = int(input())
k = int(input())
mylist = list(map(int, input().split()))
mylist.sort()

templist = []

for i in range(len(mylist)-1):
  templist.append(mylist[i+1]-mylist[i])

templist.sort(reverse=True)
result = 0

for i in range(k-1, len(templist)):
  result += templist[i]     

print(result)
