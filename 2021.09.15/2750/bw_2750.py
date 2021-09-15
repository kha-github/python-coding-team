import sys
k = int(input())
arr1=[]

for _ in range(k):
    arr1.append(int(input()))    
    
arr1.sort()
for i in arr1:
    print(i,sep='\n')
