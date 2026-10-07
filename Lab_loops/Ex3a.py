# Write Python code that executes a for loop that examines every element of the tuple (“hello,” 10; “goodbye,” 3; “goodnight,” 5). Within the loop, use an if statement to count how many of the elements are strings. After the loop completes, print out a message stating how many strings are in the tuple.
# Define the tuple
my_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Initialize the counter
string_count = 0

# Iterate through the tuple
for element in my_tuple:
    if isinstance(element, str):
        string_count += 1

# Print the result
print(f"There are {string_count} strings in the tuple.")
