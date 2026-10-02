# Add an assertion that will cause the program to terminate and raise an exception if the temperature is below absolute zero (-273.15C).

def celsius_to_fahrenheit(celsius):
    assert celsius >= -273.15, "Temperature cannot be below absolute zero"
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))  # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(-273.15))  # -459.67
print(celsius_to_fahrenheit(-274))  # This will raise an AssertionError   
