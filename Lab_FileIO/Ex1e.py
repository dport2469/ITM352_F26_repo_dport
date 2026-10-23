# Using the .readline() method, read the names from the names.txt file and print out the names as well as a count of how many names there are altogether. 
with open('./names.txt', 'a') as file:
    file.write('\nDan Port')
    
with open('./names.txt', 'r') as file:
    count = 0
    # readline() returns '' only at end of file (blank lines return '\n')
    line = file.readline()
    while line:
        name = line.strip()
        # Skip blank lines
        if name:
            print(name)
            count += 1
        line = file.readline()
    # Print the count of names
    print(f"Total number of names: {count}")

# add Dan Port to the end of the file and print the entire contents of the file.


with open('./names.txt', 'r') as file:
    contents = file.read()
    print("Entire contents of the file:")
    print(contents)
