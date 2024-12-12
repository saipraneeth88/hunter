# 1.b) Develop a program to read the name and year of birth of a person. Display whether the person is a senior citizen or not.

from datetime import datetime

def input_person_details():
    name = input("Enter the person's name: ")
    year_of_birth = int(input("Enter the year of birth: "))
    return name, year_of_birth

def is_senior_citizen(year_of_birth):
    current_year = datetime.now().year
    age = current_year - year_of_birth
    return age #>= 60

def display_result(name, age):
    print("\n--- Result ---")
    if age >= 60:#is_senior:
        print(f"{name} is a senior citizen.")
    else:
        print(f"{name} is not a senior citizen.")

name, year_of_birth = input_person_details()

#is_senior
age = is_senior_citizen(year_of_birth)

display_result(name, age )#is_senior)