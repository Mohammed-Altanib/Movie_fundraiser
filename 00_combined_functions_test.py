snack = ""
snack_ok = ""

for i in range(0, 3):
    desired_snack = int(input("Enter the NUMBER corresponding to the snack for the snack you want\n"
                             "[1] Popcorn\n"
                             "[2] M&M's\n"
                             "[3] Pita chips\n"
                             "[4] Water\n"
                             "Snack: "))
    for var_list in valid_snacks:
        if desired_snack in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        else:
            snack_ok = "no"

    if snack_ok == "yes":
        print("Snack choice:", snack)
    else:
        print("Invalid choice")




