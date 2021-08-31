n = int(input())
a=[]
for i in range(n):
    p,d = map(int,input().split())
    a.append((p,d))
a = sorted(a,key=lambda x: (x[1],-x[0]))
f = a[0][1]
s = a[0][0]
for i in range(1,n):
    if a[i][1] > f:
        s += a[i][0]
        f = a[i][1]
print(s)
