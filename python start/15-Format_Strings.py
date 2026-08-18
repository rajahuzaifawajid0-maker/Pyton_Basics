#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this
age = 36
#This will produce an error:
txt = "My name is John, I am " + str(age)
print(txt)
#Create an f-string
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#Add a placeholder for the price variable
price = 50
txt = f"The price is {price} dollars"
print(txt)
#Display the price with 2 decimals
price = 50
txt = f"The price is {price:.2f} dollars"
print(txt)
#Perform a math operation in the placeholder, and return the result
txt = f"The price is {20 * 59} dollars"
print(txt)


