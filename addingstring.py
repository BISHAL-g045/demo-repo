a = []
a.extend(["Leopard","Lion","Tiger"])
print(a)
a.insert(2,"Jaguar")
print(a)
a.append("Cat")
print(a)
a.sort(reverse = True)
print(a)
b = a[-2]
print(b)
c = b.upper()
print(c)
print(f"The second last element of the list is {c}")

