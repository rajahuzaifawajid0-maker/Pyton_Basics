"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.
"""
thisset = {"apple", "banana", "cherry"}
print("****************")
print(thisset)
print("***************duplicate value are not printed**************")
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print("***Check if banana is present in the set***")
print("banana" in thisset)
print("***Check if banana is not present in the set***")
print("banana" not in thisset)
print("***Add an item to a set using the add() method***")

thisset.add("orange")

print(thisset)

print("***Add elements from tropical into this set***")
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

print("***Remove an item to a set using the remove() method***")
thisset.remove("pineapple")
print(thisset)
print("***Remove banana by using the discard() method***")
thisset.discard("banana")

print(thisset)
print("***Remove a random item by using the pop() method***")
x = thisset.pop()

print(x)

print(thisset)
