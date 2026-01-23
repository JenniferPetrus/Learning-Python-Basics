# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake, there is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("It's a room full of fire . Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

# logical operators: and, or, not
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Ticket is $7.")
    elif age >= 45 and age <= 55: # <= 45 age <= 55
        print("Free ride")
    else:
        bill = 12
        print("Ticket is $12.")
    wants_photo = input("Do you want to have a photo taken? y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3 # bill = bill + 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

# pizza order practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("You typed the wrong inputs.")
    if pepperoni == "Y":
        if size == "S":
            price += 2
        else:
            price += 3
    else:
        print(price)
    if extra_cheese == "Y":
        price += 1
print(f"Your final price is ${price}")

# multiple if statements in succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Ticket is $7.")
    else:
        bill = 12
        print("Ticket is $12.")
    wants_photo = input("Do you want to have a photo taken? y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3 # bill = bill + 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
    
# if and elif statements: nested if / else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Ticket is $5.")
    elif age <= 18:
        print("Ticket is $7.")
    else:
        print("Ticket is $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Modulo operator: %
# 10 % 3 = 1
number = int(input("What number you want to check?"))
if number % 2 == 0:
    print("Even number")
else:
    print("Not even")

# if / else and conditional operators: ==, <=, >=, <, >, !=
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")