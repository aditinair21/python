x=""
mylist=[]
while x != "quit":
  x= input("Enter a name: ")
  if x!="quit":
     mylist.append(x)
str(mylist)
print("The names you entered are" + str(mylist))