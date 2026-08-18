"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
"""
#for simple for loop
a = "Pakistan"
for i in a:
    print(i)
#for dic loop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict:
    print(thisdict[i])
    print(thisdict,i)
