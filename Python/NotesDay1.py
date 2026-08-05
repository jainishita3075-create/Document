# to take input from user:- n = datatype(input())
print("Hello")
print("Hey,there!")

# to print in the same line 
print("Hello,", end=" ")
print("My name is Ishita.")

# to print numbers and text together
print("I am", 20, "years old")

"""
This is used for multiline commenting
"""

"""
variables: objects for storing data
in python variables are created when you first assign the value to it.
"""

x = "Amy is"
y = 10
print(x,y)

# type of variable can be changed even after its been set(overriding)
n = 2
n = "Name"
print(n)

# type casting

a = str(3)
b = int(3)
c = float(3)
print(a,b,c)

# to get the data type of the function = "type()" function is used

x = 10.0
print(type(x))

# string can be declared both in "" or '' quotes
# python is case sensitive 

a = 90
A = "English"
print(a)
print(A)

"""
Variable Names Types:
1. Camel case: myVariableType
2. Pascal case: MyVariableName
3. Snake case: my_variable_name

we can assign multi values in a single line
"""

x,y,z = "A","B","C"
print(x)
print(y)
print(z)

# Sim we can also assign the ,multi variables with same values

i = j = k = "Orange"
print(i)
print(j)
print(k)

# unpacking list in python

fruits = ["apple","banana","cherry"]
x,y,z=fruits
print(x,y,z) 

# unpacking tuples in python

fruits = ("apple", "banana" , "cherry")
(x,y,z) = fruits
print(x,y,z)
# use of + is also same as ,  just with no space we need to insert space in declaring of that variable value
print(x + y + z)
a = 10
b = 15
print(a+b)
a = 5
b = "John"
print(a,b)  # we can not use print(a+b) as it return error

# use of * in a tuple result in assigning of all the leftover values to the variable with *sign by creating a list of remaining values
# this feature in python is called as "Extended iterable unpacking"
# now if we will use type() for fruits its class will be tuples but for *red it will be list
fruits = ("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
print(type(fruits))
print(type(red))
print(type(yellow))


"""
Global Variables: variables that can be created outside of a function and can be used by everyone both inside and outside of function
Local Variable: variable created inside the function and can be used locally only i.e inside the function only
Note:- we can use global keyword to create the variable global inside the function
"""

x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

"""
Data Type:
1. int:- whole no, +ve or -ve without decimal and unlimited length
2. float:- +ve or -ve with 1 or more decimals, can also indiacte scientific numbers with an 'e' indicating power of 10
3. complex:- numbers written with j(imaginary part)

Python has a built in module called "random" that is used to make random numbers
"""

import random
print(random.randrange(1,10))


"""
String in Python: 
"""
# to print multiline string we can use """ """/''' ''' and assign it to a variable

a = """This is unacceptable"""
b = '''What is this?'''
print(a)
print(b)

# Strings can be used as an array
a = "Hello World!"
print(a[6], a[5], a[1])
# looping in a string
for x in 'banana':
    print(x)
# to find length of string
a = "My name is abc"
print(len(a))
# to check for a certain character prensent in a string "in" keyword is used
txt = "Nothing is free in this world."
print("free" in txt )       # return boolean value

if "free" in txt:
    print("Yes, 'free' is present")

# to check if word is not present in text
print("what" not in txt)

if "what" not in txt:
    print("No, 'what' is not present")


''' Slicing String: used to return range of characters by using slice syntax'''
b = "Hello, World!"
print(b[2:5])
# it can also be sliced from start
print(b[:5])
# it can aslo be sliced till the end
print(b[2:])
# negative indexing: used to start the slicing from end of the string
print(b[-5:-2])
# to reverse a string
a = "String"
print(a[::-1])
# here start and end is nothing and step is -1 as we take 1 step back at a time

# to return in upper or lower case: use of .upper()/.lower() function used
a = "Hello, World"
print(a.upper())
print(a.lower())

# to remove whitespace strip() is used if space is before or after the actual text
a = " Hello, World"
print(a.strip())

# Replace String
a = "Hello, World"
print(a.replace("H", "J"))

# split() methods returns a list where text is specified 
print(a.split(","))

# String concatenation: combining 2 strings using + operator
a = "hello"
b = "world"
c = a+" "+b
print(c)

'''
F-String: used to merge string and int in a single sentence 
using f in front of string literal and placing variable in curly braces
in this {age} is inside placeholder
'''

age = 20
txt = f"if you are {age} or above then only you can enter"
a = f"I am {19}"
b = f"answer is {18*3}"
print(f'price is {age:.2f} dollars')
print(txt)
print(a)
print(b)


"""
Escape character = \, helps to insert a character, even if it is illegal such as double quotes inside double quotes
1. \' ==> used for sentences such as It's okay, etc.
2. \\ ==> used to insert 1 backslash in a sentence
3. \n ==> used to shift in other line
4. \r ==> used to return the world written next to it
5. \t ==> tab key
6. \b ==> backspace, removes space from front
7. \f ==> form feed
8. \ooo ==> octal value
""" # 9. \xhh ==> hex value


txt = "We are here from the \"North\""
print(txt)
txt = "What are \byou doing here"
print(txt)


"""
1. capitalize() = first char to upper case
2. casefold() = string to lower case
3. center() = centers the text by moving to the space of char defined by user
4. count() = return the no of times the specified value occurs in a string
5. encode() = returns an encoded version of string
6. endswith() = returns true if the string ends with a specified value
7. expandtabs() = set the tab size of string
8. find() = search for specific value and written its place it was found at
9. format() = formats specifieed value in a string
10. format_map() = one mapping object, usually a dictionary.
"""

txt = "banana"
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)        # here it matches the word present or not not the whole string


# string.count(value, start, end) for specified value to appear in string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

"""
price = 49
txt = f"For only {price:.2f} dollars!"
print(txt)  or 
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
"""


data = {
    "name": "Ishita",
    "age": 21
}
txt = "My name is {name} and I am {age} years old."
print(txt.format_map(data))


# Functions that returns boolean values are:-    isinstance()

x = -10.0
print(isinstance(x,float))

"""
Arithmetic Operations:
1. + = add 2 values
2. - = sub 2 values
3. * = mul 2 values
4. / = div 2 values
5. % = returns rem after div of 2 values
6. **(exponential) = (2**5) ==> gives 5 in power of 2 and returns its value
7. //(floor division) = (15//2) ==> gives result as quotient of the 2 numbers
"""

"""
Assignment Operators:
1. = (assigns value)
2. += (add value to the existing value)
3. -= (sub value from existing value)
4. *= (mul value into the existing value)
5. /= (div value from the existing value)
6. %= (shows rem left after div of value from existing value)
7. //= (returns quotient after div of values from existing value)
8. **= (returns the value by powering value into existing value)
9. &= (x = 5, x &= 3,print(x)), bitwise manipulation and
10. ^= (x = 5, x ^= 3,print(x)), bitwise manipulation xor
11. |= (x = 5, x |= 3,print(x)), bitwise manipulation or
12. >>= (x = 5, x >>= 3,print(x)), bitwise manipulation right shift assignment
13. <<= (x = 5, x <<= 3,print(x)), bitwise manipulation left shift
14. :=  (print:=3) value = 3 returned, called as Walrus Operator
"""

numbers = [1, 2, 3, 4, 5]       
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


# Ternary operator: helps to assign 1 value if true and another if false
num = 2
x = "weekend" if num>5 else "workday"
print(x)

# chaining comparision operators
x = 5
print(1 < x < 10)
print(1 < x and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10)) # reversing values with not


"""
Identity Operator: returns true if object are same 
1. is (Returns True if both variables are the same object)
2. is not (Returns True if both variables are not the same object)
"""


# === used to compare memory location and == is used to compare value
# pep8(Python Enhancement Proposal 8) => official style guide for writing clear, readable, and consistent Python code, focusing on core practices like indentation, line length, and naming conventions.
# String sanitization = is the process of cleaning, filtering, or modifying a string to ensure it is safe, consistent, and well-formatted for your application.
# use common exception == Exception, following heirarchy
"""__init__.py ==> is a special file used to mark a directory as a regular Python package, making the modules within that directory importable.
function ==> doc string = "stores description; purpose, args and args types, how to call the func"
"""