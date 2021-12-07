import sqlite3
import os

import harrys_game_list_parser as parser
import game_title_matcher as matcher

titles_file = "resources/game_title_list.txt"
games_file = "resources/harrys_game_list.txt"



# Replace quotes with weird unicode quotes that look almost the same but don't need to be escaped
def replace_quotes(input):
    weird_single_quote = "’"
    return input.replace("'", weird_single_quote)

# Open database
# connection = sqlite3.connect("games.db")
# cursor = connection.cursor()

#Load games from Harry's data file
game_dict = parser.load_games_from_file(games_file)

# Get list of game titles from my file
with open(titles_file, "r") as game_file:
    game_titles = game_file.readlines()

# Create games table
# cursor.execute("CREATE TABLE games (title text, developer text, publisher text, genre text, in_archive integer, rarity integer, summary text, notes text)")

dict_keys = game_dict.keys()

num_items_without_match = 0
for game_title in game_titles:

    matching_key = matcher.find_match(game_title[:-1], dict_keys)

    if matching_key:
        pass
    else:
        print(f"No match found for {game_title[:-1]}")  
    
    

    # cleaned_game_title = replace_quotes(game_title)
    # # We don't want the newline at the end of the game title
    # command = f"insert into games values ('{cleaned_game_title[:-1]}', '-', '-', '-', 0, 0, '-', '-')"
    # print(command)
    # cursor.execute(command)


# Close out
# connection.commit()
# connection.close()
