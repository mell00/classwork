"""
Assignment #1 by
    Madison Ell
    6/29/2020
    A program that asks the user for their name, then returns a greeting.
"""


def main():
    """Obtain the user's name."""
    my_name = input("Please enter your name: ")
    print("Hello " + my_name + ", nice to meet you!")


if __name__ == "__main__":
    main()


r"""
--- Sample Run ---
Please enter your name: Madison
Hello Madison, nice to meet you!
"""
