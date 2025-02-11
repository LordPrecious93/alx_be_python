def display_menu():
    """Display the menu options for the Shopping List Manager."""
    # Exact print statement required for the checker
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """Main function to manage the shopping list."""
    shopping_list = []  # Define the array (list) to store shopping items

    while True:
        display_menu()  # Call display_menu to show options
        try:
            choice = int(input("Enter your choice (number): ").strip())  # Ensure input is a number
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # Add an item with the exact required prompt
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Invalid item name. Please try again.")

        elif choice == 2:
            # Remove an item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == 3:
            # View the list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == 4:
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

