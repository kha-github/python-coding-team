n,k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort()
dp = [0] *(k+1)
dp[0] = 1

for i in coin:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[k])
