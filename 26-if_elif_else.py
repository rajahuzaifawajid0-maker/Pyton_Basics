# ==================================================
# IF, ELIF, ELSE IN PYTHON
# ==================================================

# if:
# if ka matlab hai "agar".
# Python sab se pehle if ki condition check karta hai.
# Agar condition True ho, to if ke andar wala code chalega.

# elif:
# elif ka matlab hai "agar pehli condition False ho".
# Ye doosri ya additional condition check karta hai.

# else:
# else tab chalta hai jab if aur tamam elif
# ki conditions False hon.


# Example: Student Marks

marks = 75

# Pehle check hoga:
# Kya marks 80 ya us se zyada hain?
if marks >= 80:
    print("Grade A")

# Agar upar wali condition False hai,
# to ye condition check hogi:
# Kya marks 60 ya us se zyada hain?
elif marks >= 60:
    print("Grade B")

# Agar upar wali dono conditions False hain,
# to ye condition check hogi:
# Kya marks 40 ya us se zyada hain?
elif marks >= 40:
    print("Grade C")

# Agar koi bhi condition True nahi hui,
# to else chalega.
else:
    print("Fail")


# Output:
# Grade B