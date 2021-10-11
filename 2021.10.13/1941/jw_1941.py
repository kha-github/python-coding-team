position = []
for _ in range(5):
    position_line = input()
    position_line_item = []
    for i in position_line:
        position_line_item.append(i)
    position.append(position_line_item)

answer = 0

def dfs(a,b,idx,cnt,V):
    global answer
    if [a,b] in V:
        return
    if idx ==7:
        if cnt >= 4:
            answer+=1
            return
        else:
            return
    if position[a][b] == "S":
        cnt+=1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        new_position_idx_x = a + dx[i]
        new_position_idx_y = b + dy[i]
        if new_position_idx_x >=0 and new_position_idx_x<5 and new_position_idx_y>=0 and new_position_idx_y<5:
            V.append([a,b])
            dfs(new_position_idx_x, new_position_idx_y, idx+1, cnt, V)

for i in range(5):
    for j in range(5):
        visited=[]
        dfs(i,j,0,0,visited)
        
print(answer)
