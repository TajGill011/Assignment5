#Sartaj Gill 10/02/2022

#Revision Number 1 10/02/2022
fname = input("Please enter your first name(In all lowercase letters): ") #Stores the user input for first name as a variable

#Revision Number 2 10/02/2022
lname = input("Please enter your last name(In all uppercase letters): ") #Stores the user input for the last name as a variable

#Revision Number 3 10/02/2022
print("Hello,", fname.upper(), lname.lower()) #Prints out a string which converts the first name input for the user to all uppercase and the last name input for the user to all lowercase

#Revision Number 4 10/02/2022
print("\n\n")#Prints out two new lines

#Revision Number 5 10/03/2022
flname = (fname.upper() + " " + lname.lower()) #Created a new variable named fl name that stores the user input for first and last name together 
print(flname) #Prints the variable

#Revision Number 6 10/03/2022
print(flname[slice(7,11)]) #Prints out the last name from the variable we just created using slice

#Revision Number 7 10/03/2022
print(flname.replace(f"{lname.lower()}", f"{lname.lower()}" + ", Walsh College Student")) #Replaces the last name in the variable flname with lname, Walsh College Student

#Revision Number 8 10/03/2022
print('"Start by doing what\'s necessary; then do what\'s possible;\n and suddenly you are doing the impossible - Francis of\n Assisi"') #Prints the statement provided

#Revision Number 9 10/03/2022
decone = float(3.75) #Stores a decimal number as a variable
dectwo = float(12.56)

#Revision Number 10 10/03/2022
plus = "+" #Assigns the variable the value of a math operation
minus = "-"
multi = "*"
div = "/"

#Revision Number 11 10/03/2022
print(decone, plus, dectwo, "=", decone + dectwo) #Prints a statement using the first decimal variable plus the second decimal variable. Adding them
print(f"{decone} {minus} {dectwo} = {decone - dectwo}")#Prints a statement subtracting the first decimal variable with the second decimal variable
multi_string = (f"{decone} {multi} {dectwo} = {decone * dectwo}") #creates variable storing all information 
print(multi_string) #Printst the variable
print(decone, div, dectwo, "=", decone / dectwo)

#Revision Number 12 10/03/2022
import math #imports the math library

sq_root = math.sqrt(decone * dectwo) #Assigns the square root value of decone * dectwo to the variable sq_root
sq_root = str(round(sq_root,2)) #Rounds the variable to 2 decimal places
print("The sqare root of", {decone * dectwo}, "=", sq_root) #Prints out the statement

#Revision Number 13 10/03/2022
month = input("Enter the current month: ")
month = str(month) #Stores user input as a integer
day = input("Enter the day of the month: ")
day = int(day) #Converts the user input into a integer value

#Revision Number 14 10/03/2022
print(f"\n\t\tToday is the day {day} of the month of {month}") #Prints the statement

#Final Date 10/03/2022
#End Sartaj Gill
