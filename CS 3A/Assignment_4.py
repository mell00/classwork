"""
Assignment #4 by
    Madison Ell
    7/8/2020
    A program that asks the user for their name and returns a
    greeting. Program accepts home currency, desired currency,
    and quantity of home currency, then converts to quantity
    of desired currency. Includes unit testing for currency
    conversion feature. Program prints the options of a
    main menu, then asks the user for their selection and
    returns an appropriate message.

"""


conversions = {
    "USD": 1,
    "EUR": 0.9,
    "CAD": 1.4,
    "GBP": 0.8,
    "CHF": 0.95,
    "NZD": 1.66,
    "AUD": 1.62,
    "JPY": 107.92
}


def main():
    """Obtain the user's name."""
    my_name = input("Please enter your name: ")
    print("Hello " + my_name + ", nice to meet you!")
    menu()


def print_menu():
    """Print the main menu options."""
    print("Main Menu")
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu():
    """Obtain the user's input, filter numeric values
    between 1 and 9, and print appropriate message."""
    while True:
        print_menu()
        user_input = input("What is your choice? ")
        try:
            choice_num = int(user_input)
        except ValueError:
            print("Please enter a numeric value.")
            continue
        if (choice_num >= 1 and choice_num <= 9):
            not_implemented = " functionality is not implemented yet."
            if choice_num == 1:
                print("Average rent" + not_implemented)
            if choice_num == 2:
                print("Minimum rent" + not_implemented)
            if choice_num == 3:
                print("Maximum rent" + not_implemented)
            if choice_num == 4:
                print("Location" + not_implemented)
            if choice_num == 5:
                print("Property type" + not_implemented)
            if choice_num == 6:
                print("Location filter" + not_implemented)
            if choice_num == 7:
                print("Property type filter" + not_implemented)
            if choice_num == 8:
                print("Data loading" + not_implemented)
            if choice_num == 9:
                print("Goodbye!")
                break
        else:
            print("Please enter a value between 1 and 9.")
        continue


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """Calculate value of money converted from one currency to another."""
    if quantity == 0:
        raise ValueError
    else:
        exch_rate = conversions[target_curr] / conversions[source_curr]
        targ_quantity = quantity * exch_rate
    return targ_quantity


def unit_test():
    """Conduct unit testing for currency conversion results."""
    # User enters invalid source currency should raise KeyError
    try:
        currency_converter(1, "cat", "USD")
        print("FAIL: Source Currency Does Not Raise KeyError")
    except KeyError:
        print("PASS: Invalid Source Currency Raises KeyError")
    # User enters invalid target currency should raise KeyError
    try:
        currency_converter(1, "USD", "cat")
        print("FAIL: Target Currency Does Not Raise KeyError")
    except KeyError:
        print("PASS: Invalid Target Currency Raises KeyError")
    # User enters zero for quantity should raise ValueError
    try:
        currency_converter(0, "EUR", "USD")
        print("FAIL: Quantity Does Not Raise ValueError")
    except ValueError:
        print("PASS: Zero Quantity Raises ValueError")
    # Conversion from USD to another currency with quantity > 1
    if currency_converter(1.2, "USD", "EUR") == 1.08:
        print("PASS: Conversion from USD to EUR")
    else:
        print("FAIL: Conversion from USD to EUR")
    # Conversion from another currency to USD with quantity > 1
    if currency_converter(2.8, "CAD", "USD") == 2:
        print("PASS: Conversion from CAD to USD")
    else:
        print("FAIL: Conversion from CAD to USD")
    # Conversion between two currencies other than USD with quantity > 1
    if currency_converter(5.6, "CAD", "EUR") == 3.6:
        print("PASS: Conversion from CAD to EUR")
    else:
        print("FAIL: Conversion from CAD to EUR")


if __name__ == "__main__":
    unit_test()


r"""
--- Sample Run ---
PASS: Invalid Source Currency Raises KeyError
PASS: Invalid Target Currency Raises KeyError
PASS: Zero Quantity Raises ValueError
PASS: Conversion from USD to EUR
PASS: Conversion from CAD to USD
PASS: Conversion from CAD to EUR
"""
