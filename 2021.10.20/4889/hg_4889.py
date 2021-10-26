# 다시 보기
import sys
sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

index = 1
while True:
    strings = input()
    if "-" in strings:
        break

    stack = []
    answer = 0

    for s in strings:
        if not stack:
            stack.append(s)

        elif s == "}" and stack[-1] == "{":
            stack.pop()

        elif s == "{" :
            stack.append(s)
            answer += 2



    print(f"{index}. {answer}")
    index += 1
