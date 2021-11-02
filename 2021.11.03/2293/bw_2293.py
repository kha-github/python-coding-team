import sys

n,k = map(int,sys.stdin.readline().split())

arr1=[]

for _ in range(n):

    arr1.append(int(sys.stdin.readline().strip()))

dp = [0] * (k+1)
dp[0]=1

for i in arr1:
    for j in range(i,k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[k])
# 이차원 배열로 생각했으나 시간초과
# 1로 10까지 만들 수있는 경우 -> 1,2로 10까지 만들수 있는경우 -> 1,2,5로 10까지 만들수 있는경우
# dp[] 갱신
