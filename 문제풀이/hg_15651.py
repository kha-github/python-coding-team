import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().split())
ans_lis = [0 for _ in range(M)]
arr = list(range(1, N+1))

def permutation_repetite(L):
    if L == M:
        for i in range(M):
            print(ans_lis[i], end = ' ')
        print()

    else:
        for i in range(N):
            ans_lis[L] = arr[i]
            permutation_repetite(L+1)


permutation_repetite(0)