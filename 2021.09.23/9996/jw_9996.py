n = int(input())
pat = input()
for i in range(len(pat)):
    if pat[i] == "*":
        idx = i
        break

pat_first = pat[:idx]
pat_last = pat[idx+1:]
ans = []
for _ in range(n):
    chk = input()
    flag = "NE"
    if len(chk) >= len(pat) - 1:
        if chk[:idx] == pat_first and chk[len(chk) - len(pat) + idx+1:] == pat_last:
            flag = "DA"
    ans.append(flag)
    
for i in ans:
    print(i)
