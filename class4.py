#list

ex = []
a = type(ex)
print(a)

exx = [1,2,3,4,5]
b = type(exx)
print(b)

listt = [1,2,"hello" ,4,0]
c = type(listt)
print(c)



d =  list((1 , 2, 3, 4,5))
print(type(d))


#features of list :: changeable , ordered , Allow duplicates

animals = ["Panda","Tiger","Elephant","Giraffee"]  #ordered
print(animals)

animals[1] = "Lion" #Changeable(mutable)
print(animals)

animals = ["Panda","Tiger","Elephant","Giraffee","Panda"] #Duplicates
print(animals)


#Adding elements to list
animals.insert(0 ,"Lion")  #insert
print(animals)

animals.append("Zebra") #append : adds elemnt at last
print(animals)

animals.insert(-1 ,"Jaguar")
print(animals)

animals.extend(["Jaguar","Rhinoceros"]) #extend
print(animals)


#Removing elements from list
animals.pop()  #pop :: Removes last element from the list
print(animals)

animals.remove("Panda") #remove
print(animals)



animals = ["Panda","Tiger","Elephant","Giraffee"]  #clear
animals.clear()
print(animals)



#SORTING
animals = ["Panda","Tiger","Elephant","Giraffee"] #Capital case
print(animals)
animals.sort(reverse = True) #animals.sort(key = str.lower)
print(animals)

animals = ["panda","tiger","elephant","giraffee"] #Lower case
print(animals)
animals.sort(reverse = True)
print(animals)
