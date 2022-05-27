import pandas as pd,bs4, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


players_url = 'https://www.hltv.org/stats/players'
players_req = requests.get(players_url)
soup = bs4.BeautifulSoup(players_req.text, 'html.parser')

driver = webdriver.Edge()
driver.get(players_url)
driver.implicitly_wait(120)
driver.find_element(By.ID,'CybotCookiebotDialogBodyButtonDecline').click()


def get_players_overview():

    players_overview = pd.read_html(players_req.text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_overview_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_overview_t = pd.read_html(requests.get(driver.current_url).text)[0]


def get_players_flashes():

    driver.find_element(by=By.LINK_TEXT,
                        value='Flashes').click()
    players_flashes = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_flashes_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_flashes_t = pd.read_html(requests.get(driver.current_url).text)[0]


def get_players_op_kills():

    driver.find_element(by=By.LINK_TEXT,
                        value='Opening kills').click()
    players_op_kills = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_op_kills_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_op_kills_t = pd.read_html(requests.get(driver.current_url).text)[0]


def get_players_pistols():

    driver.find_element(by=By.LINK_TEXT,
                        value='Pistol rounds').click()
    players_pistols = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_pistols_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_pistols_t = pd.read_html(requests.get(driver.current_url).text)[0]


get_players_overview()
get_players_flashes()
get_players_op_kills()
get_players_pistols()

driver.quit()