import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

# 10^6?
dp = [-1 for _ in range(10**6 + 1)]
dp[1] = 0

for num in range(1, N+1):
    if num % 6 == 0: # 3으로도 나누어 떨어지고, 2로도 나누어 떨어질떄 == num % 2 == 0 and num % 2 == 0
        dp[num] = min(dp[num // 3] + 1, dp[num//2] + 1, dp[num-1] + 1)
    elif num % 3 == 0:# only 3
        dp[num] = min(dp[num//3] + 1, dp[num-1] + 1)
    elif num % 2 == 0:# only 2
        dp[num] = min(dp[num//2] + 1, dp[num-1] + 1)
    else: #else
        dp[num] = dp[num-1] + 1

print(dp[N])

# 오기생기네
# dp[i] = i 기준 최소 시행 값



