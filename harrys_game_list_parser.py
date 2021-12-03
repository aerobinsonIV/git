# (title, company, year, rarity_num, rarity_rank)

def load_games_from_file(filename):

    with open(filename, 'r') as games_file:
        game_lines = games_file.readlines()

    game_dict = {}

    for line in game_lines:
        title = line[line.find("Title") + 7:line.find(";Company")]
        company = line[line.find("Company") + 9:line.find("; PubYr")]
        year = line[line.find("PubYr") + 7:line.find("; Rarity")]
        rarity_num = line[line.find("Rarity") + 8:line.find(" percent")]

        game_dict[title] = (company, year, rarity_num)

    return game_dict