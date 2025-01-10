shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the card.")
    else:
        print("Invalid input. Please enter a valid item.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()

    if item not in shopping_list:
        print(f"{item} is not in the shopping list")
    else:
        shopping_list.remove(item)
        print(f"{item} has been removed from the  list shopping")


def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        for item in shopping_list:
            print(item)
    