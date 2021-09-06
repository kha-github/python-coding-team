n, k = map(int, input().split())

w = []
v = []
dptable = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
  a, b = map(int, input().split())
  w.append(a)
  v.append(b)

for i in range(1, n+1):
  for j in range(1, k+1):
    if j >= w[i-1]: 
      dptable[i][j] = max(dptable[i-1][j], dptable[i-1][j-w[i-1]]+v[i-1])
    else:
      #감당 가능한 무게보다 현재 아이템의 무게가 더 크면 이전 케이스 그대로
      dptable[i][j] = dptable[i-1][j]
    
print(dptable[n][k])
