'''
 Use the input() function to input three strings (a first name, a middle initial, and a last name). Concatenate these strings together with a space between each, storing the result in a new variable. Print out the concatenated string
'''
first_name = input("Enter the first name: ")   
middle_initial = input("Enter the middle initial: ")
last_name = input("Enter the last name: ")

print("The full name is: {} {} {}".format(first_name, middle_initial, last_name))