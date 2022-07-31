#if else
import random as r
number = r.randrange(-100,100)
if(number>0):
  print(f"{number} is postive")
elif(number == 0):
  print(f"{number} is zero")
else:
    print(f"{number} is negative")


a = input("Enter a number")
b = int(a)
print(type(b))

if(b%2==0):
  print(f"{b} is even")
else:
  print(f"{b} is odd")
