n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
p = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, k + 1):
        if wv[i - 1][0] > w:
            p[i][w] = p[i - 1][w]
        else:
            p[i][w] = max(wv[i - 1][1] + p[i - 1][w - wv[i - 1][0]], p[i - 1][w])
print(p[n][k])
