import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = list(range(1, N + 1))
visit = [0 for _ in range(N)]
ans_list = [0 for _ in range(M)]
def get_permutation(L):
    if L == M:
        for i in range(M):
            print(ans_list[i], end = " ")
        print()

    else:
        for i in range(N):
            if visit[i] == 0: #방문한 적이 없으면
                visit[i] = 1 #방문처리 하고
                ans_list[L] = arr[i]
                get_permutation(L+1)
                visit[i] = 0

get_permutation(0)