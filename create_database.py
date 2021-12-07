import re
import sqlite3
import os
from fuzzywuzzy import fuzz # Fuzzy string matching library
from Levenshtein import distance as lev

titles_file = "resources/game_title_list.txt"
games_file = "resources/harrys_game_list.txt"

import harrys_game_list_parser as parser

# Replace quotes with weird unicode quotes that look almost the same but don't need to be escaped
def replace_quotes(input):
    weird_single_quote = "’"
    return input.replace("'", weird_single_quote)

# Performs substitutions and simplifications to help fuzzy matching be more accurate
def prep_name(name):
    return re.sub('[\W_]+', '', name.lower().strip().replace("&", "and")).replace("the", "").replace("2", "ii").replace("3", "iii")

#Returns the item in search_list that is most similar to input_string in form (item, lev distance)
def find_best_match(input_string, search_list):
    best_distance = 99
    best_match = ""
    
    for item in search_list:
        current_distance = lev(prep_name(input_string), prep_name(item))
        
        if(current_distance < best_distance):
            best_distance = current_distance
            best_match = item

    return (best_match, best_distance)

#Similar to find_best_match, but returns None if we're not reasonably certain it's a match
def find_match(input_title, search_list):

    best_match = find_best_match(input_title, search_list)

    if(best_match[1] < 5):
        # If we have a match with a distance of less than 5, it might be a match, or it could be a different installment of the series.

        prepped1 = prep_name(input_title)
        prepped2 = prep_name(best_match[0])
        # Check the last few chars for an exact match to exclude different versions or years.
        if prepped1[-3:] == prepped2[-3:]:
            
            # Even if the last few chars match, these might just be games with similar, short names (e.g. FIFA 2000 to F1 2000 would still be valid at this point)
            # As a last line of defense against false positives, check the match ratio with fuzzywuzzy:
            ratio = fuzz.ratio(prepped1, prepped2)
            if(ratio > 88):
                return best_match[0]

    return None

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
