import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
cnt = 0
graph = [[0] * N for _ in range(N)]
check_c = [0 for _ in range(N)]

def count_queen(graph, r):
    global cnt
    if r == N:
        cnt += 1

    for c in range(N):
        if check_c[c] == 0:
            print(check_c)
    check_c[c] = c
            count_queen(graph, r+1)
            check_c[c] = 0

count_queen(graph, 0)
print(cnt)










