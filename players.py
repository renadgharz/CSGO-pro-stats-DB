import time

import pandas as pd,bs4, requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.implicitly_wait(120)

def get_players_overview():

    players_url = 'https://www.hltv.org/stats/players'

    driver.get(players_url)
    time.sleep(10)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonDecline').click()

    players_overview = pd.read_html(requests.get(players_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_overview_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_overview_t = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.quit()


def get_players_flashes():

    players_flashes_url = 'https://www.hltv.org/stats/players/flashbangs'

    driver.get(players_flashes_url)
    time.sleep(10)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonDecline').click()

    players_flashes = pd.read_html(requests.get(players_flashes_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_flashes_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_flashes_t = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.quit()


def get_players_op_kills():

    players_op_kills_url = 'https://www.hltv.org/stats/players/openingkills'

    driver.get(players_op_kills_url)
    time.sleep(10)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonDecline').click()

    players_op_kills = pd.read_html(requests.get(players_op_kills_url).text)[0]

    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/a[5]').click()
    players_op_kills = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    players_op_kills_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    players_op_kills_t = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.quit()


def get_players_pistols():

    players_pistols_url = 'https://www.hltv.org/stats/players/pistols'

    driver.get(players_pistols_url)
    time.sleep(10)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonDecline').click()

    players_pistols = pd.read_html(requests.get(players_pistols_url).text)[0]

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


get_players_overview()
get_players_flashes()
get_players_op_kills()
get_players_pistols()