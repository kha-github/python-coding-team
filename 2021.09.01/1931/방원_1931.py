import sys
 
n = int(input())

data=[]
cnt=0
semina=[0,0]


for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
    
data.sort(key=lambda x: (x[1],x[0]))

for k in data:
    
    if k[0]>=semina[1]:
        cnt+=1
        semina=k
    
    
    
    
    
 
#print(data)
print(cnt)
     

