def your_vat():
    while True:
        try:
            price = float(input("Enter the price of the item: "))
            vat = float(input("Enter the VAT percentage: "))

            if price < 0 or vat < 0:
                print("Please enter a valid number")
            else:
                vat_amount = price * (vat / 100)
                return price + vat_amount
        except (ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            print("Please enter a valid number")


# Example usage
price_with_vat = your_vat()
print("VAT-inclusive price:", price_with_vat)
