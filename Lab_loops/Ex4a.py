recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50
total_spent = 0

for expense in recent_purchases:
    if expense + total_spent > budget:
        print(f"This purchase of ${expense:.2f} is over budget! total_spent: ${total_spent:.2f}")
    else:
        total_spent += expense
        print(f"This purchase of ${expense:.2f} is within budget total_spent: ${total_spent:.2f}")
        