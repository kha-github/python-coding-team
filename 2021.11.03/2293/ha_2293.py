n, k = map(int, input().split())

coinList = []
dptable = [0]*(k+1)
dptable[0] = 1

for _ in range(n):
  coinList.append(int(input()))

for coin in coinList:
  for i in range(1, k+1):
    if i < coin:
      continue
    dptable[i] += dptable[i-coin]

print(dptable[-1])
