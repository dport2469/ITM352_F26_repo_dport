# Using the .read() method, read the names from the names.txt file and print out the names as well as a count of how many names there are altogether. 

with open('./names.txt', 'r') as file:
    # Display the data type returned from open()
    print(type(file))
    # Read the contents of the file
    contents = file.read()
    # Split the contents into a list of names
    names = contents.split('\n')
    # Remove any empty strings from the list
    names = [name for name in names if name]
    # Print each name
    for name in names:
        print(name)
    # Print the count of names
    print(f"Total number of names: {len(names)}")

