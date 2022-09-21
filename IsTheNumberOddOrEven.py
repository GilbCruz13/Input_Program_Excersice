#Ask the user for a number. Depending on whether the 
#number is even or odd, print out an appropriate message to the user.
def x (inputNumber):
    inputNumber =int(input("Enter a number: "))
    if inputNumber % 2 == 0:   
        print("Your number is Even")
    elif inputNumber % 2 == 1: 
        print("Your number is Odd")
    return x

print(x(""))
#Even number will return 0 residuals
#Odd numbers will retrun 1 residuals 

