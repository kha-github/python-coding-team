import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
N, D, C = map(int, input().split())

pcs = [[100001] * (N+1) for _ in range(N+1)]

for _ in range(D):
    S, E, T = map(int, input().split())
    pcs[S][E] = T


for r in pcs[1:]:
    for c in r[1:]:
        print(c, end = " ")
    print()

for now in range(1, N+1)
    for mid in range(1, N+1):


