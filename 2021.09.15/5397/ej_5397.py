from collections import deque


def solution(keys):
    password = deque()
    for key in keys:
        if key == ">":
            password.rotate(1)
        elif key == "<":
            password.rotate(-1)
        elif key == "-":
            if len(password) > 0:
                password.pop()
        else:
            password.append(key)
    return ''.join(password)


for _ in range(int(input())):
    print(solution(list(input())))
