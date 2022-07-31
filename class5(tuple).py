#Features of tuple :: Ordered , not changeable(immutable) , allow duplicates
tup = ("Apple","Bsnana","Mango")
print(tup)
a = list(tup)
print(type(a))
a[0] = "Pineapple"
print(tuple(a))


c = (1,2,3,4)
c = c + (5,6,7,8,9)
print(c)

#tuple pacling and unpacking

p,q,r = (2,3,4)
print(p)
print(q)
print(r)

*a , b , c = (2,3,4,5,6,7,8,9,10)
print(a)
print(b)
print(c)


