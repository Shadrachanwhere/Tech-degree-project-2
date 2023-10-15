TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
    'name': 'Karl Saygan',
    'guardians': 'Heather Bledsoe',
    'experience': 'YES',
    'height': '42 inches'
},
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {'name': 'Sammy Adams',
     'guardians': 'Jeff Adams and Gary Adams',
     'experience': 'NO',
     'height': '45 inches'
     },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]


def cleaned_data(players):  ## a function that cleans the Players list data
    cleaned = []
    for player in players:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["guardians"] = player["guardians"].split("and")
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"].split(" ")[0])
        cleaned.append(fixed)
    return cleaned


formatted_data = cleaned_data(PLAYERS)  ## cleaned data is now stored in formatted_data


def balanced_team(b_team):  # a function to evenly balance the players across the team
    P = b_team[0:5]
    B = b_team[6:12]
    W = b_team[13:18]
    return P, B, W


def stats(team):  # a function to analyse the statistics of the player
    guardian_list = []
    player_name_list = []
    height_list = []
    count_experience = 0
    count_inexperience = 0
    for user in team:
        player_name = user["name"]
        guardian = user["guardians"]
        height = user["height"]
        player_name_list.append(player_name)
        guardian_list.append(guardian)
        height_list.append(height)
        if user["experience"]:
            count_experience += 1
        else:
            count_inexperience += 1
    average_height = int(sum(height_list) / len(height_list))
    number_of_players = len(player_name_list)
    number_of_experience = count_experience
    number_of_inexperience = count_inexperience
    print(f"Total Players: {number_of_players}")
    print(f"Number of experience: {number_of_experience}")
    print(f"Number of inexperience: {number_of_inexperience}")
    print(f"Average height: {average_height}")
    print(player_name_list)
    print(guardian_list)


def main():
    cleaned_data(PLAYERS)
    stats(team)
    balanced_team(f_data)


if __name__ == "__main__":
    main()
