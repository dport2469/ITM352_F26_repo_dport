'''
Write Python code that uses the input built-in function to ask the user to enter a whole number between 1 and 100.
 Square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered. Make sure you correctly handle the data types in the expressions to get the expected results.
'''

number = input("Please enter a whole number between 1 and 100: ")
square = int(number) ** 2
print("You entered " + number +", and its square is " + str(square) + ".")