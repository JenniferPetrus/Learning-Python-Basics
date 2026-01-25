# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level
# password = ''
# for char in range(0, nr_letters):
#     password += random.choice(letters)
    
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
    
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)    
# print(f"Your password is: {password}")

# Hard Level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
    
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

    
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(f"Your password is: {password_list}")
random.shuffle(password_list)
print(f"Your password is: {password_list}")

password = ''

for char in password_list:
    password += char
print(f"Your password is: {password}")

# FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# for loops and the range() function
total = 0
# for number in range(1, 10, 3): # range between 1 and 9, (1, 10, 3) = steps by 3 = 1, 4, 7
for number in range(1, 101):
    total += number
print(total)

# Highest Score
student_scores = [150, 142, 185, 120, 171, 186, 24, 199, 68, 86, 45, 129]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
# total_exam_score = sum(student_scores)
# sum = 0
# for score in student_scores:
#     sum += score
    
# print(sum)
# print(total_exam_score)
# print(max(student_scores))

# using the for loop with python lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits) # in the loop
print(fruits) # after the loop

