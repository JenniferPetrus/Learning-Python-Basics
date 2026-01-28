# Love Calculator
def calculate_love_score(name1, name2):
    combine_names = name1 + name2
    lower_names = combine_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Jenny", "Timo")


# Keyword Arguments = my_function(a = 1, b = 2, c = 3)

# def my_function(a, b, c):
  # do this with a
  # then do this with b
  # finally do this with c

# Functions with more than 1 input
def greet_with(name = "Jenny", location = "Nowhere"):
  print(f"Heyy {name}, how is it in {location}?")
  
greet_with("Jenny", "Nowhere")
greet_with("Nowhere", "Jenny")
greet_with( location = "Nowhere", name = "Jenny") # now I can switch around the arguments