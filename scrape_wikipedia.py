# (title, developer(s), publisher(s), year)
from bs4 import BeautifulSoup

def html2txt(input):
    return input.getText().strip()

def get_north_america_field(input):
    #If a game has different titles in different regions, the titles are seperated by "•". Or sometimes ",". It's very inconsistent.
    #Regional names are marked by the title ending with NA, UK, PAL, or JP. Some titles don't have any of these endings, which means they're the standard title for a game used in all except specific regions.
    
    #First: Is the input string actually one that contains multiple regional variants?
    if not "•" in input:
        if not (("NA" in input or "UK" in input or "PAL" in input or "JP" in input) and "," in input):
            print(f"{input} Does not have regional variants")
            return
    print(f"{input} DOES have regional variants")
    # if "•" in input:
    #     regional_titles = input.split("•")

    #     for title in regional_titles:
    #         if title[-2:] == "NA":
    #             #Trim off explicit North America indicator
    #             title_data = title[:-2]
    #             break
    #         elif title[-2:] != "JP" and title[-3:] != "PAL" and title[-2:] != "UK":
    #             #No explicit North America indicator, game was marketed in North America with standard title, don't trim
    #             title_data = title
    #             break

def parse_wikipedia_html_file(input_file):
    doc = BeautifulSoup(input_file, "html.parser")

    softwarelist_table = doc.find_all(id="softwarelist")[0]

    table_rows = softwarelist_table.find_all("tr")

    north_america_games = []

    for row in table_rows[2:]:
        table_data = row.findAll("td")

        # Ignore games that were not released in North America
        if html2txt(table_data[5]) != "Unreleased":
            title_data = html2txt(table_data[0])

            get_north_america_field(title_data)

            # (title, developer(s), publisher(s), year)
            north_america_games.append((title_data, html2txt(table_data[1]), html2txt(table_data[2]), html2txt(table_data[5])[-4:]))

    return north_america_games
