durations = [1.1, 0.8, 2.5, 2.6]
costs = ("$6.25", "$5.25", "$10.50", "$8.05")
 
trip_dict = dict(zip(durations, costs))
print(trip_dict)

print(f"The 3rd trip duration: {durations[2]} and cost: {trip_dict[durations[2]]}")