# Create a list
my_list = [10, 11, 12, 13, 14, 15, 16, 171]

# Use the list comprehension method to get sort out only odd numbers in the list
# List comprehension is used to filter out only the odd numbers from the list
# List comprehension checks if ('if i % 2 == 1') checks if the element 'i' is an odd number (i.e., has a remainder of 1 when divided by 2).
odd_numbers = [i for i in my_list if i % 2 == 1]

# Initialize a variable to take the value of the highest odd number
highest_odd = None

# Iterate through the 'odd_numbers' list to find the highest odd number
for i in odd_numbers:
    # Check if 'highest_odd' is None (i.e., no odd number has been found yet) or if the current element 'i' is greater than the current highest_odd.
    if highest_odd is None or i > highest_odd:
        # If it is correct, update 'highest_odd' to the current element 'i'.
        highest_odd = i

# Print the highest odd number in the list
print(highest_odd)
