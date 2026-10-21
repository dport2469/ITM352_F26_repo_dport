def get_numbers(student_id, N=10):
	digits = [int(digit) for digit in student_id]
	first_num = sum(digits) % N + 1

	nonzero_product = 1
	for digit in digits:
		if digit != 0:
			nonzero_product *= digit

	second_num = nonzero_product % N + 1
	while first_num == second_num:
		second_num = (second_num % N) + 1

	return first_num, second_num


student_id = input("Enter your 8-digit student ID: ")
first_num, second_num = get_numbers(student_id)
print(first_num, second_num)
