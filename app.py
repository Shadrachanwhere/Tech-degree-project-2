import constants
from constants import formatted_data

Panthers, Bandits, Warriors = constants.balanced_team(formatted_data)


def app_basket_ball():
    print("-_-_  MENU -_-_-_\n\n\n A) Display Team Stats\n B) Quit\n")

    option = input("Enter an option: ").lower()
    if option == "a":
        print("-_-_ TEAMS -_-_\n\n 1) Panthers\n 2) Bandits\n 3) Warriors")
    else:
        print("Thank you for using this app! Goodbye")

    team_select = input("Enter an option: ")
    if team_select == "1":
        constants.stats(Panthers)
    elif team_select == "2":
        constants.stats(Bandits)
    else:
        constants.stats(Warriors)
    continue_app = input("Press enter to continue: ")
    if continue_app == "":
        app_basket_ball()


app_basket_ball()
