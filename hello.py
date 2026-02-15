print("Hello, World!")

if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")
        
x =5
y = "Helllo, World!"

#This is a comment.
print("Hello, World!")  # This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

x = 5
y = "John"
print(x)
print(y)

x = 4 # x is of tye int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y)) 

x = "John"
# is the same as
x = "John"
print(x)


a = 4
A = "Sally"
#A will not overwrite a
print(A)
print(a)


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

myVariableName = "John"
print(myVariableName)
my_variable_name = "John2"
print(my_variable_name)

x, y, z = "Orange", "Banana", "Cherry"
print (x)
print (y)
print (z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(fruits)

x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome "
print (x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)  # This will raise an error because you cannot add an int and a str










x = "awesome"

def myfunc():
    print("Python is " + x)
    
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()
print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"
  
myfunc()
print("Python is " + x)


x= "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = frozenset({"apple", "banana", "cherry"})
print(x)




x = 1 #int
x = 2.8 #float
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))


x = 1
y = 335656222554887711
z = -325522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))  

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))  
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))




x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from in to float:
a = float(x)

#convert from float to int:
b = int(y)

#conver from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))


x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)

x = str("s1") # x will be 's1'
y = str(2) # y will be '2'
z = str(3.0) # z will be '3.0'
print(x)
print(y)
print(z)

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)
    
a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("A" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is there.")
    
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT there.")

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "This will insert one \\ (backslash)"
print(txt)

txt = "Hello\bWorld"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "36 is my age."
x = txt.capitalize()
print (x)

txt = "banana"
x = txt.center(20, "z")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 8, 24)
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

print(10 > 9)
print(10 == 9)
print (10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True
print(myFunction())

def myFunction() :
    return False
if myFunction():
    print("YES!")
else:
    print("NO!")
    
x = 200
print(isinstance(x, str))

print(10 + 5)

print(x := 3)

x = 5 
y = 3
print(x <= y)

x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x < 5 and x < 10))
print(x < 5 and x < 10)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because y is not the same object as x
print(x != y)
# to demonstrate the difference between "is not" and "!=": this comparison returns False beacuse x is equal to y

x = ["apple", "banana"]
print("banana" in x) # returns True because a sequence with the value "banana" is in the list
print("banana" not in x)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~6)
print(6 << 3) # 00000110 -> 00110000
print(6 >> 3) # 00000110 -> 00000000

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
print((6 + 3) - (6 + 3))
print(100 - 3 ** 3)

print(100 - ~3)
print(6 & 2 + 1) # 00000110 & 00000011 = 00000010
print(6 ^ 2 + 1) # 00000110 ^ 00000011 = 00000010
print(6 | 2 + 1) # 00000110 | 00000011 = 00000111
print(5 == 4 + 1) # True because 5 is equal to 4 + 1

x = 5
x ^= 3
print(x) # x is now 6 because 5 ^ 3 = 6, 00000101 ^ 00000011 = 00000110

print(not 5 == 5)
"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""

print(1 or 2 and 3)
print(4 or 5 + 10 or 8)
print(5 + 4 - 7 + 3)

START PYTHON LISTS