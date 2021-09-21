t = int(input())
answer_print = []
for _ in range(t):
    n = int(input())
    call = []
    for i in range(n):
        call.append(input().replace(" ",""))
    call = sorted(call)
    answer = "YES"
    for i in range(n-1):
        if call[i] == call[i+1][:len(call[i])]:
            answer = "NO"
    answer_print.append(answer)

for i in answer_print:
    print(i)
