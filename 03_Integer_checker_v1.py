# Function goes here

def integer_checker(question):
    valid = False

    while not valid:
        try:
            response = int(input(question))
            if response < 12 or response > 130:
                print("Please enter a whole number between 12 and 130")
            else:
                return response
        except ValueError:
            print("Please enter a whole number between 12 and 130")
            print()

# Main routine
age = integer_checker("Age: ")
