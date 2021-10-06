import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

# 먹는 행위 따
# 지나가는 행위 따로

nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]

graph = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

print(graph)

def babyShark(now_x, now_y, shark_volumn = 2, fishes_eaten):
    if now_x < 0 or now_x >= N or now_y <= 0 or now_x >= N:
        return
    if fishes_eaten == shark_volumn:
        babyShark(now_x, now_y, shark_volumn + 1, fishes_eaten):









