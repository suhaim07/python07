numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = sorted(set(numbers))

if len(unique_numbers) < 2:
    print("The list must contain at least two distinct numbers.")
else:
    print("Second largest number:", unique_numbers[-2])
