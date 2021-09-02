import sys
#sys.stdin = open("input.txt", "rt")

def checker(r, c, w, h):
    # 기저조건 : 범위 밖으로 나가면, 바다면
    if r < 0 or r >= h or c < 0 or c >= w:
        return

    if graph[r][c] == 0:
        return

    # 섬이 있으면 주변섬 전부 가라앉히기
    else:
        graph[r][c] = 0
        for nr, nc in zip(dr, dc):
            nr = r + nr
            nc = c + nc
            checker(nr, nc, w, h)

dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]
while True:
    answer = 0
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if graph[r][c] == 1:
                checker(r, c, w, h)
                answer += 1
    print(answer)