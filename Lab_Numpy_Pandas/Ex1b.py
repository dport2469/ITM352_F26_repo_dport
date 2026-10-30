import numpy as np

percentile_income_list = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]

percentile_income_array = np.array(percentile_income_list)
print("Dimensions of the array:", percentile_income_array.shape)
print("Number of elements in the array:", percentile_income_array.size)

# Print out the table of percentiles and household incomes
print("Percentile\tIncome")
for percentile, income in percentile_income_array:
    print(f"{percentile}\t{income}")