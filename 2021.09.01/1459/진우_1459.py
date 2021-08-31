x,y,w,s = map(int, input().split())
if x==0 or y==0 or w*2 < s:
    print((x+y)*w)
else:
    print(min(x,y)*s + (x+y-2*min(x,y))*w)
