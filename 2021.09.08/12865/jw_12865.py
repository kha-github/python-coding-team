N, K = map(int,input().split())
dp = [[0] *(K+1) for _ in range(N+1)]
item = []
for i in range(N):
    W,V = map(int,input().split())
    item.append((W,V))
for i in range(1,N+1):
    for j in range(1,K+1):
        if item[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-item[i-1][0]]+item[i-1][1])
print(dp[N][K])
