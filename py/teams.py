import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from connect import teams_engine

teams_url = 'https://www.hltv.org/stats/teams'
teams_req = requests.get(teams_url)

driver = webdriver.Edge()
driver.get(teams_url)
driver.implicitly_wait(120)
driver.find_element(By.ID,'CybotCookiebotDialogBodyButtonDecline').click()


def get_teams_overview():

    teams_overview = pd.read_html(teams_req.text)[0]
    
    teams_overview.to_sql('Teams_Overview', con=teams_engine, if_exists='append')


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
    
    teams_ftu.to_sql('Teams_FTU', con=teams_engine, if_exists='append')
    teams_ftu_ct.to_sql('Teams_FTU_CT', con=teams_engine, if_exists='append')
    teams_ftu_t.to_sql('Teams_FTU_T', con=teams_engine, if_exists='append')
    

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

    teams_pistols.to_sql('Teams_Pistols', con=teams_engine, if_exists='append')
    teams_pistols_ct.to_sql('Teams_Pistols_CT', con=teams_engine, if_exists='append')
    teams_pistols_t.to_sql('Teams_Pistols_T', con=teams_engine, if_exists='append')


get_teams_overview()
get_teams_ftu()
get_teams_pistols()
driver.quit()
