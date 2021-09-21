t = int(input())
from collections import deque

ans = []
for _ in range(t):
    p = input()
    n = int(input())
    arr = input()
    arr = arr[1:-1]
    if n == 0:
        arr= deque()
    else:
        arr = deque(map(int,arr.split(",")))
    for i in p:
        if i == "R":
            arr.reverse()
        else:
            if not arr:
                ans.append("error")
                break
            arr.popleft()
            
    if arr:
        a=[]
        while arr:
            a.append(arr[0])
            arr.popleft()
        ans.append(a)

for i in ans:
    print(i)
