import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.insert(N, (0, 0))

dp = [0 for _ in range(N+1)]
dp[0]

for now in range(N+1):
    for before in range(now):
        if now - before >= arr[before][0]:
            dp[now] = max(dp[now], dp[before] + arr[before][1])

print(dp[now])