age = 70
weekday = "Tuesday"
matinee = True

price = 14

if age >= 65 and price > 8:
	price = 8

if weekday == "Tuesday" and price > 10:
	price = 10

if matinee:
	matinee_price = 5 if age >= 65 else 8
	if price > matinee_price:
		price = matinee_price

print("Age:", age)
print("Weekday:", weekday)
print("Matinee:", matinee)
print("Price: $", price, sep="")
