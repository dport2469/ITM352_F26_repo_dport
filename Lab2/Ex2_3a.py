''' 
Write Python code that uses the input built-in function to ask the user to enter a decimal formatted number between 1 and 100.
'''

number = float(input("Please enter a decimal formatted number between 1 and 100: "))

#  Square the number that the user entered using the exponentiation operator.
squared = number ** 2

# Alternative: multiplication avoids the overhead of a general power algorithm, so it's faster for squaring.
squared_mult = number * number

print("The square of " + str(number) + " is " + str(squared) + ".")
