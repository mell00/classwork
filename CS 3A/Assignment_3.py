"""
Assignment #3 by
    Madison Ell
    7/5/2020
    A program that asks the user for their name and returns a
    greeting, prints the options of a main menu, then asks the user
    for their selection and returns an appropriate message.

"""


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


if __name__ == "__main__":
    main()


r"""
--- Sample Run ---
Please enter your name: Madison
Hello Madison, nice to meet you!
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
What is your choice? 10
Please enter a value between 1 and 9.
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
What is your choice? e
Please enter a numeric value.
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
What is your choice? 2
Minimum rent functionality is not implemented yet.
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
