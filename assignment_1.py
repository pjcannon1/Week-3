'''
Welcome to Week 3!

This script demonstrates conditionals and loops in Python.

Play around with the values to explore different outputs!
'''

# Function using a "for" loop
def loop_function(x):
    """Loops from 0 to x-1, checking if each number is even or odd."""
    
    for i in range(x):
        if i % 2 == 0:
            print(f"{i} is even!")
        else:
            print(f"{i} is odd!")

    print("For loop finished!")

# Function using a "while" loop
def while_loop_function(x):
    """Uses a while loop to count down from x to 0."""
    
    while x > 0:
        print(f"Countdown: {x}")
        x -= 1  # Decrement x by 1
    
    print("While loop finished!")

# Get user input
try:
    number_of_loops = int(input("Enter a number: "))  # Convert input to integer
    
    # Call both functions
    loop_function(number_of_loops)
    while_loop_function(number_of_loops)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
