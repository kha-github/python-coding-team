import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N+1))
ans_list = [0 for _ in range(M)]

def combination_par(L, start):
    if L == M :
        for i in range(M):
            print(ans_list[i], end = " ")
        print()


    else:
        for i in range(start,N):
            ans_list[L] = arr[i]
            combination_par(L + 1, i)



combination_par(0, 0)


