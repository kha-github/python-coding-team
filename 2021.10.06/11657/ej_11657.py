def bellman_ford(start):
    dist[start] = 0
    negative_flag = False

    # 모든 노드에서 매번 모든 간선을 확인
    for i in range(n):
        for j in range(m):
            x, y, cost = graph[j][0], graph[j][1], graph[j][2]
            if dist[x] != M:
                if dist[y] > dist[x] + cost:
                    dist[y] = dist[x] + cost
                    if i == n - 1:
                        negative_flag = True
                        break
    return negative_flag


M = int(1e9)
n, m = map(int, input().split())
graph = []
dist = [M] * (n + 1)

for _ in range(m):
    graph.append((list(map(int, input().split()))))

is_negative = bellman_ford(1)

if is_negative:
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i]) if dist[i] != M else print(-1)
