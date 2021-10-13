from collections import deque
import sys
sys.stdin = open('../../input.txt', 'r')

n, k = input().split()
q = deque(list(n))
k = int(k)
result = ""

for i in range(k):
    print(q)
    max_val = max(q)
    max_idx = q.index(max_val) - 1
    q[max_idx] = q.popleft()
    result += max_val

if q:
    result += ''.join(list(q))

print(int(result))







