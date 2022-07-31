#d = [1,2,3,4,5]
#for i in d:
#    print(i, end = ' ')

#tup = (1,2,3,4,5)
#for j in tup:
#   print(j + 5)
   
#for i in "Hello":
#   print(i, end = '  ')



count = 0
countt = 0
for i in "Hello":
    if i in "aeiou":
        count = count + 1
    else:
        countt = countt + 1
print(f"number of vowels: {count}")
print(f"number of consonants: {countt}")




for i in [1,2,3,4]:
    if i == 1:
      print(i)
else:
    print("NONE")
