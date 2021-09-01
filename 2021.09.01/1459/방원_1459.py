x,y,w,s = map(int,input().split())


root1 = (x+y)*w

if (x+y)%2==0:    
    root2 = max(x,y)*s
else:             
    root2 = (max(x,y)-1)*s + w

root3 = min(x,y)*s + abs(x-y)*w

result = min(root1, root2, root3)

print(result)
    