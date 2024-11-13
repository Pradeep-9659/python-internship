import string
import random
length=int(input("Enter the length of password:"))
print("choose the set of password"
      "\n"
      "1.Digits"
      "\n"
      "2.Letters"
      "\n"
      "3.Special charaters")
A=""
choice=int(input("Pick the option:"))
if (choice==1):
    A+=string.ascii_letters
elif (choice==2):
    A+=string.digits
elif(choice==3):
    A+=string.punctuation
password=[]
for i in range(length):
    B=random.choice(A)
    password.append(B)
print("".join(password))



