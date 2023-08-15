from datetime import datetime
from tabulate import tabulate


def customer_name():
    while True:
        name = str(input("Enter your name: "))
        has_lower = any(a.islower() for a in name)
        is_valid = len(name) >= 2 and has_lower

        if is_valid:
            return name
        errors = []
        if not has_lower:
            errors.append("Name should have at least one lowercase letter.")
        if len(name) < 2:
            errors.append("Name should have at least 3 characters.")
        print("Invalid name. Please fix the following errors:")
        for error in errors:
            print(f"- {error}")


Name = customer_name()
print("Customer Name: ", Name)


def user_purchase():
    purchases = []
    while True:
        purchase = input("Enter the item you want to purchase: ")
        quantity = input("Enter the quantity: ")
        price = input("Enter the price per unit: ")

        if not purchase.isalpha() or not quantity.isdigit() or not price.isdigit() or int(price) <= 0:
            print("Invalid input, try again.")
            continue

        purchases.append((purchase, int(quantity), int(price)))

        done = input("Are you done? (y/n): ")
        if done.lower() == 'y':
            break

    return purchases


purchases = user_purchase()

table_data = []
total = 0
for purchase in purchases:
    item = purchase[0]
    quantity = purchase[1]
    price = purchase[2]
    subtotal = quantity * price
    total += subtotal
    table_data.append([item, quantity, price, subtotal])

print(tabulate(table_data, headers=["Item", "Quantity", "Price", "Subtotal"], tablefmt="grid"))
print("Total: ", total)


def cashier_name():
    Cashier_name = input("Please enter your cashier name: ")
    has_lower = any(a.islower() for a in Cashier_name)
    is_valid = len(Cashier_name) >= 2 and has_lower

    if is_valid:
        return Cashier_name
    errors = []
    if not has_lower:
        errors.append("Name should have at least one lowercase letter.")
    if len(Cashier_name) < 2:
        errors.append("Name should have at least 3 characters.")
    print("Invalid name. Please fix the following errors:")
    for error in errors:
        print(f"- {error}")


C_name = cashier_name()


def discount():
    return input('How much discount will the customer get?: ')


print(discount())

print(" ", end="\n")
print('''SEMICOLON STORES
MAIN BRANCH
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS
TEL: 07047218991''')
date = datetime.now()
formatted_date = date.strftime("%Y-%m-%d %I:%M:%S %p")
print(formatted_date)
print("Customer Name: ", Name)
print("Cashier Name: ", C_name)
