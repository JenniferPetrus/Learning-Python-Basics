print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give?"))
people = int(input("How many people to split the bill?"))
pay = round(((bill + (tip/100)*bill) / people), 2)
print(f"Each person should pay: ${pay}")

# Number Manipulation
score = 0
# User scores a point
score += 1
print(score) # score 1
# +=   -=   *=   /=
# f-strings = insert a varaible or an expression into a string
print(f"Your score is =  {score}")

height = 1.65
weight = 84
bmi = (84 / 1.65 ** 2)
print(bmi) # 30.85399
print(int(bmi)) # 30
print(round(bmi)) # 31
print(round(bmi, 2)) # 30.85 = number of digits

# PEMDASLR
# 1. ()    2. **    3. * OR /   4. + OR -
print(3 * (3 + 3) / 3 - 3) # = 3

# Mathematical Operations
print(12 + 34)
print(7 - 3)
print(3 * 2)
print(2 ** 3) # = 2 * 2 * 2 = 8
print(5 / 3) # float = 1.666666
print(5 // 3) # int = 1

# Make this line of code run without errors:
# print("Number of letters in your name: " + len(input("Enter your name")))
# TypeError: can only concatenate str (not "int") to str
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Type Conversion: convert a string into a number/integer: 579
print(int("123") + int("456"))

# Type Checking of a view data types
print(type(2.2)) # float
print(type(True)) # bool
print(type(343)) # int
print(type("Tree")) # str

# Type Checking: Check data type: <class 'str'>
print(type("Cat"))

# Length of a string: 5
print(len("12345"))

# Subscripting
print("Hello"[0])

# String -> Concatenation: 123345 
print("123" + "345")

# Integer = Whole Number: 468
print(123 + 345)

# Large Integers: 123456789
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)