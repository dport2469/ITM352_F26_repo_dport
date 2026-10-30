import pandas as pd
import numpy as np

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]



# Use zip() to create a list of (age, gender) tuples.
age_gender_list = list(zip(ages, gender))


df = pd.DataFrame(age_gender_list, index=names, columns=["Age", "Gender"])

# Calculate and print out the average age by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()
print(df.groupby("Gender")["Age"])
print(average_age_by_gender)    