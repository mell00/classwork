"""
Assignment #6 by
    Madison Ell
    7/18/2020
    A program that asks the user for their name and returns a
    greeting. Program accepts home currency, converts to equivalent
    quantities of foreign currencies, then prints a table with
    these values. Includes unit testing for header and
    currency conversion features. Program prints the options
    of a main menu, then asks the user for their selection
    and returns an appropriate message.

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

default_borough = ("Staten Island", "Brooklyn", "Bronx",
                   "Brooklyn", "Manhattan", "Manhattan",
                   "Brooklyn", "Manhattan", "Manhattan",
                   "Manhattan", "Manhattan", "Brooklyn",
                   "Queens", "Manhattan", "Brooklyn",
                   "Brooklyn", "Brooklyn", "Brooklyn")

default_type = ("Private room", "Private room", "Private room",
                "Entire home / apt", "Private room", "Entire home / apt",
                "Private room", "Entire home / apt", "Entire home / apt",
                "Entire home / apt", "Entire home / apt", "Private room",
                "Entire home / apt", "Private room", "Entire home / apt",
                "Entire home / apt", "Private room", "Private room")

default_rate = (70, 50, 40, 150, 125, 196, 110, 170, 165, 150, 100,
                65, 350, 99, 200, 150, 99, 120)


class EmptyDatasetError(Exception):
    pass


class DataSet:
    header_length = 30

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self._header = ""

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value: str):
        if type(value) == str and len(value) < self.header_length:
            self._header = value
        else:
            raise ValueError

    def _cross_table_statistics(self, descriptor_one: str, descriptor_two: str):
        raise EmptyDatasetError
        matching_rents = []
        for i in self._data:
            if i[0] == descriptor_one and i[1] == descriptor_two:
                matching_rents.append(i[2])
        if matching_rents == [""]:
            return tuple(None, None, None)
        else:
            avg_rent = sum(matching_rents) / len(matching_rents)
            return tuple(min(matching_rents), avg_rent, max(matching_rents))

    def _load_default_data(self):
        self._data = [default_borough, default_type, default_rate]


def main():
    """Obtain the user's name."""
    my_name = input("Please enter your name: ")
    print("Hello " + my_name + ", nice to meet you!")
    while True:
        header_name = str(input("Please enter a menu header: "))
        try:
            DataSet(header_name)
        except KeyError:
            print("Please enter a string less than 30 characters long.")
            continue
        break
    air_bnb = DataSet(header_name)
    menu(air_bnb)


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


def menu(dataset: DataSet):
    """Obtain the user's input, filter numeric values
    between 1 and 9, and print appropriate message."""
    while True:
        home_currency = input("What is your home currency? ")
        try:
            conversions[home_currency]
        except KeyError:
            continue
        break
    currency_options(home_currency)
    while True:
        print(dataset.header)
        print_menu()
        user_input = input("What is your choice? ")
        try:
            choice_num = int(user_input)
        except ValueError:
            print("Please enter a numeric value.")
            continue
        if 1 <= choice_num <= 9:
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


def currency_options(base_curr="EUR"):
    """Print table of foreign currency quantities equivalent to
    incremental home currency quantities."""
    print(f"Options for converting from {base_curr}:")
    for curr in conversions:
        print(f"{curr:<6}", end=" ")
    for i in range(10, 100, 10):
        print("\n")
        for curr in conversions:
            convert_output = currency_converter(i, base_curr, curr)
            print(f"{convert_output:<6.2f}", end=" ")
    print("\n")


def crosstable_unit_test():
    """Conduct unit testing for DataSet class cross-table method."""
    my_set = DataSet("")
    # User does not load data
    try:
        my_set._cross_table_statistics("", "")
        print("Method Raises EmptyDataSet Error: FAIL")
    except EmptyDatasetError:
        print("Method Raises EmptyDataSet Error: PASS")
    my_set._load_default_data()
    # User calls with match in Borough column but invalid Property Type
    if my_set._cross_table_statistics("Queens", "Hotel Room") == (None, None, None):
        print("Invalid Property Type Returns None Tuple: PASS")
    else:
        print("Invalid Property Type Returns None Tuple: FAIL")
    # User calls with invalid Borough but match in Property Type column
    if my_set._cross_table_statistics("Queensland", "Private room") == \
    (None, None, None):
        print("Invalid Borough Returns None Tuple: PASS")
    else:
        print("Invalid Borough Returns None Tuple: FAIL")
    # User calls valid Borough and Property Type columns, with no match
    if my_set._cross_table_statistics("Bronx", "Entire home / apt") == \
    (None, None, None):
        print("No Matching Rows Returns None Tuple: PASS")
    else:
        print("No Matching Rows Returns None Tuple: FAIL")
    # User calls valid Borough and Property Type columns, with 1 match
    if my_set._cross_table_statistics("Bronx", "Private room") == \
    ("Bronx", "Private room", 40):
        print("One Matching Row Returns Correct Tuple: PASS")
    else:
        print("One Matching Row Returns Correct Tuple: FAIL")
    # User calls valid Borough and Property Type columns, with 2+ matches
    if my_set._cross_table_statistics("Brooklyn", "Private room") == \
    ("Brooklyn", "Private room", 88.8):
        print("Multiple Matching Rows Returns Correct Tuple: PASS")
    else:
        print("Multiple Matching Rows Returns Correct Tuple: FAIL")


def dataset_unit_test():
    """Conduct unit testing for DataSet class header method."""
    # User does not provide a header argument
    if DataSet(""):
        print("Testing constructor with default parameter: PASS")
    else:
        print("Testing constructor with default parameter: FAIL")
    # User provides a valid header argument
    try:
        DataSet("valid argument")
        print("Testing constructor with valid header argument: PASS")
    except ValueError:
        print("Testing constructor with valid header argument: FAIL")
    # User provides an invalid header argument
    try:
        DataSet(32)
        print("Testing constructor with invalid header argument: PASS")
    except TypeError:
        print("Testing constructor with invalid header argument: FAIL")
    # User provides a valid header
    try:
        DataSet("valid header").header
        print("Testing setter with valid assignment: PASS")
    except ValueError:
        print("Testing setter with valid assignment: FAIL")
    # User provides an invalid header
    try:
        DataSet("invalid header invalid header invalid header").header
        print("Testing setter with invalid assignment: PASS")
    except ValueError:
        print("Testing setter with invalid assignment: FAIL")


def currency_unit_test():
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
    crosstable_unit_test()


r"""
--- Sample Run #1---
Method Raises EmptyDataSet Error: PASS
"""
