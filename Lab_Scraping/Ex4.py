import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)
results = client.get("rr23-ymwb", limit=500)

df = pd.DataFrame.from_records(results)
print(df.head())
print(df.columns)
print(df[['public_vehicle_number', 'vehicle_fuel_source']])
# Group the vehicles by fuel type and output the number of vehicles per fuel source
print(df.groupby('vehicle_fuel_source').size())