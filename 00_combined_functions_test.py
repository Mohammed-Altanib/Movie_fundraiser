# start of loop

name = ""
ticket_count = 0
max_tickets = 5

# Display available seats left before booking
while name != "xxx" and ticket_count < max_tickets:
    if max_tickets - ticket_count == 1:
        print("You have {} seat left".format(max_tickets - ticket_count))
    else:
        print("You have {} seats left".format(max_tickets - ticket_count))

    # Get details + not blank function
    name = input("Name: ")
    if any(char.isdigit() for char in name) or name.strip() == "":
        print()
        print("Please enter only alphabetical characters in your name.")
        print()
    elif name == "xxx":
        continue
    else:
        ticket_count += 1
        print()

# Display available seats left after booking
if ticket_count == max_tickets:
    print("You have sold all available tickets!")
elif max_tickets - ticket_count == 1:
    print(("You have sold {} tickets. \n"
          "There is {} seat still available".format(ticket_count, max_tickets - ticket_count)))
else:
    print("You have sold {} tickets. \n"
          "There are {} seats still available".format(ticket_count, max_tickets - ticket_count))


