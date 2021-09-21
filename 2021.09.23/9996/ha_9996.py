n = int(input())

pattern = input()
mylist = pattern.split("*")

for _ in range(n):
  myword = input()
  if len(myword) >= len(pattern)-1:
    if myword[0:len(mylist[0])] == mylist[0] and myword[len(myword)-len(mylist[1]):] == mylist[1]:
      print("DA")
    else:
      print("NE")
  else:
    print("NE")
