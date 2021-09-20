n = int(input())
start, end = input().split("*")

for _ in range(n):
    name = input()
    # 대상 문자열이 비교 문자열보다 짧을 경우 패턴 불일치
    if len(name) >= (len(start) + len(end)) \
            and name.startswith(start) and name.endswith(end):
        print("DA")
    else:
        print("NE")
