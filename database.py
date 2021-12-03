import re
import sqlite3
import os
from fuzzywuzzy import fuzz # Fuzzy string matching library
from Levenshtein import distance as lev

import harrys_game_list_parser as parser

# Replace quotes with weird unicode quotes that look almost the same but don't need to be escaped
def replace_quotes(input):
    weird_single_quote = "’"
    return input.replace("'", weird_single_quote)

# Performs substitutions and simplifications to help fuzzy matching be more accurate
def prep_name(name):
    return re.sub('[\W_]+', '', name.lower().strip().replace("&", "and")).replace("the", "").replace("2", "ii").replace("3", "iii")

#Returns the item in search_list that is most similar to input_string in form (item, match_ratio)
def find_best_match(input_string, search_list):
    best_distance = 99
    best_match = ""
    for item in search_list:
        current_distance = lev(prep_name(input_string), prep_name(item))
        # print(f"Distance from {prep_name(input_string)} to {prep_name(item)} is {current_distance}")
        if(current_distance < best_distance):
            best_distance = current_distance
            best_match = item

    # print(f"Best match of {input_string} is {best_match} with distance {best_distance}")
    return (best_match, best_distance)

#Similar to find_best_match, but returns null if we're not reasonably certain it's a match
def find_match(input_string, search_list):
    # Make sure every game in the title list has a match in Harry's game data list
    best_match = find_best_match(input_string, search_list)

    if(best_match[1] < 6):
        prepped1 = prep_name(input_string)
        prepped2 = prep_name(best_match[0])
        # If we have a match over 89%, it's possibly a different installment of a series.
        # Check the last few chars for an exact match to exclude different versions or years.
        if prepped1[-3:] == prepped2[-3:]:
            print(f"Matched {game_title[:-1]} to {matching_key} (Levenshtein distance {best_match[1]})")
            return best_match[0]
    
    return None

# Open database
# connection = sqlite3.connect("games.db")
# cursor = connection.cursor()

#Load games from Harry's data file
game_dict = parser.load_games_from_file("games.txt")

# Get list of game titles from my file
with open("output.txt", "r") as game_file:
    game_titles = game_file.readlines()

# Create games table
# cursor.execute("CREATE TABLE games (title text, developer text, publisher text, genre text, in_archive integer, rarity integer, summary text, notes text)")

dict_keys = game_dict.keys()

num_items_without_match = 0
for game_title in game_titles:

    matching_key = find_match(game_title[:-1], dict_keys)

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

# Load harry's game file
# Function that takes in title and outputs year
# For each row in database, get title, run thru function, add year to database