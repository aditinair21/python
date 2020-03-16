name=input("Enter ur name: ")
y=(len(name))
k=0
for i in range(0,y):
  if (name[i]=="a" or name[i]=="A" or name[i]== "E" or name[i]=="I" or name[i]=="O" or name[i]=="U" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u"):
   s=(name[i])
   print(s)
   k=k+1
print(k)