# SUPER IMPORTANT: SQLITE IS BUILT INTO PYTHON3. DO NOT WASTE AN ENTIRE HOUR TRYING TO INSTALL THE SQLITE3 PACKAGE
# SCREAMING AND CRYING
import sqlite3
import sys

### Input file format:
# >Title1
# Description 1. Super epic game.
# >Title2: the sequel
# Description 2. Pretty epic but the original was better tbh

summaries_file = sys.argv[1]
print("Summaries file is " + summaries_file)

# Replace quotes with weird unicode quotes that look almost the same but don't need to be escaped
def replace_quotes(input):
    weird_single_quote = "’"
    return input.replace("'", weird_single_quote)

with open(summaries_file, "r") as summaries:
    summaries_file_lines = summaries.readlines()

summaries = []
game_titles = []

game_summary_pairs = []

current_summary = ""
current_title = ""

for i, line in enumerate(summaries_file_lines):

    if line[:1] == '>':
        # We found a new game title, previous summary is over
        # Create tuple for previous (game, summary) pair and add to list
        temp_pair = (replace_quotes(current_title), replace_quotes(current_summary))
        game_summary_pairs.append(temp_pair)
        
        # Start fresh
        current_title = line[1:-1]
        current_summary = ""
    else:

        # TODO: summary parsing
        # power and money..All in real-time
        # 
        # This line is part of a summary, append to current summary string
        current_summary += line[:-1]
    

# Open database
connection = sqlite3.connect("games.db")
cursor = connection.cursor()

for pair in game_summary_pairs:
    summary_command = f"update games set summary = '{pair[1]}' where title = '{pair[0]}'"
    print(f"running: {summary_command}")
    cursor.execute(summary_command)

# Close out
connection.commit()
connection.close()


