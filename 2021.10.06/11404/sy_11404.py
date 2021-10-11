# 틀렷어
n = int(input())
INF = int(1e6)
g = [[INF] * n for _ in range(n)]
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a - 1][b - 1] = min(g[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                g[i][j] = min(g[i][k] + g[k][j], g[i][j])

for i in range(n):
    for j in range(n):
        if g[i][j] == INF:
            print(0, end=' ')
        else:
            print(g[i][j], end=' ')
    print()
