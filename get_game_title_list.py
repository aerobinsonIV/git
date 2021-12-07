import os
url = "https://www.listchallenges.com/all-north-american-release-playstation-games/list/"

# for file in os.listdir("."):

def parseOnePage(lines):
    trigger_string = '<div class="item-name">'

    titles = []

    next_line_is_title = False

    for line in lines:
        if next_line_is_title:
            titles.append(line.strip().replace("&#39;", "’").replace("&amp;", "&").replace("&#228;", "ä"))
            next_line_is_title = False

        if line.__contains__(trigger_string):
            next_line_is_title = True
    return titles

for i in range(1, 34):
    command = 'wget ' + url + str(i) + " -P ./downloaded-files/"
    os.system(command)
    # print(command)


outputFile = open("game_title_list.txt", 'w')

for file in os.listdir("./downloaded-files/"):
    if not file.endswith(".py"):
        f = open("./downloaded-files/" + file)
        lines = f.readlines()
        f.close()

        titles = parseOnePage(lines)

        for title in titles:
            outputFile.write(title + "\n")

outputFile.close()