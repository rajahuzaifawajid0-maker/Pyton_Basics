#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#Print the number of items in the list
print(len(thislist))
#check the data type of a list
print(type(thislist))
#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#To add an item to the end of the list, use the append() method
thislist.append("orange")
print(thislist)
#The remove() method removes the specified item.
thislist.remove("banana")
print(thislist)