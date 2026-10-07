# Write Python code that uses the Python while statement to create a list of elements that are even numbers from 1 to 50.
even_numbers = []
num = 1 
while num <= 50:
    if num % 2 == 0:
        even_numbers.append(num)
    num += 1
print(even_numbers)