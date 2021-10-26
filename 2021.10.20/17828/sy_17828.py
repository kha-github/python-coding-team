n, x = map(int, input().split())

if n > x or n * 26 < x:
    print('!')
else:    
    wallet = [1] * n
    z = (x - n) // 25
    for i in range(z):
        wallet[-i - 1] += 25
    remain = (x - n) % 25
    if remain:
        wallet[- z - 1] += remain
    
    for i in wallet:
        print(chr(64 + i), end='')