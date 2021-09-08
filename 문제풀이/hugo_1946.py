import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    arr.sort(key = lambda x : x[0])
    #print(arr) #일단 서류순으로 거르고 그리고 LIS 구하면 될 듯? 아뉜데~ ㅋㅋ

    #dp[i] = i번쨰 기준으로 뽑을 수 있는 최대 신입사원의 수
    #dp = [1 for _ in range(N)]

    answer = 1
    minn = arr[0][1]
    for now in range(N):
        if arr[now][1] < minn:
            answer += 1
            minn = arr[now][1]

    print(answer)