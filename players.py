import pandas as pd,bs4, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.hltv.org/stats/players'
players_url = requests.get(url)
soup = bs4.BeautifulSoup(players_url.text, 'html.parser')

driver = webdriver.Edge()
driver.get(url)
driver.implicitly_wait(120)
driver.find_element(By.ID,'CybotCookiebotDialogBodyButtonDecline').click()


def get_players():

    players = pd.read_html(players_url.text)[0]

    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_t = pd.read_html(requests.get(driver.current_url).text)[0]


get_players()


driver.quit()
