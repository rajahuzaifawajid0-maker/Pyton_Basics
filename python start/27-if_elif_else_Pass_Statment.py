"""
if statements cannot be empty, but if you for some reason have an if statement with no content,
put in the pass statement to avoid getting an error.
"""
a = 33
b = 200

if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement


age = 20

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")


#This works correctly with pass:
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

#Using pass in different branches:

value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")