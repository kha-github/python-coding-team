import sys
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for s in range(N):
    for e in range(N):
        if graph[s][e] == 0:
            graph[s][e] = 100001


for waypoint in range(N):
    for start_node in range(N):
        for end_node in range(N):
            # if start_node == end_node: 자기자신 포함X 아니다
            #     graph[start_node][end_node] = 0
            graph[start_node][end_node] = min(graph[start_node][end_node], graph[start_node][waypoint] + graph[waypoint][end_node])

for i in range(N):
    for j in range(N):
        if graph[i][j] in (100001, ):
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()