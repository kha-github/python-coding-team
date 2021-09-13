alphadict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
numdict = {'1':'I', '5':'V', '10':'X', '50':'L', '100':'C', '500':'D', '1000':'M', '4':'IV', '9':'IX', '40':'XL', '90':'XC', '400':'CD', '900':'CM'}

def alphaToNumber(alpha):
  result = 0
  before = -1
  for i in range(len(alpha)-1, -1, -1):
    if before <= alphadict[alpha[i]]:
      result += alphadict[alpha[i]]
      before = alphadict[alpha[i]]
    else:
      result -= alphadict[alpha[i]]
  return result

def numToAlpha(number):
  result = ""
  mulval = ""
  while number != 0:
    temp = int(number%10)
    if temp == 1 or temp == 4 or temp == 5 or temp == 9:
      result = numdict[str(temp)+mulval] + result
    elif temp == 2 or temp == 3:
      result = numdict["1"+mulval]*temp + result
    elif temp == 6 or temp == 7 or temp == 8:
      result = numdict["5"+mulval]+numdict["1"+mulval]*(temp%5) + result
    mulval += "0"
    number /= 10

  return result


first = input()
second = input()

resultNum = alphaToNumber(first) + alphaToNumber(second)
print(resultNum)
print(numToAlpha(resultNum))



