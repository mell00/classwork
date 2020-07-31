"""
Assignment #7 by
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

from enum import Enum

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


class Categories(Enum):
    LOCATION = 1
    PROPERTY_TYPE = 2


class Stats(Enum):
    MIN = 1
    AVG = 2
    MAX = 3

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        """ Given a label from each category, calculate summary
        statistics for the items matching both labels. Returns
        a tuple of min, average, max from the matching rows.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        value_list = [item[2] for item in self._data if
                      descriptor_one == item[0] and item[1] == descriptor_two]
        if len(value_list) == 0:
            return None, None, None
        return min(value_list), sum(value_list) / len(value_list), max(value_list)


class DataSet(Categories, Stats):
    """ the DataSet class will present summary tables based on
    information imported from a .csv file
    """

    class EmptyDatasetError(Exception):
        pass

    header_length = 30

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self._header = ""
        self._labels = {Categories.LOCATION: set(), Categories.PROPERTY_TYPE: set()}
        self._active_labels = {Categories.LOCATION: set(), Categories.PROPERTY_TYPE: set()}

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value: str):
        if type(value) == str and self.header_length > len(value):
            self._header = value
        else:
            raise ValueError

    def load_default_data(self):
        """ Load sample data into self.__data"""
        self._initialize_sets()
        self._data = [("Staten Island", "Private room", 70),
                      ("Brooklyn", "Private room", 50),
                      ("Bronx", "Private room", 40),
                      ("Brooklyn", "Entire home / apt", 150),
                      ("Manhattan", "Private room", 125),
                      ("Manhattan", "Entire home / apt", 196),
                      ("Brooklyn", "Private room", 110),
                      ("Manhattan", "Entire home / apt", 170),
                      ("Manhattan", "Entire home / apt", 165),
                      ("Manhattan", "Entire home / apt", 150),
                      ("Manhattan", "Entire home / apt", 100),
                      ("Brooklyn", "Private room", 65),
                      ("Queens", "Entire home / apt", 350),
                      ("Manhattan", "Private room", 99),
                      ("Brooklyn", "Entire home / apt", 200),
                      ("Brooklyn", "Entire home / apt", 150),
                      ("Brooklyn", "Private room", 99),
                      ("Brooklyn", "Private room", 120)]

    def _initialize_sets(self):
        if not self._data:
            raise DataSet.EmptyDatasetError
        Categories.LOCATION = {"Bronx", "Manhattan", "Staten Island", "Brooklyn", "Queens"}
        Categories.PROPERTY_TYPE = {"Private room", "Entire home / apt"}

    def display_cross_table(self):
        if not self._data:
            raise DataSet.EmptyDatasetError
        for key in self._labels:
            print(f"{key}  {self._labels[key]}")


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
        home_currency_input = input("What is your home currency? ")
        try:
            conversions[home_currency_input]
        except KeyError:
            continue
        break
    currency_options(home_currency_input)
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


if __name__ == "__main__":
    main()

r"""
--- Sample Run #1---
Method Raises EmptyDataSet Error: PASS
"""
