import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().split())
#N~N, 1 <= N <= 1024, 1 <= M <= 100,000

def get_subtot(graph):
    subtot = [[0] * (N+1) for _ in range(N+1)]
    for r in range(N+1):
        for c in range(N+1):
            if r == 0 or c == 0:
                continue
            if r == 1 and c == 1:
                subtot[r][c] = graph[r-1][c-1]
            elif r == 1:
                subtot[r][c] = subtot[r][c-1] + graph[r-1][c-1]
            elif c == 1:
                subtot[r][c] = subtot[r-1][c] + graph[r-1][c-1]
            else:
                subtot[r][c] = subtot[r-1][c] + subtot[r][c-1] + graph[r-1][c-1] - subtot[r-1][c-1]
    return subtot

def solution():
    graph = [list(map(int, input().split())) for _ in range(N)]
    subtot = get_subtot(graph) #구간합 계산
    for _ in range(M):
        x1, y1, x2, y2 = map(lambda x: int(x), input().split())
        answer = subtot[x2][y2] - subtot[x1-1][y2] - subtot[x2][y1-1] + subtot[x1-1][y1-1]
        print(answer)

solution()