import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = []
for i in range(N):
    res.append(sum(arr[:i+1]))

print(sum(res))