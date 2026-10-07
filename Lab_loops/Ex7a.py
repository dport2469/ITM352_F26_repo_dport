# Write code that will iterate through numbers from 1 to 10 and print the number if it is not equal to 5 (using continue) and stop the loop entirely and print a message when it reaches 8 (using break).
i = 1
while True:
    i += 1
    if i == 5:
        continue
    elif i == 8:
        print("Reached 8, stopping the loop.")
        break
    print(i)
