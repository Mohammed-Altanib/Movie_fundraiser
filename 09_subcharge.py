# loop until exit code
name = ""
while name == "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit): ").lower()
        how_pay = snack_checker(how_pay, pay_method)
