t = int(input())

dptable = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, ]

temp = 10

for _ in range(t):
  n = int(input())
  if len(dptable) < n+1:
    for idx in range(len(dptable), n+1):
      dptable.append(dptable[idx-5] + dptable[idx-1])
  
  print(dptable[n])
