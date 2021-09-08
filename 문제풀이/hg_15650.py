import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(range(1, N+1))
ans_list = [0 for _ in range(M)]

def get_combination(L, start): #L Level
    if L == M:
        for i in range(M):
            print(ans_list[i], end = ' ')
        print()
    else:
        for i in range(start, N):
            ans_list[L] = arr[i]
            get_combination(L + 1, i + 1)
            ans_list[L] = 0

get_combination(0, 0)
