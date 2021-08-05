# import statements

# functions go here

# Checks that ticket name is not blank or has a digit in it
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is blank or has digits in it, show error
        if any(char.isdigit() for char in response) or response.strip() == "":
            print("Please enter only alphabetical characters in your name.")

        # If name is not blank, code continues
        else:
            return response

# Checks for an integer between two values
def integer_checker(question):
    valid = False

    while not valid:
        # Check if the response recorded is an integer
        try:
            response = int(input(question))
            return response
        # If the response is not an integer, show an error
        except ValueError:
            print("Please enter a whole number between 12 and 130")

# -- Main Routine --

# Set up dictionaries / lists needed to hold data

# Ask the user if they have used the program before and show instructions if necessary

# Loop to get ticket details
name = ""
ticket_count = 0
max_tickets = 5

while name != "xxx" and ticket_count < max_tickets:
    if max_tickets - ticket_count == 1:
        print("*** There is ONE seat left ***")
    else:
        print("You have {} seats left".format(max_tickets - ticket_count))

    # Get name (Can't be blank or have a digit)
    name = not_blank("Name: ")

    # End the loop if exit code is entered
    if name == "xxx":
        break

    # Get age (has to be a whole number between 12 and 130)
    age = integer_checker("Age: ")

    # Check if age is valid (between 12 and 130)
    if age < 12:
        print("Sorry, you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    ticket_count += 1

if ticket_count == max_tickets:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. \n"
              "There are {} seat(s) still available".format(ticket_count, max_tickets - ticket_count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply subcharge if necessary)

# Calculate total sales and profit

# Output data to text file

# Functions go here
