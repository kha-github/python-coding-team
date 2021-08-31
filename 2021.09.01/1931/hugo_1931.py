import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]


arr.sort(key= lambda x:(x[1], x[0]))

st = 0
end = 0
cnt = 0

for x, y in arr:
    if end <= x:
        cnt += 1
        end = y
        st = x

print(cnt)