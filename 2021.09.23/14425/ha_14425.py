import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
myset = {input() for _ in range(n)}

cnt = 0
for _ in range(m):
  temp = input()
  if temp in myset:
    cnt += 1

print(cnt)
