import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
distance = [[100001] * (N+1) for _ in range(N+1)]
M = int(input())

for _ in range(M):
    S, E, Cost = map(int, input().split())
    distance[S][E] = min(Cost, distance[S][E])

for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            # if s == e:
            #     distance[s][e] = 0
            # else:
            if s != e:
                distance[s][e] = min(distance[s][e], distance[s][k] + distance[k][e])


for r in range(1, N + 1):
    for c in range(1, N + 1):
        if distance[r][c] == 100001 :
            print(0, end=" ")
        else:
            print(distance[r][c], end=" ")
    print()


