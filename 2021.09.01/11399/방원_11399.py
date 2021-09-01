n = int(input())

arr1 = list(map(int,input().split()))
arr1.sort()

for i in range(1,n):
    arr1[i]+=arr1[i-1]

print(sum(arr1))
