# start of loop

ticket_count = 0
max_tickets = 5

while ticket_count < max_tickets:
    name = input("Name: ")
    if any(char.isdigit() for char in name):
        print("Please enter only alphabetical characters in your name.")
    else:
        ticket_count += 1



