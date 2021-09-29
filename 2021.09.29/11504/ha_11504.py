n = int(input())
mylist = list(map(int, input().split()))

asc_dptable = [1] * n
desc_dptable = [1] * n
result = 1

for i in range(n):
  for j in range(i):
   if mylist[j] < mylist[i]:
     asc_dptable[i] = max(asc_dptable[i], asc_dptable[j]+1)

for i in range(n):
  for j in range(i):
   if mylist[n-j-1] < mylist[n-i-1]:
     desc_dptable[n-i-1] = max(desc_dptable[n-i-1], desc_dptable[n-j-1]+1)

for idx in range(n):
  if result < asc_dptable[idx]+desc_dptable[idx]:
    result = asc_dptable[idx]+desc_dptable[idx]

print(result-1)
