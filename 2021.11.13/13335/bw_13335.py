import sys

n,w,l = map(int,sys.stdin.readline().split()) # n: 개수 w: 다리길이 l:최대하중
trucks = list(map(int,sys.stdin.readline().split()))


bridge = [0]*w
weight, time = 0, 0

while bridge:
    
    bridge.pop(0)
    
    if trucks:
        if (sum(bridge) + trucks[0]) <= l:
            bridge.append(trucks.pop(0))
                          
        else:
            bridge.append(0)
        
    time += 1
        
    
print(time)
