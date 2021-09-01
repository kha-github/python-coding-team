x,y,w,s = map(int, input().split())
m = min(x,y)
M = max(x,y)
if x==0 or y==0:
    if M % 2 ==0:
        if w < s:
            print(M * w)
        else:
            print(M * s)
    else:
        if (M-1)*s + w < M*w:
            print((M-1)*s + w)
        else:
            print(M*w)
elif w*2 < s:
    print((x+y)*w)
elif (x+y - 2*min(x,y)) % 2 == 0:
    if w<s:
        print(min(x,y)*s + (x+y-2*min(x,y))*w)
    else:
        print(min(x,y)*s + (x+y-2*min(x,y))*s)
else:
    if (x+y-2*min(x,y)-1)*s + w < (x+y-2*min(x,y))*w:
        print(min(x,y)*s + (x+y-2*min(x,y)-1)*s + w)
    else:
        print(min(x,y)*s + (x+y-2*min(x,y))*w)
