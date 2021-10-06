def calc_days(month, day):
    return sum(days[1: month]) + day


terms = []
result = []
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
START = calc_days(3, 1)
END = calc_days(11, 30)
now = START
n = int(input())

for i in range(n):
    term = list(map(int, input().split()))
    terms.append([calc_days(term[0], term[1]), calc_days(term[2], term[3])])

# 시작 일자와 종료 일자가 늦은 순으로 정렬
terms.sort(key=lambda x: (x[0], -x[1]))
print(terms)
print(START, END)


for i in range(n):
    start, end = terms[i][0], terms[i][1]
    if start > END:
        break
    if start <= now < end:
        if len(result) > 0 and result[len(result) - 1][1] - now < end - now:
            result.pop()
        now = end
        result.append(terms[i])

print(result)

