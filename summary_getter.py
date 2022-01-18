from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# gameSite = "https://gamefaqs.gamespot.com/search?game="
# driver.get(gameSite)


gameFile = open("./games_in_db.txt", "r")
outputFile = open("./game_descriptions_combo.txt", "a")
rOutputFile = open("./game_descriptions_combo.txt", "r")
errorFile = open("./game_errors.txt", "w")
titles = gameFile.readlines()

alreadyDone = []
for t in rOutputFile.readlines():
    if(t[0] == '>'):
        title = t[1:].replace("\n", "")
        alreadyDone.append(title)
rOutputFile.close()

for gameName in titles:
    gameName = gameName.replace("\n", "")
    if(gameName in alreadyDone):
        # print(f"{gameName} already been done")
        continue

    print(f"{gameName} hasn't been done")
    # try:
    #     driver.get(gameSite + gameName.replace(" ", "+"))
    #     driver.find_elements_by_link_text("PlayStation")[0].click()

    #     myElem = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'game_desc')))

    #     desc = driver.find_element_by_class_name("game_desc")
    #     outputFile.write(">{}\n{}\n".format(
    #         gameName, desc.text.replace("\n", ".")))
    #     outputFile.flush()
    # except Exception as e:
    #     print(e)
    #     errorFile.write("{}\n".format(gameName))
    #     errorFile.flush()
    #     pass
