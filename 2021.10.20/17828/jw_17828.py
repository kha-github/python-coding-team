n, x = map(int,input().split())

if 26 * n < x or x < n:
    print("!")
else:
    answer = ['A'] * n
    x -= n
    idx = n-1
    while x >0:
        if x>=25:
            answer[idx] = "Z"
            idx-=1
            x-=25
        else:
            answer[idx] = chr(x+65)
            break
    print(''.join(answer))
