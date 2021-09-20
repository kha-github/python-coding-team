n = int(input())
word = [input() for _ in range(n)]
count = 0

# 자신보다 짧은 문자열과 비교하는 경우의 수를 줄이기 위해 길이순 정렬
word.sort(key=len)
for i in range(n):
    target = word[i]
    for j in range(i + 1, n):
        # startswith 과의 차이점 무엇
        if target == word[j][:len(target)]:
            count += 1
            break
print(len(word) - count)
