n,k = map(int,input().split())
M = 1000000000

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][1] = 1

for i in range(1,k+1):
    dp[1][i] = i

for i in range(2,n+1):
    for j in range(2,k+1):
        for l in range(j):
            dp[i][j] += dp[i-1][j-l]
            
print(dp[n][k] % M)
