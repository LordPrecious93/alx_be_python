# pattern_drawing.py

# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate that the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks for the current row
        for _ in range(size):
            print("*", end="")
        # Move to the next line after printing one row
        print()
        row += 1

