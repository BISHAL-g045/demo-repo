name = input("Enter Your Name")
mail = input("Enter your Mail")
print(name)
print(mail)
A = name.find(' ')
B = mail.find('@')
C =B + 1
D = mail.find('.')
FirstName = name[0:A]
LastName = name[A+1 : ]
print("First Name = ",FirstName)
Domain = mail[C : D]
print("Domain = ",Domain)

print("Your first name is {1} and Domain is {0}".format(FirstName,Domain))
print(f"Your first name is {FirstName} and last name is {LastName}")
