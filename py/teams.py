import time

import pandas as pd,bs4, requests
from selenium import webdriver
from selenium.webdriver.common.by import By


teams_url = 'https://www.hltv.org/stats/teams'
teams_req = requests.get(teams_url)

driver = webdriver.Edge()
driver.get(teams_url)
driver.implicitly_wait(120)
driver.find_element(By.ID,'CybotCookiebotDialogBodyButtonDecline').click()


def get_teams_overview():

    teams_overview = pd.read_html(teams_req.text)[0]
    

def get_teams_ftu():
    
    time.sleep(5)
    driver.find_element(by=By.LINK_TEXT,
                        value='FTU').click()
    teams_ftu = pd.read_html(requests.get(driver.current_url).text)[0]
    
    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    teams_ftu_ct = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    teams_ftu_t = pd.read_html(requests.get(driver.current_url).text)[0]
    

def get_teams_pistols():
    
    time.sleep(5)
    driver.find_element(by=By.LINK_TEXT,
                        value='Pistol rounds').click()
    teams_pistols = pd.read_html(requests.get(driver.current_url).text)[0]

    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[2]').click()
    teams_pistols_ct = pd.read_html(requests.get(driver.current_url).text)[0]
    
    driver.find_element(By.XPATH,
                        value='/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div/a[3]').click()
    teams_pistols_t = pd.read_html(requests.get(driver.current_url).text)[0]


get_teams_overview()
get_teams_ftu()
get_teams_pistols()
driver.quit()
