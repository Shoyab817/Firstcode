print("=== Number Repeat Magic ===")

# Ask for input
number = input("Enter a 2-digit number: ")

# Check if input is exactly 2 digits
if number.isdigit() and len(number) == 2:

    # Convert string to integer
    number = int(number)

    # Multiply
    result = number * 10101

    # Show output
    print("Magic Result:", result)

else:
    print("Please enter exactly 2 digits.")