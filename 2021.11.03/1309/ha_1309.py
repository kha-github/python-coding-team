n = int(input())
dptable = [[0]*3 for _ in range(n)]

dptable[0] = [1, 1, 1]

for i in range(1, n):
  dptable[i][0] = (dptable[i-1][1] + dptable[i-1][2] + dptable[i-1][0])%9901
  dptable[i][1] = (dptable[i-1][0] + dptable[i-1][2])%9901
  dptable[i][2] = (dptable[i-1][0] + dptable[i-1][1])%9901

print((dptable[-1][0] + dptable[-1][1] + dptable[-1][2])%9901)
