"""import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())

#2진트리로 변경#
def get_bin(x, n=0):
    return format(x, 'b').zfill(n)

#1의 갯수를 세자!
N = 42

min_k = get_bin(N).count("1")
print(min_k)
print(bin)
answer = 0

for i in range(len(get_bin(N))-1, -1, -1):
    if get_bin(N)[i] == 1 and min_k > K :
        answer += 2 ** (len(bin) - i)
        N += 2 ** (len(bin) - i)

print(answer)


"""
def get_bin(x, n=0):
    return format(x, 'b').zfill(n)

print(get_bin(10))

# 1010100 k = 2
#    1000
#    1000
#   10000
# 1100000

answer = int('10000', 2)+ int('1000', 2) + int('1000', 2)
print(answer)





