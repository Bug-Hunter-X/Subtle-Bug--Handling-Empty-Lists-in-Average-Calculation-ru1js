def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

try:
    my_empty_list = []
    average_empty = calculate_average(my_empty_list)
    print(f"The average of an empty list is: {average_empty}")
except ValueError as e:
    print(f"Error: {e}")
