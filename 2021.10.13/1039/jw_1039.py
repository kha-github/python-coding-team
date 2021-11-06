import copy

n,k = map(int,input().split())
n_len = len(str(n))
n_str = str(n)
num_max = 0

def dfs(num,idx):
    global num_max
    if idx == k:
        print(num)
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
            num_copy = copy.deepcopy(num_list)
            dfs(num_copy,idx+1)

if n_len == 1 or str(n)[1:] == "0"* (n_len-1):
    print(-1)
else:
    dfs(n_str,0)
    print(num_max)
