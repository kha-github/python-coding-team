import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [1 for _ in range(100)]

    for i in range(3, N):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N-1])



