import pandas as pd,bs4, requests
from selenium import webdriver
from selenium.webdriver.common.by import By

teams = 'https://www.hltv.org/stats/teams'
teams_url = requests.get(teams)

driver = webdriver.Edge()
driver.get(teams_url)
driver.implicitly_wait(120)
driver.find_element(By.ID,'CybotCookiebotDialogBodyButtonDecline').click()


def get_teams_overview():

    teams_overview = pd.read_html(teams_url.text)[0]

    print(teams_overview)


def get_teams_ftu():
    pass


def get_teams_pistols():
    pass


get_teams_overview()
driver.quit()