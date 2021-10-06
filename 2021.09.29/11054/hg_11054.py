import sys
sys.stdin = open("input.txt", 'rt')

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]
dp_reverse = [1 for _ in range(N)]

# linear_dpcase
for now in range(N):
    for before in range(now):
        if arr[now] > arr[before]:
            dp[now] = max(dp[before] + 1, dp[now])

# reverse_dpcase
for now in range(N-1, -1, -1):
    for before in range(N-1, now - 1, -1):
        if arr[now] > arr[before]:
            dp_reverse[now] = max(dp_reverse[now], dp_reverse[before] + 1)
# dp_sum
dp_sum = list([x + y - 1 for x, y in zip(dp, dp_reverse)])
print(max(dp_sum))







