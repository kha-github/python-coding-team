import sys
import heapq as hq
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
heapq = []
sign = []
for _ in range(N):
    num = int(input())
    if num > 0:
        hq.heappush(heapq, (num, 1))
    elif num < 0 :
        hq.heappush(heapq, (-num, -1))
    else:
        if heapq:
            ans = hq.heappop(heapq)
            print(ans[0] * ans[1])
        else:
            print(0)



