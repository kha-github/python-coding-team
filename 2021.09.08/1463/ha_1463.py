n = int(input())
dptable = [0]*(n+1)

for i in range(2, n+1):
  
  dptable[i] = dptable[i-1] + 1

  if i % 2 == 0:
    dptable[i] = min(dptable[i], dptable[i//2] + 1)

  if i % 3 == 0:
    dptable[i] = min(dptable[i], dptable[i//3] + 1)

print(dptable[n])
