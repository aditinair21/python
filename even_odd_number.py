x=input("Enter a number: ")
x=int(x)
y=0
while y<x:
  if y%2==1:
    print(y)
  y=y+1
if x%2==0:
  print(str(x)+" is an even number")
elif x%2==1 :
  print(str(x)+" is an odd number")