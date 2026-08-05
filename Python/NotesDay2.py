"""
Algorithm ==> is a step-by-step instructions lead to the desired outcome. 
    or/     is a set of finite, well-defined steps or instructions designed to solve a problem or perform a computation.

How to express an Algorithm?
1. Natural Language: Written in plain English. Easy to describe, but can be unclear for complex problems.
2. Flowchart: Graphical representation of steps. Easier to visualize than natural language.
3. Pseudocode: Text-based, code-like instructions without language syntax.

==> in python max() is an inbuilt function which can be used to find the maximum value present among all the numbers


How to analyse an Algo: 
1. Priori:- Evaluates the algorithm theoretically, without running it, assumes some factors as constant.
2. Posterior:- Evaluates the algorithm practically, by executing it, measure real performance and depends on hardware and compiler.
"""


"""
List:- items are ordered, changable and allow duplicate values. The items are all indexed(0 to n).

To change order of list we have some specific built in methods such as:
1. append()	Adds an element at the end of the list
2. clear()	Removes all the elements from the list
3. copy()	Returns a copy of the list
4. count()	Returns the number of elements with the specified value
5. extend()	Add the elements of a list (or any iterable), to the end of the current list
6. index()	Returns the index of the first element with the specified value
7. insert()	Adds an element at the specified position
8. pop()	Removes the element at the specified position
9. remove()	Removes the item with the specified value
10. reverse()	Reverses the order of the list
11. sort()	Sorts the list
"""

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

# List Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(thislist[1])      # accessing items
# Negative indexing means start from the end


# to check if the item exist in the list ==> "in" keyword used
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# to append elements of one list into another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# we can also add tuples into list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# pop() used to remove a particular element
# del keyword is also used to remove a specific index element
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# clear() ==> empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# looping in list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# or/
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# or/
newlist = [x for x in range(10)]
print(newlist)


# to sort list using keyword argument(key = function)
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)



"""
Tuples:- ordered and unchangeable(we can not add or remove items from tuples after its been created), allow duplicate values, indexed(0 to n)
        A Tuple can contain different data types  
        tuple() constructor to make a tuple by using double round-brackets
"""

thistuple = ("apple",)
print(type(thistuple))      #needs to add comma after adding single item in tuple else will not be recognised as tuple

# to access tuple item use:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])        # indexing starts from end


# to copy list using slicing operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)




"""
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered and changeable. No duplicate members.
"""


# algo patterns: 
# mul update = sql script used(concat)- removes dirty read dirty write and n+1 problem
# hot data = readily availb {when large database i.e 1 gb around data}
# cold data = archive data 
# use csv/json (mockkro) and try implementing it