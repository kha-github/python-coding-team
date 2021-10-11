n,k = map(int,input().split())
n_len = len(str(n))
n_str = str(n)
num_max = 0

def dfs(num,idx):
    global num_max
    if idx == 3:
        num_max = max(num_max,int(num))
    for i in range(len(num)-1):
        for j in range(i,len(num)):
            num = num[:i] + num[j] + num[i+1:j] + num[i] + num[j+1:]
            dfs(num,idx+1)  

if n_len == 1 or str(n)[1:] == "0"* (n_len-1):
    print(-1)
else:
    dfs(n_str,0)  
print(num_max)
