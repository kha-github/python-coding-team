import sys

n = int(input())

for _ in range(n):
    key=sys.stdin.readline().strip()
    
    arr1 = []
    arr2 = []
    
    for i in key:
        if i == '<':
            if arr1:
                arr2.append(arr1.pop())
        elif i == '>':
            if arr2:
                arr1.append(arr2.pop())
        elif i == '-' :
            if arr1:
                arr1.pop()
        else:
            arr1.append(i)
    
    arr1.extend(reversed(arr2))
    #print(arr1)
    print("".join(arr1))
    
        
