# (title, year, developer, publisher)
from bs4 import BeautifulSoup


with open("wiki1.html", 'r') as html:
    doc = BeautifulSoup(html, "html.parser")

print(doc.prettify())

# for line in html_lines:
#     if '<th rowspan="2" width="28%" data-sort-type="text">Title' in line:
#         print(line)