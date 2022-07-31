
#this is my variable
'''This is
my
comment'''

abc = "gOOD mORNING"
print(type(abc))
print(abc.upper())
print(abc.lower())
print(abc.capitalize())
print(abc.strip())

A = input("Enter your name").strip()
print(len(A))

#indexing
info = "Python Java"
splitted = info.split()
print(splitted)
" ".join(splitted)

a = info[0].lower()
print(a)

b = info[-2].upper()
print(b)

#Slicing
c = info[2:5]
print(c)

wish = "Good Morning"
d = wish[5: ]
print(d)
e = wish.index("M")
print(e)

#Enter email from user 
