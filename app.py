import constants
from constants import formatted_data

Panthers, Bandits, Warriors = constants.balanced_team(formatted_data)


def app_basket_ball():
    while True:
        print("-_-_  MENU -_-_-_\n\n\n A) Display Team Stats\n B) Quit\n")
        option = input("Enter an option: ").lower()
        if option == "a":
            print("-_-_ TEAMS -_-_\n\n 1) Panthers\n 2) Bandits\n 3) Warriors")
            try:
                team_select = int(input("Enter an option: "))
            except ValueError:
                print("Please select a valid option")
            else:
                if team_select == "1":
                    print(" Team: Panthers\n --------------")
                    constants.stats(Panthers)
                elif team_select == "2":
                    print(" Team: Bandits\n --------------")
                    constants.stats(Bandits)
                else:
                    print(" Team: Warriors\n --------------")
                    constants.stats(Warriors)
                continue_app = input("Press enter to continue: ")
                if continue_app == "":
                    continue

        else:
            print("Thank you for using this app! Goodbye")
            break


app_basket_ball()
