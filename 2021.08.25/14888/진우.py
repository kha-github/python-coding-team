import itertools
N = int(input())
A = list(input().split())
B = list(map(int, input().split()))

if len(A) != N or len(B)!=4 or sum(B)!=N-1:
    exit()
op=[]
for i in range(B[0]):
    op.append('+')
for i in range(B[1]):
    op.append('-')
for i in range(B[2]):
    op.append('*')
for i in range(B[3]):
    op.append('//')
    
op_list = list(itertools.permutations(op))
m=A[0]
sum_list = []

for o in op_list:
    for i in range(N-1):
        m = str(eval(m+o[i]+A[1+i]))
    sum_list.append(m)
    m=A[0]
print(max(sum_list))
print(min(sum_list))
