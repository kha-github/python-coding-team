import copy

n,k = map(int,input().split())
n_len = len(str(n))
n_str = str(n)
num_max = -1

def dfs(num,idx):
    global num_max
    if idx == k:
        num_max = max(num_max,int(num))
        return
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            num_list = list(num)
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp
            if num_list[0] == "0":
                continue
            num_list = ''.join(num_list)
            dfs(num_list,idx+1)

if n_len == 1:
    print(-1)
else:
    dfs(n_str,0)
    print(num_max)
