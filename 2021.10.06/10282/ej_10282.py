import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드를 제외
        if distance[now] >= dist:
            for x in graph[now]:
                cost = dist + x[1]
                if cost < distance[x[0]]:
                    distance[x[0]] = cost
                    heapq.heappush(q, (cost, x[0]))


M = int(1e9)

for _ in range(int(input())):
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [M] * (n + 1)

    for _ in range(m):
        a, b, second = map(int, input().split())
        graph[b].append((a, second))

    dijkstra(start)

    count, time = 0, 0
    for i in range(1, n + 1):
        if distance[i] != M:
            count += 1
            time = max(time, distance[i])
    print(count, time)
