import sys
import heapq

n = int(input())

data =[]
cnt=0
money=0

for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
    
data.sort(key=lambda x: (x[1]))

heap=[]

for i in range(n):
    money +=data[i][0]
    heapq.heappush(heap, data[i][0])
    
    if len(heap) > data[i][1]:
        money -= heapq.heappop(heap)
    
    
    
#print(data)
    
print(money)