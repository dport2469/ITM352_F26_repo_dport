# Read the json file of taxi trip data at  https://drive.google.com/file/d/1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus/view?usp=sharing and create a dataframe from it. Print summary statistics about the dataframe, as well as the median.
import pandas as pd

taxi_trip_URI = "https://drive.google.com/uc?export=download&id=1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus"


# Read the JSON file of taxi trip data
df = pd.read_json(taxi_trip_URI)

print(df.head())
# Print summary statistics about the dataframe
print(df.describe())

print(df['fare'].median()) 