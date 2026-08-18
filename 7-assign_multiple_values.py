# Assigning multiple values at once

a=1
b=2
c=3
d= "this is string"

print(a)
print(b)
print(c)
print(d)

print("########################################")

a, b, c, d = 1, 2, 3, "huzaifa"
print(a)
print(b)
print(c)
print(d)

print("########################################")

x = 1
y = 1
z = 1


y=x

z = y

print(x)
print(y)
print(z)

x = y= z ="this is string"

print(x)
print(y)
print(z)


print("################### unpack list ##################")

fruits = ["apple", "banana", "cherry"]

print(type(fruits)) #check type of list

fruit1 ,fruit2,fruit3 = fruits
print(fruit1)
print(fruit2)
print(fruit3)



x = "5" # or str(5)
y = "John"
print(x + y)