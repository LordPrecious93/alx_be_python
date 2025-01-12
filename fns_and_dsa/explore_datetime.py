from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time in a readable format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    """Calculates and displays a future date based on user input."""
    try:
        # Prompt the user to enter the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_date = datetime.now()
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Print the future date in a readable format
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def main():
    """Main function to call the required functionalities."""
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()

