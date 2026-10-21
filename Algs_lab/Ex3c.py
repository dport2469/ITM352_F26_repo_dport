'''
Step 1: Generate a list of all pairs of numbers 1 … N
Step 2: Shuffle the list of pairs (randomize the order)
Step 3: Given an 8-digit StudentID, assign the pair with index  (student_id - 10000000) % len(pairs)

'''

# Generate a list of all pairs of numbers 1 … N
N = 10
pairs = [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)]

# Shuffle the list of pairs (randomize the order)
import random


# Given an 8-digit StudentID, assign the pair with index  (student_id - 10000000) % len(pairs)  
student_id = input("Enter your 8-digit student ID: ")
# swet the seed for reproducibility
random.seed(int(student_id))
random.shuffle(pairs)
assigned_pair = pairs[0]
print(f"Assigned pair: {assigned_pair}")