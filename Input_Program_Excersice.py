#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
#tells them the year that they will turn 100 years old

type_name = input("Enter Your Name: ")
type_age = int(input("How old are you: "))

def x (name, year):
    name = type_name
    year = type_age
    years =  2022 - year + 100
    return f"Your name is {name}, you will turn 100 years of age on the year {years}. " 

print(x("",''))