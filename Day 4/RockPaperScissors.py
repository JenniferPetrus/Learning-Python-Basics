import random
import my_module

# Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print (scissor)
else:
    print("Wrong number")
    
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
    if player == 0:
        print("It's a draw")
    elif player == 1:
        print("You win")
    elif player == 2:
        print("You lose")
    else:
        print("Wrong number")
elif computer == 1:
    print(paper)
    if player == 0:
        print("You lose")
    elif player == 1:
        print("It's a draw")
    elif player == 2:
        print("You win")
    else:
        print("Wrong number")
elif computer == 2:
    print (scissor)
    if player == 0:
        print("You win")
    elif player == 1:
        print("You lose")
    elif player == 2:
        print("It's a draw")
    else:
        print("Wrong number")
else:
    print("Wrong number")


# list and indexError
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][2]) # [0] = fruits, [1] = vegetables THEN in [1](vegetables) the item with index 2 = Tomatoes
print(dirty_dozen[1][3])

fruits = ["Strawberries", "Apples"]
vegetables = ["Spinach", "Kale"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1. Option
print(random.choice(friends))
# 2. Option
random_index = random.randint(0, 4)
print(friends[random_index])

# list
# fruits = [item1, itwem2]
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "Ohio"
]
print(states_of_america[0]) # first item
states_of_america[1] = "Pencilvania" # change item
states_of_america.append("Jennyland") # add item
states_of_america.extend(["State1", "State2"]) # add items of another list
states_of_america.remove("State2") # remove item
print(states_of_america)

# Heads or Tails
heads_or_tails = random.randint(0, 1)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

# randomisation and python lists
random_integer = random.randint(1, 10) # random number between 1 and 10
print(random_integer)

print(my_module.my_favourite_number)