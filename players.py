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


def get_players_overview():

    players_overview = pd.read_html(players_url.text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_overview_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_overview_t = pd.read_html(requests.get(driver.current_url).text)[0]


def get_players_flashes():

    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/a[4]').click()
    players_flashes = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_flashes_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_flashes_t = pd.read_html(requests.get(driver.current_url).text)[0]


def get_players_op_kills():

    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/a[5]').click()
    players_op_kills = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_op_kills_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_op_kills_t = pd.read_html(requests.get(driver.current_url).text)[0]


def get_players_pistols():

    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/a[6]').click()
    players_pistols = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_pistols_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_pistols_t = pd.read_html(requests.get(driver.current_url).text)[0]


driver.quit()
