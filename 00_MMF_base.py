# import statements
import re
import pandas

# Functions go here

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

# Checks number of tickets left and warns user if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if ticket_limit - tickets_sold == 1:
        print("*** There is ONE seat left ***")
    else:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    return  ""

def get_ticket_price():

    # Get age (has to be a whole number between 12 and 130)
    age = integer_checker("Age: ")

    # Check if age is valid (between 12 and 130)
    if age < 12:
        print("Sorry, you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.50
    elif age > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50

    return ticket_price

def snack_checker(choice, options):

    for var_list in options:

        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # , and possible abbreviations etc>

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj", "o", "juice", "e"]
    ]


    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # Ask the user for desired snack
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, seperate it into two (numbers / items)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = snack_checker(desired_snack, valid_snacks)

        if snack_choice == "invalid choice":
            print("Please enter a valid option")
            print()

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

            # add snack AND amount to list
        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

# -- Main Routine --

# Set up dictionaries / lists needed to hold data
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
# initialize loop so that it runs at least once
name = ""
ticket_count = 0
max_tickets = 5
ticket_sales = 0

# initialize lists ( to make data-frame in due course
all_names = []
all_tickets = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

while name != "xxx" and ticket_count < max_tickets:

    # check number of ticket limit has not been exceeded
    check_tickets(ticket_count, max_tickets)

    # Get name (Can't be blank or have a digit)
    name = not_blank("Name: ")

    # End the loop if exit code "xxx" is entered
    if name == "xxx":
        break

    # get ticket price based on age
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks

    # ask the user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks?: ").lower()
        check_snack = snack_checker(want_snack, yes_no)

        # If user doesnt enter a valid option (yes/y or no/n), generate an error and ask the question again
        if check_snack == "invalid choice":
            print("Please enter a valid option")
            print()

    # If they want snacks, ask what snacks they want
    if check_snack == "Yes":
        get_order = get_snack()

    else:
        get_order =[]

    # show snack orders
    print()
    if len(get_order) == 0:
        print("Snack ordered: None")

    else:
        print("Snacks ordered: ")

        for item in get_order:
            print(item)


    # Ask for payment method (and apply subcharge if necessary)

# End of ticket loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)


# Calculate ticket profit

ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count == max_tickets:
    print("You have sold all the available tickets")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count, max_tickets - ticket_count))
