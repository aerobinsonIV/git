import sqlite3
import os
from tqdm import tqdm

import harrys_game_list_parser as parser
import game_title_matcher as matcher

titles_file = "resources/game_title_list.txt"
games_file = "resources/harrys_game_list.txt"

archive =   ["Final Fantasy VII", 
            "Monster Rancher 2", 
            "Need for Speed III: Hot Pursuit", 
            "NHL 99", 
            "Oddworld: Abe’s Exoddus", 
            "Oddworld: Abe’s Oddysee", 
            "Spyro the Dragon", 
            "Vandal Hearts II", 
            "Warhammer: Shadow of the Horned Rat", 
            "Bust-A-Move 2 - Arcade Edition", 
            "Bust-A-Move ’99", 
            "Caesars Palace"]

# Replace quotes with weird unicode quotes that look almost the same but don't need to be escaped
def replace_quotes(input):
    weird_single_quote = "’"
    return input.replace("'", weird_single_quote)

# ******************************Database creation***************************************

# Get list of game titles from my file
with open(titles_file, "r") as game_file:
    game_titles = game_file.readlines()

# Open database
connection = sqlite3.connect("games.db")
cursor = connection.cursor()

# Create games table
cursor.execute("CREATE TABLE games (title text, year int, developer text, publisher text, genre text, in_archive integer, rarity integer, summary text, notes text)")

for game_title in game_titles:
    
    cleaned_game_title = replace_quotes(game_title)[:-1]
    
    command = f"insert into games values ('{cleaned_game_title}', '0', '-', '-', '-', 0, 0, '-', '-')"
    cursor.execute(command)


# *****************************************************Title/data matching******************************

#Load games from Harry's data file
game_dict = parser.load_games_from_file(games_file)

dict_keys = game_dict.keys()

matched_titles_and_keys = []

print("Matching game titles to games...")
for i in tqdm(range(0, len(game_titles))):

    matching_key = matcher.find_match(game_titles[i][:-1], dict_keys)

    if matching_key:
        matched_titles_and_keys.append((game_titles[i][:-1], matching_key))

for pair in matched_titles_and_keys:
    # Dict entries have format (company, year, rarity_num)
    publisher_command = f"update games set publisher = '{game_dict[pair[1]][0]}' where title = '{pair[0]}'"
    year_command = f"update games set year = {game_dict[pair[1]][1]} where title = '{pair[0]}'"
    rarity_command = f"update games set rarity = {game_dict[pair[1]][2]} where title = '{pair[0]}'"

    if pair[0] in archive:
        in_archive_command = f"update games set in_archive = 1 where title = '{pair[0]}'"
        cursor.execute(in_archive_command)
    
    cursor.execute(publisher_command)
    cursor.execute(year_command)
    cursor.execute(rarity_command)

# Close out
connection.commit()
connection.close()
