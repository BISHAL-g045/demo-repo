import random
inport random as r
SyntaxError: invalid syntax

import random as r

r.random()
0.9617124125958074

r.random(0 , 20)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    r.random(0 , 10)
TypeError: Random.random() takes no arguments (2 given)

r.randrange(1,10)
8
r.randrange(0,101,2) #generating even numbers
72

r.randrange(1,101,2) #generating odd numbers
33

r.choice(options)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    r.choice(options)
NameError: name 'options' is not defined
options = [ "Rock" , "Paper"]
opt = ["Rock" , "Paper" , "Scissors"]
r.choice(opt)
'Paper'
r.sample(options, k=2)
['Rock', 'Paper']



