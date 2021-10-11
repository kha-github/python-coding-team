n = int(input())
M = int(1e10)
cost = [[M] * n for _ in range(n)]

# 인접행렬 초기화
for x in range(int(input())):
    i, j, price = map(int, input().split())
    cost[i - 1][j - 1] = min(price, cost[i - 1][j - 1])

# 플로이드-워셜 구현
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 출력
for i in range(n):
    for j in range(n):
        if cost[i][j] == M:
            print(0, end=" ")
        else:
            print(cost[i][j], end=" ")
    print()

