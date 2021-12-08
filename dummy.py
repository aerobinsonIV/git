import scrape_wikipedia as sw


with open("resources/wiki1.html", 'r') as html:
    games = sw.parse_wikipedia_html_file(html)


# for game in games:
#     print(game)

# print(f"{len(games)} games found.")