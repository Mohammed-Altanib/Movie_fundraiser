import re

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

# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

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









