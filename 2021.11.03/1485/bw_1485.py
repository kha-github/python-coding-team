import sys

n, s, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

dp = [ [0]*(m+1) for _ in range(n+1) ]        # (m+1) * (n+1)배열 생성
dp[0][s] = 1


def vol():                       # 이차원 배열에 가능한 값들 저장

    for i in range (1,n+1):
        for j in range(m+1):

            if dp[i-1][j] == 0:
                continue

            if j + v[i-1] <= m:
                dp[i][j+v[i-1]] = 1

            if j - v[i-1] >= 0:
                dp[i][j-v[i-1]] = 1

def answer():

    for i in range(m,-1,-1):
        if dp[-1][i] == 1:          # dp 마지막 행에 가장큰 원소 출력 없으면 -1출력
            print(i)
            break
    else:
        print(-1)

vol()
answer()

# 재귀로 풀이 시간초과
# 2차원 배열 사용하여 dp[i][j] 갱신
# 마지막 행 1이 존재하면 index return 하여주고 없으면 -1 출력

# import sys
#
# n, s, m = map(int, sys.stdin.readline().split())
# v = list(map(int, sys.stdin.readline().split()))
#
# arr1 = []
# arr1.append(s)
#
# def check(arr, v):
#
#     k = arr.pop()
#
#     a = k - v[0]
#     b = k + v[0]
#
#     if v and ( a > 0 and  a < m):
#         arr.append(a)
#         v.pop()
#         print(v)
#         print(arr)
#         check(arr, v)
#
#     if v and (b > 0 and b < m):
#         arr.append(b)
#         print(v)
#         print(arr)
#         v.pop()
#         check(arr, v)
#
#     return arr
#
#
# print(check(arr1, v))
#
#
#
#
# #print(n,s,m)
# #print(v)
