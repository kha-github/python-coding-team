import sys
import heapq
input = sys.stdin.readline

myheap = []

n = int(input())

for _ in range(n):
  temp = int(input())
  if temp == 0:
    if myheap:
      result = heapq.heappop(myheap)[1]
      print(result)
    else:
      print("0")
  else:
    heapq.heappush(myheap, (abs(temp), temp))
