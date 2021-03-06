import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0, 0))
visit[0][0] = 1


while q:
    now_y, now_x, hit = q.popleft()
    if now_y == N-1 and now_x == M-1:
        print(distance[N-1][M-1] + 1)

    for ny, nx in zip(dy, dx):
        next_y = now_y + ny
        next_x = now_x + nx

        if 0 <= next_y < N and 0 <= next_x < M:
            if graph[next_y][next_x] == 1 and visit[next_y][next_x] == 0 and not hit:
                hit = 1
                visit[next_y][next_x] = 1
                distance[next_y][next_x] = distance[now_y][now_x] + 1
                q.append((next_y, next_x, hit))

            elif graph[next_y][next_x] == 0 and visit[next_y][next_x] == 0:
                visit[next_y][next_x] = 1
                distance[next_y][next_x] = distance[now_y][now_x] + 1
                q.append((next_y, next_x, hit))
            print(q)

for r in distance:
    print(r)





