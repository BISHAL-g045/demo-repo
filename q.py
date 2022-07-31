a = input("Enter purchased amount")
b = int(a)
if(b>=5000):
   discount = b *(10/100)
elif(b>=4000 and b<5000):
  discount =  b * (7/100)
elif(b>=3000 and b<4000):
   discount = b* (5/100)
elif(b>=2000 and b<3000):
   discount = b*(3/100)
else :
    discount = b * (2/100)
print(discount)
