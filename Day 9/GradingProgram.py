# Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary
for student in student_scores:

    #Get the value (student score) by using the key each time.
    score = student_scores[student]

    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'


programming_dictionary = {
  'Bug': 'An error prevents the program ...',
  'Function': 'A piece of code that you ...',
  'Loop': 'The action of doing ...'
}

# list[0]
print(programming_dictionary['Bug']) # the key is 'Bug'

# adding a new value
programming_dictionary['NewKey'] = 'This is the Value'
print(programming_dictionary)

empty_dictionary = {}
# then adding new keys and values with empty_dictionary = ['KEY'] = 'VALUE'

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary['Bug'] = 'A new text for Bug'
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])