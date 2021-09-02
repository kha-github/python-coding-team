import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = [tuple(map(int ,input().split())) for _ in range(N)]
dp = [0 for _ in range(M+1)]

# 힙색 _ only 1
for kind in range(N):
    w = arr[kind][0]
    for weight in range(M, w-1, -1): #냅색 + 한번만 사용하므로 역으로.
        dp[weight] = max(dp[weight], dp[weight - w] + arr[kind][1])

print(dp[M])