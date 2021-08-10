# initialise loop so that it runs at least once

name = ""
ticket_count = 0
max_tickets = 5

while name != "xxx" and ticket_count < max_tickets:
    if max_tickets - ticket_count == 1:
        print("*** There is ONE seat left ***")
    else:
        print("You have {} seats left".format(max_tickets - ticket_count))

    # Get details
    name = input("Name: ")
    if name == "xxx":
        continue
    else:
        ticket_count += 1
        print()

if ticket_count == max_tickets:
    print("You have sold all available tickets!")
elif max_tickets - ticket_count == 1:
    print(("You have sold {} tickets. \n"
          "There is {} seat still available".format(ticket_count, max_tickets - ticket_count)))
else:
    print("You have sold {} tickets. \n"
          "There are {} seats still available".format(ticket_count, max_tickets - ticket_count))
