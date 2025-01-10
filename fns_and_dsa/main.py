# from arithmetic_operations import perform_operation
# from shopping_list_manager import display_menu, add_item, remove_item, view_list, shopping_list
# from explore_datetime import display_current_datetime, calculate_future_date
from temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit

def main():
    # print("Arithmetic Operations")
    # num1 = float(input("Enter the first number: "))
    # num2 = float(input("Enter the second number: "))
    # operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # result = perform_operation(num1, num2, operation)
    # print(f"Result: {result}")
    
    
    # while True:
    #     display_menu()
    #     choice = input("Enter  your choice: ")

    #     if choice == '1':
    #         add_item(shopping_list)
    #     elif choice == '2':
    #         remove_item(shopping_list)
    #     elif choice == '3':
    #         view_list(shopping_list)
    #     elif choice == '4':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please  try again.")

    # display_current_datetime()
    # calculate_future_date()

    

    temperature = float(input("Enter the temperature to convert:").strip())

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower().upper()

    if unit == 'F':
        
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equivalent to {result}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equivalent to {result}°F.")
    else:
        print("Invalid choice. Please enter 1 or 2.")



if __name__ == "__main__":
    main()