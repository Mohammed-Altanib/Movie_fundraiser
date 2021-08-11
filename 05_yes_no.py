# New Fuction

def yes_no_checker(question):
    valid = False
    while not valid:

        # Ask question and put response in lowercase, and also check if the response is a string
        try:
            response = input(question).strip().lower()

            if response == "yes" or response == "y":
                return "yes"

            elif response == "no" or response == "n":
                return "no"
            else:
                print("Sorry, that is not a valid response\n"
                      "(Enter \"yes\" or \"no\")")
                print()

        except TypeError:
            print("Sorry, that is not a valid response\n"
                      "(Enter \"yes\" or \"no\")")
            print()

# Test function
for i in range(7):
    want_snacks = yes_no_checker("Do you want snacks?: ")
    print("Answer OK, you said: {}".format(want_snacks))
    print()
