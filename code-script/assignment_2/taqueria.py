def main():
    # Menu dictionary with item names and prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0  # variable to store the running total

    while True:
        try:
            # Get item from user
            # .title() makes the input case-insensitive
            # Example: "taco" becomes "Taco", "BAJA TACO" becomes "Baja Taco"
            item = input("Item: ").title()


        except EOFError:
            break # Stop the loop when user sends EOF (Ctrl+D)


        # If item exists in menu, add its price to total
        if item in menu:
            total += menu[item]


            # Print total formatted with 2 decimal places
            print(f"Total: ${total:.2f}")


main()
