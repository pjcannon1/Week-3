
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.



# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.



# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

# Problem 1

def process_numbers(numbers):
    if not numbers:
        print("The list is empty. Please provide valid numbers.")
        return

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    largest = max(numbers)

    print(f"Sum: {total_sum}")
    print(f"Average: {average:.2f}")
    print(f"Largest Number: {largest}")


def get_user_numbers():
    while True:
        user_input = input("Enter numbers separated by spaces: ").strip()
        
        if not user_input:
            print("Error: No input provided. Please enter at least one number.")
            continue  # Ask again

        try:
            numbers_list = [float(num) for num in user_input.split()]
            if not numbers_list:
                raise ValueError  # Ensure at least one number is entered
            return numbers_list
        except ValueError:
            print("Error: Please enter only numbers separated by spaces.")


numbers_list = get_user_numbers()


process_numbers(numbers_list)
