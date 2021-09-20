import re

# works out wether string hs numbers
# and seperates string into amount and item

test_strings = [
    "Popcorn",
    "2 pc",
    "1.5OJ",
    "4OJ"
]

for item in test_strings:

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # if item has a number, seperate it itno two (numbers / items)
    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item

    # remove white spaec around snack
    desired_snack = desired_snack.strip()

    # print order
    print("Amount:", amount)
    print("Snack: ", desired_snack)
    print("Length of snack:", len(desired_snack))