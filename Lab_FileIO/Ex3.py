# Read the 1,000 lines of taxi data from the taxi_1000.csv file and calculate the total of all fares, the average of those fares, and the maximum trip distance (based on the Trip Miles field).
import csv
import os
from pathlib import Path

csv_path = Path(__file__).with_name("taxi_1000.csv")

if csv_path.is_file() and os.access(csv_path, os.R_OK):
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        taxis = csv.DictReader(csv_file)
        fares = [
            float(row["Fare"].replace("$", "").replace(",", ""))
            for row in taxis
            if row["Fare"]
        ]
        trip_miles = [
            float(row["Trip_Miles"].replace(",", ""))
            for row in taxis
            if row["Trip_Miles"]
        ]

    total_fares = sum(row["Fare"])
    average_fares = total_fares / len(fares)
    maximum_trip_distance = max(trip_miles)

    print(f"Total Fares: ${total_fares:,.2f}")
    print(f"Average Fares: ${average_fares:,.2f}")
    print(f"Maximum Trip Distance: {maximum_trip_distance:,.2f} miles")
else:
    print(f"Cannot read file: {csv_path}")