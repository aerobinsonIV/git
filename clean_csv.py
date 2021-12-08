with open("resources/games_csv.txt") as games_file:
    lines = games_file.readlines()

for line in lines:
    print(line.replace('"', "").replace(",-", ",").replace("’", "'"), end="")