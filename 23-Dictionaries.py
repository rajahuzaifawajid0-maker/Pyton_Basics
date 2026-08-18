"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print("***Print the brand value of the dictionary***")
print(thisdict["brand"])
print("***Print the number of items in the dictionary***")
print(len(thisdict))
print("**** type ******")
print(type(thisdict))
#Make a change in the original dictionary,
#and see that the values list gets updated as well
print("****Value Updated******")
print(type(thisdict))
x = thisdict.values()

print(x) #before the change

thisdict["year"] = 2020

print(x) #after the change


print("****dict values are updated******")
thisdict["year"] = 2020
print(x) 

