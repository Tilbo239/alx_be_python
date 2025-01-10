from datetime import datetime,  timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(formatted_date)

def calculate_future_date():
    number_of_days = input("Enter the number of days to add to the current date: ")

    if number_of_days.isdigit():
        number_of_days = int(number_of_days)
        current_date =  datetime.now()
        future_date = current_date + timedelta(days=number_of_days)

        formatted_future_date = future_date.strftime("%Y-%m-%d")

        print(f"Future Date (after {number_of_days} days): {formatted_future_date}")
    else:
        print("Invalid input. Please enter an integer value for the number of days.")

       