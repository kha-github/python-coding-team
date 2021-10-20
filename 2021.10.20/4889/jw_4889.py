idx=0
finish = []
while True:
    a = input()
    idx +=1
    if '-' in a:
        break
    stack = []
    answer = 0
    for i in a:
        if i == '{':
            stack.append("{")
        elif i == '}':
            if stack:
                stack.pop()
            else:
                answer += 1
                stack.append("{")
                
    if stack:
        answer += len(stack)/2
    finish.append([idx,answer])

for i in finish:
    print("%d. %d" %(i[0],i[1]))
