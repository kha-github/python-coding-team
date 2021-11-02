n, k = map(int, input().split())
dptable = [0]*(n+1)
dptable[0] = 1

for _ in range(1, k+1): 
  for i in range(1, n+1): 
    dptable[i] = (dptable[i] + dptable[i-1])%1000000000

print(dptable[n])
