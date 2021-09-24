import re
import pandas

# Function goes here
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

# main routine
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]


# loop until exit code
name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit): ").lower()
        how_pay = snack_checker(how_pay, pay_method)
        if how_pay == "invalid choice":
            print("Please enter a valid choice")
            print()

    # Ask for subtotal
    subtotal = float(input("Sub total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge
    # print details
    print("Name: {} | Subtotal: ${:.2f} | Subcharge: ${:.2f} | "
          "Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))
