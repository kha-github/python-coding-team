n = int(input())

li1 = list(map(int,input()))
li2 = list(map(int,input()))

#print(li1)

def convert(a):                 # 전구 상태 변경
    if a == 0:
        return 1
    else:
        return 0

k=2

for p in range(k):

    cnt=0

    arr1 = li1[:] #arr1 초기화
    arr2 = li2[:] #arr2 초기화

    if p == 0:                      # 맨 처음 전구 상태 변경하지 않을 때
        for i in range(n):

            if i == 0:
                pass
                #print(arr1)

            elif i == n-1:

                if arr1[i-1] != arr2[i-1]:
                    arr1[i-1]=convert(arr1[i-1])
                    arr1[i]=convert(arr1[i])
                    cnt+=1
                    #print(arr1)
                else:
                    pass
            else:

                if arr1[i - 1] != arr2[i - 1]:
                    arr1[i - 1] = convert(arr1[i - 1])
                    arr1[i] = convert(arr1[i])
                    arr1[i+1] = convert(arr1[i+1])
                    cnt+=1
                    #print(arr1)

                else:
                    pass

        if arr1 == arr2:
            answer = cnt
            break

        else:
            answer = -1


    else:                                # 맨 처음 전구 상태 변경할때

        for i in range(n):

            if i == 0:

                arr1[i] = convert(arr1[i])
                arr1[i+1] = convert(arr1[i+1])
                cnt += 1
                #print(arr1)
                #print(arr1)

            elif i == n - 1:

                if arr1[i - 1] != arr2[i - 1]:
                    arr1[i - 1] = convert(arr1[i - 1])
                    arr1[i] = convert(arr1[i])
                    cnt += 1
                    #print(arr1)

                else:
                    pass
            else:

                if arr1[i - 1] != arr2[i - 1]:
                    arr1[i - 1] = convert(arr1[i - 1])
                    arr1[i] = convert(arr1[i])
                    arr1[i + 1] = convert(arr1[i + 1])
                    cnt += 1
                    #print(arr1)

                else:
                    pass

        if arr1==arr2:
            answer = cnt
        else:
            answer = -1

if li1==li2:
    answer = 0

print(answer)








