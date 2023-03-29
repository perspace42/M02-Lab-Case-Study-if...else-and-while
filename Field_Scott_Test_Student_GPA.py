'''
Author: Scott Field
Version: 1.00
Date: 3/28/2023
Program Name: Field_Scott_Test_Student_GPA
Program Purpose: Accept Student Names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll 
(program loops until 'ZZZ' is entered)
The program will;
- ask for and accept a student's last name.
- quit processing student records if the last name entered is 'ZZZ'.
- ask for and accept a student's first name.
- ask for and accept the student's GPA as a float.
- test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
- test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
Main Variable List:
- user_input (string) stores user input as a string
- first_name (string) stores students first name (taken from user_input)
- last_name (string) stores students last name (taken from user_input)
- gpa (float) stores students GPA (taken from user_input)
- input_validated (boolean) stores whether or not float input is correct
- welcome_message (string) stores the welcome message for the program
- deans_list_gpa (float) stores the GPA value required to be on the deans list
- honor_roll_gpa (float) stores the GPA value required to be on the honor roll
''' 

#Function To Determine If Program Should Exit
def exit(input_string):
    #Program Should Exit If the Input String is ZZZ
    if (input_string == 'ZZZ'):
        return True
    #Otherwise The Program Should Continue
    else:
        return False
    
#Function To Determine If Input Is A Valid Name (this wansn't required by program directions, I just wanted to add more program functionality)
def isName(input_string):
    #convert string to be tested to lowercase
    lower_string = input_string.lower()
    #have a string of accepted characters to test against
    letters = "abcdefghijklmnopqrstuvwxyz"
    #A name cannot be empty, if it is output the error.
    if (input_string == ""):
        print("Error, a name cannot be empty. (This loop will continue until a valid name is entered)")
        return False
    #A name must only consist of numeric characters
    else:
        #Iterate across string, test if it only consists of approved characters (letters)
        for index in range(len(input_string)):
            #If the character is not an aprroved character, output the error
            if (lower_string[index] not in letters):
                print("Error,", input_string[index], "is not a letter a name can only consist of letters. (This loop will continue until a valid name is entered)")
                return False
    
    #Otherwise input is valid, return True
    return True

    
#Intialization
welcome_message = "Enter a student's first name, last name, and GPA to see if that student has made the Dean's List or Honor Roll, or enter 'ZZZ' to exit"
user_input = ""
first_name = ""
last_name = ""
gpa = 0.0
input_validated = False

dean_list_gpa = 3.5
honor_roll_gpa = 3.25

#Welcome Message
print(welcome_message)

#Input Loop
while (user_input != "ZZZ"):

    #Set Variables
    input_validated = False
    user_input = ""

    #Get student first name
    user_input = input("Please enter the student's first name or 'ZZZ' to exit.\n:")

    #If the input is not a valid name, ask the user for new input
    while (isName(user_input) == False):
        user_input = input("Please enter the student's first name or 'ZZZ' to exit.\n:")
    #If the user has entered 'ZZZ' exit the program.
    if exit(user_input):
        break

    #set first_name equal to the correct input
    first_name = user_input

    #Get student last name
    user_input = input("Please enter " + first_name + "'s" + " last name or 'ZZZ' to exit.\n:")

    #If the input is not a valid name, ask the user for new input
    while (isName(user_input) == False):
        user_input = input("Please enter the student's first name or 'ZZZ' to exit.\n:")
    #If the user has entered 'ZZZ' exit the program.
    if exit(user_input):
        break

    #Set last_name equal to correct input
    last_name = user_input

    #Get student GPA
    user_input = input("Please enter " + first_name + " " + last_name + "'s GPA or 'ZZZ' to exit.\n:")
    if exit(user_input):
        break

    #Convert GPA to float 

    #Input Validation Loop
    while (input_validated == False):
        #Try to convert gpa to a float (decimal)
        try:
            gpa = float(user_input)
        #If an error is raised output a message and ask the user for correct input
        except:
            print("Error GPA must be a number, (This loop will continue until a valid number is entered).")
            user_input = input("Please enter " + first_name + " " + last_name + "'s GPA or 'ZZZ' to exit.\n:")
            #if the user wants to exit the program, exit both loops
            if exit(user_input):
                #Set outer loop condition to false
                user_input = "ZZZ"
                #Exit inner loop
                break
        #If input is valid, exit the input validation loop
        else:
            input_validated = True


    #Output if student has made the Dean's List (If the student has made the dean's list then they have made the Honor Roll as Well)
    if (gpa >= dean_list_gpa):
        print(f"Congratulations {first_name} {last_name} has made the Honor Roll.")
        print(f"Congratulations {first_name} {last_name} has made the Dean's List.")

    #Output if student has made the Honor Roll
    elif (gpa >= honor_roll_gpa):
        print(f"Congratulations {first_name} {last_name} has made the Honor Roll.")

    
