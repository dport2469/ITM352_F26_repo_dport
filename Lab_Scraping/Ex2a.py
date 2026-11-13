
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603" 


# Use .read_html() to extract the interest rate table information as a DataFrame and print out its columns. 
df = pd.read_html(url)[0]
print(df.columns)
# Use .iterrows() to loop through the the rows and print out the 1 month interest rates
for index, row in df.iterrows():
    print(row['1 Mo'])