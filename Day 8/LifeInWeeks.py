# Life in weeks
end_of_age = 90
years_left = ''


def life_in_weeks(current_age):
    years_left = end_of_age - current_age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(20)

# Function that allows for input
name = "Jenny" # Parameter (name) = Argument ("Jenny")

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name(name)
greet_with_name("name")

# def function():
  # do this
  # then do this
  # finally do this
def greet():
  print("Hello")
  print("How are you?")
  print("Bye")
  
greet()
