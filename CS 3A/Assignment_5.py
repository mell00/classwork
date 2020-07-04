"""
Assignment #5 by
    Madison Ell
    7/8/2020
    A program that asks the user for their name and returns a
    greeting, generates foreign currency exchange values,
    prints the options of a main menu, then asks the user
    for their selection and returns an appropriate message.

"""


home_currency = ""


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
    home_curr_input = True
    while home_curr_input:
        home_currency = input("What is your home currency? ")
        try:
            conversions[home_currency]
        except KeyError:
            continue
        home_curr_input = False
        break

    currency_options(home_currency)
    is_running = True
    while is_running:
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
                is_running = False
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


def currency_options(base_curr="EUR"):
    print(f"Options for converting from {base_curr}:")
    for curr in conversions:
        print(f"{curr:<6}", end=" ")
    for i in range(10, 100, 10):
        print("\n")
        for curr in conversions:
            convert_output = currency_converter(i, base_curr, curr)
            print(f"{convert_output:<6.2f}", end=" ")
    print("\n")


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
    main()


r"""
--- Sample Run #1 ---
Please enter your name: Madison
Hello Madison, nice to meet you!
What is your home currency? USD
Options for converting from USD:
USD    EUR    CAD    GBP    CHF    NZD    AUD    JPY

10.00  9.00   14.00  8.00   9.50   16.60  16.20  1079.20

20.00  18.00  28.00  16.00  19.00  33.20  32.40  2158.40

30.00  27.00  42.00  24.00  28.50  49.80  48.60  3237.60

40.00  36.00  56.00  32.00  38.00  66.40  64.80  4316.80

50.00  45.00  70.00  40.00  47.50  83.00  81.00  5396.00

60.00  54.00  84.00  48.00  57.00  99.60  97.20  6475.20

70.00  63.00  98.00  56.00  66.50  116.20 113.40 7554.40

80.00  72.00  112.00 64.00  76.00  132.80 129.60 8633.60

90.00  81.00  126.00 72.00  85.50  149.40 145.80 9712.80

Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 9
Goodbye!
"""

r"""
--- Sample Run #2 ---
Hello Madison, nice to meet you!
What is your home currency? JPY
Options for converting from JPY:
USD    EUR    CAD    GBP    CHF    NZD    AUD    JPY

0.09   0.08   0.13   0.07   0.09   0.15   0.15   10.00

0.19   0.17   0.26   0.15   0.18   0.31   0.30   20.00

0.28   0.25   0.39   0.22   0.26   0.46   0.45   30.00

0.37   0.33   0.52   0.30   0.35   0.62   0.60   40.00

0.46   0.42   0.65   0.37   0.44   0.77   0.75   50.00

0.56   0.50   0.78   0.44   0.53   0.92   0.90   60.00

0.65   0.58   0.91   0.52   0.62   1.08   1.05   70.00

0.74   0.67   1.04   0.59   0.70   1.23   1.20   80.00

0.83   0.75   1.17   0.67   0.79   1.38   1.35   90.00

Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 9
Goodbye!
"""
