
even_numbers = [2]
num = 3 
while even_numbers[-1] < 50:
    if num % 2 == 0:
        even_numbers.append(num)
    num += 1
print(even_numbers)