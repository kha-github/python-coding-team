from collections import deque
import sys
sys.setrecursionlimit(10**5)


def dfs(start, now, cnt):
    if now == start and visited[start] == 1:
        if cnt >= 3:
            visited[start] = 2
    else:
        if visited[now] == 0:
            visited[now] = 1
            if graph[now]:
                for next in graph[now]:
                    dfs(start, next, cnt + 1)


def bfs():
    q = deque()
    for i in range(1, n + 1):
        if cycle[i] == 2:
            q.append(i)
            distance[i] = 0
        else:
            distance[i] = -1
    while q:
        x = q.popleft()
        for y in graph[x]:
            if distance[y] == -1:
                q.append(y)
                distance[y] = distance[x] + 1


n = int(input())
graph = [[] for _ in range(n + 1)]
cycle = [0] * (n + 1)
distance = [0] * (n + 1)

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, i, 0)
    cycle[i] = visited[i]   # 0:방문X, 1:순환X, 2:순환O

bfs()

print(' '.join(map(str, distance[1:])))
