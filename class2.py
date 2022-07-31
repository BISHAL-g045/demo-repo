a ="good morning"
d ="good morning"
c = a is d
print(c)

#location
print(id(a))
print(id(d))


#membership operator
mem = "apple" in "pineapple"
print(mem)
ab = "good" in "Goodmorning"
print(ab)


#bitwise operator
print(2 & 4) #bitwise and
print(2 | 4)  #bitwise OR
print(2 ^ 4) #bitwise XOR


#Formatting
name = input("Enter your name")

roll = input("Enter your roll number")

print(" Your name is {} and roll number is {}".format(name , roll))


print(f"Your name is {name} and roll number is {roll}")
