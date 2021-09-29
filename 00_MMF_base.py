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
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&M's", "m&m's", "mms", "mm", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h2O", "d"],
        ["orange juice", "oj", "o", "juice", "e"]
    ]


    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

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

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# initialize loop so that it runs at least once
name = ""
ticket_count = 0
max_tickets = 5
ticket_sales = 0

# initialize lists ( to make data-frame in due course
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store subcharge multiplier
surcharge_mult_list = []

# lists to store summary data
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []

# data frame dictionary

movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
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
    snack_order = get_snack()

    # Assume no snack has been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount


    # Ask for payment method (and apply subcharge if necessary)
        # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit): ").lower()
        how_pay = snack_checker(how_pay, pay_method)
        if how_pay == "invalid choice":
            print("Please enter a valid choice")
            print()

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)
# End of ticket loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')


movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# set up summary dataframe
# populate snack items
for item in snack_lists:
    summary_data.append(sum(item))

# get snack profit
# get snack total from panda
snack_total = movie_frame['Snacks'].sum
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# get ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# create summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('item')

# set up columns to be printed
pandas.set_option('display.max_columns', None)

# display numbers in 2 dp
pandas.set_option('precision', 2)

print()
print("*** Ticket / Snack Information ***")
print()
print(movie_frame[['Ticket', 'Snacks', 'Subtotal',
                       'Surcharge', 'Total']])

print()

print("*** Snack / Profit summary")
print()
print(summary_frame)


# Calculate ticket profit

ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count == max_tickets:
    print("You have sold all the available tickets")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count, max_tickets - ticket_count))
