import random

Reqs = list(range(1, 10))

# choose a random requirement from the list
R1 = random.choice(Reqs)
# remove the chosen requirement from the list
Reqs.remove(R1)
R2 = random.choice(Reqs)

print(f"Requirement 1: {R1}")
print(f"Requirement 2: {R2}")
