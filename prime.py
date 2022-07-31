#to check given number prime or not

num = 101
for i in range(2 ,num):
    if(num%i == 0):
      print("Composite")
      break
else:
    print("Prime")



#generating numbers


for i in range(1, 101):
 if num>1:
   for i in range(2, i):
      if num % i == 0:
        break
    
   else:
        print(i)

