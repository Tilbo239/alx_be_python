# from arithmetic_operations import perform_operation
from shopping_list_manager import display_menu, add_item, remove_item, view_list


def main():
    # print("Arithmetic Operations")
    # num1 = float(input("Enter the first number: "))
    # num2 = float(input("Enter the second number: "))
    # operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # result = perform_operation(num1, num2, operation)
    # print(f"Result: {result}")
    
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter  your choice: ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please  try again.")


if __name__ == "__main__":
    main()