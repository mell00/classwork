from Assignment_7 import DataSet, currency_converter


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


def cross_table_statistics_unit_test():
    """Conduct unit testing for DataSet class cross-table method."""
    my_set = DataSet()
    print("Testing _cross_table_statistics")
    # No data loaded into program
    try:
        my_set._cross_table_statistics("test", "test")
        print("Method Raises EmptyDataSet Error: Fail")
    except my_set.EmptyDatasetError:
        print("Method Raises EmptyDataSet Error: Pass")
    except:
        print("Method Raises EmptyDataSet Error: Fail")
    my_set.load_default_data()
    # User calls with match in Borough column but invalid Property Type
    if my_set._cross_table_statistics("Queens", "a") == (None, None, None):
        print("Invalid Property Type Returns None Tuple: Pass")
    else:
        print("Invalid Property Type Returns None Tuple: Fail")
    # User calls with invalid Borough but match in Property Type column
    if my_set._cross_table_statistics("a", "Private Room") == \
            (None, None, None):
        print("Invalid Borough Returns None Tuple: Pass")
    else:
        print("Invalid Borough Returns None Tuple: Fail")
    # User calls valid Borough and Property Type columns, with no match
    if my_set._cross_table_statistics("Queens", "Private Room") == \
            (None, None, None):
        print("No Matching Rows Returns None Tuple: Pass")
    else:
        print("No Matching Rows Returns None Tuple: Fail")
    # User calls valid Borough and Property Type columns, with 1 match
    if my_set._cross_table_statistics("Queens", "Entire home / apt") == \
            (350, 350, 350):
        print("One Matching Row Returns Correct Tuple: Pass")
    else:
        print("One Matching Row Rows Returns Correct Tuple: Fail")
    # User calls valid Borough and Property Type columns, with 2+ matches
    if my_set._cross_table_statistics("Brooklyn", "Private room") == \
            (50, 88.8, 120):
        print("Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("Multiple Matching Rows Returns Correct Tuple: Fail")


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


if __name__ == '__main__':
    dataset_unit_test()
    cross_table_statistics_unit_test()
    currency_unit_test()
