n = 1
while True:
    s = input()
    if s[0] == '-':
        break
    change = 0
    q = []
    for i in s:
        if not q and i == '}':
            change += 1
            q.append('{')
        elif i == '}':
            q.pop()
        else:
            q.append(i)
    change += len(q) // 2
    print(f'{n}. {change}')
    n += 1