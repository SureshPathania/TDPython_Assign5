# Task 1 of Assignment 5 - Create a Dictionary of Student Marks

dict_student = { "Arun":85, "Balraj":90, "Vishal":65, "Chetan":78, "Rajan":65, "Varun":91}

name = input("Enter the student's name: ")      #accepting user input
for std in dict_student:    # iterating dict
    if name == std:         # check for name match
        print(f"{std}\'s marks: {dict_student[std]}")
        print("Bye!!!")
        exit()
print(f"Student \'{name}\' not found.")
print("Bye!!!")

# end of program