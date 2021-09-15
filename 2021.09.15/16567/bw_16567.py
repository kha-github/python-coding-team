import sys

a,b= map(int, sys.stdin.readline().split())


arr1= list(map(int,sys.stdin.readline().split()))
           
arr2 = []


for _ in range(b):
    arr2.append(list(map(int,sys.stdin.readline().split())))

for i in arr2:
    #print(arr1)
    if i[0]==1:
        arr1[i[1]-1]=1
    else:
        check=0
        cnt=0
        for j in arr1:
            
            if j==1 and check==0:
                cnt+=1
                check=1
            elif j==1 and check==1:
                pass
            elif j==0 and check==0:
                pass
            elif j==0 and check==1:
                check=0
        print(cnt)
                
                
        
        
        
#print(a,b)
#print(arr1)
#print(arr2)
