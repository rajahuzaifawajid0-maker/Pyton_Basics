employee = "   muhammad ali khan   "

print("Original:", employee)

employee = employee.strip()

print("After strip:", employee)
print("Title:", employee.title())
print("Upper:", employee.upper())
print("Lower:", employee.lower())
print("Capitalize:", employee.capitalize())
# Task 2: Email Validation System

# Email address
email = "student123@gmail.com"

# Check email starting
print("Starts with student:", email.startswith("student"))

# Check email ending
print("Ends with gmail.com:", email.endswith("gmail.com"))

# Find position of @
print("@ position:", email.find("@"))

# Count @
print("Number of @:", email.count("@"))

# Replace gmail.com with company.com
new_email = email.replace("gmail.com", "company.com")
print("New Email:", new_email)

# Check basic email format
if email.count("@") == 1 and email.endswith("gmail.com"):
    print("Email is Valid")
else:
    print("Email is Invalid")
    # Task 3: Product Code Analyzer

    # Product code
    product = "LAPTOP-HP-2025"

    # Split product using -
    parts = product.split("-")

    # Get category
    category = parts[0]

    # Get brand
    brand = parts[1]

    # Get year
    year = parts[2]

    # Display information
    print("Category:", category)
    print("Brand:", brand)
    print("Year:", year)

    # Partition the product
    print("\nPartition:")
    print(product.partition("-"))

    # Right partition
    print("\nRpartition:")
    print(product.rpartition("-"))

    # Join values using |
    result = "|".join([brand, category, year])

    # Display final result
    print("\nJoined:")
    print(result)
    # Task 4: User Login Validator

    # Username
    username = "Student_01"

    # Password
    password = "Pass12345"

    # Check username
    print("Username:", username)

    # Check valid identifier
    print("Is identifier:", username.isidentifier())

    # Check letters and numbers
    print("Is alphanumeric:", username.isalnum())

    # Check password
    print("\nPassword:", password)

    # Check letters and numbers
    print("Is alphanumeric:", password.isalnum())

    # Check only letters
    print("Is alphabet:", password.isalpha())

    # Check only digits
    print("Is digit:", password.isdigit())

    # Check numeric
    print("Is numeric:", password.isnumeric())
    # Task 5: Financial Report Cleaner

    # Financial report
    report = "     Total Sales = 250000 PKR      "

    # Remove extra spaces
    report = report.strip()

    # Remove text
    report = report.replace("Total Sales = ", "")

    # Split the remaining text
    parts = report.split()

    # Get only the number
    amount = parts[0]

    # Convert string into integer
    amount = int(amount)

    # Display result
    print("Sales Amount:", amount)
    print("Data Type:", type(amount))
    # Task 6: Password Strength Checker

    # Password
    password = "Python@123"

    # Variables for counting
    digits = 0
    uppercase = 0
    lowercase = 0
    symbols = 0

    # Check every character
    for char in password:

        # Check digit
        if char.isdigit():
            digits = digits + 1

        # Check uppercase
        elif char.isupper():
            uppercase = uppercase + 1

        # Check lowercase
        elif char.islower():
            lowercase = lowercase + 1

        # If it is not a letter or number, it is a symbol
        else:
            symbols = symbols + 1

    # Display results
    print("Password:", password)
    print("Number of digits:", digits)
    print("Number of uppercase letters:", uppercase)
    print("Number of lowercase letters:", lowercase)

    # Check symbols
    if symbols > 0:
        print("Password contains symbols: Yes")
    else:
        print("Password contains symbols: No")

    # Count @ symbol
    print("Number of @:", password.count("@"))
# Task 7: Chat Application Formatter

# Message
message = "hello everyone welcome to python programming"

# Convert to title case
print("Title:")
print(message.title())

# Capitalize first letter
print("\nCapitalize:")
print(message.capitalize())

# Center the message
print("\nCenter:")
print(message.center(60))

# Align message to left
print("\nLeft:")
print(message.ljust(60))

# Align message to right
print("\nRight:")
print(message.rjust(60))
# Task 9: Customer Feedback Analyzer

# Customer feedback
feedback = "Good product. Good quality. Good packaging."

# Count Good
good_count = feedback.count("Good")

# Replace Good with Excellent
new_feedback = feedback.replace("Good", "Excellent")

# Split feedback into words
words = feedback.split()

# Count total words
total_words = len(words)

# Display results
print("Number of Good:", good_count)

print("\nAfter replacement:")
print(new_feedback)

print("\nTotal words:", total_words)
# Task 10: Invoice Generator

# Customer information
name = "Ali"
product = "Laptop"
price = 85000

# Using format()
invoice = "Customer : {}\nProduct  : {}\nPrice    : {}".format(
    name, product, price
)

# Display invoice
print(invoice)

# Dictionary for format_map()
data = {
    "name": name,
    "product": product,
    "price": price
}

# Using format_map()
invoice2 = "Customer : {name}\nProduct  : {product}\nPrice    : {price}".format_map(data)

# Display invoice
print("\nUsing format_map():")
print(invoice2)