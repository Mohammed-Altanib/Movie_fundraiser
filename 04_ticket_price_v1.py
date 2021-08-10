profit = 0
name = input("Name:" )
age = int(input("Age:"))

if age < 16:
    ticket_price = 7.50
elif age > 64:
    ticket_price = 6.50
else:
    ticket_price = 10.50

profit_made = ticket_price - 5
profit += profit_made

print("{} : ${:.2f}".format(name, ticket_price))

print("Ticket profit: ${:.2f}".format(profit))


