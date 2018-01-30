from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
asins = pd.read_csv('asins.csv')
asindetails = pd.DataFrame(columns=['asin','rating'])
driver = webdriver.Chrome()
driver.implicitly_wait(10)
for index, row in asins.iterrows():
    if index >= 12430:
        baseurl = 'https://www.amazon.com/exec/obidos/ASIN/'
        driver.get(baseurl + str(row[0]))
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='reviewSummary']/div[2]/span"))
                )
        except: 
            continue
        temp = pd.DataFrame({
            'asin': row[0],\
            'rating': [driver.find_element_by_xpath("//*[@id='reviewSummary']/div[2]/span").text.replace(' out of 5 stars','')]
            })
        asindetails = asindetails.append(temp)
        asindetails.to_csv("asinrating12430.csv")
print ("Job Complete")


'''
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
asins = pd.read_csv('asins.csv')
asindetails = pd.DataFrame(columns=['asin','rating'])
driver = webdriver.Chrome()
driver.implicitly_wait(10)
for index, row in asins.iterrows():
    if index >= 0:
        baseurl = 'https://www.amazon.com/exec/obidos/ASIN/'
        driver.get(baseurl + str(row[0]))
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='acrPopover']/span[1]/a/i[1]/span"))
                )
        except: 
            continue
        hoverrating = driver.find_element_by_xpath("//*[@id='acrPopover']/span[1]/a/i[1]/span")
        hover = ActionChains(driver).move_to_element(hoverrating)
        hover.perform()
        time.sleep(2)
        try:
            WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='a-popover-content-5']/div/div/div/div[1]/span"))
                    )
        except: 
            continue
        rating = driver.find_element_by_xpath("//*[@id='a-popover-content-5']/div/div/div/div[1]/span").text.replace(' out of 5 stars','')
        temp = pd.DataFrame({
            'asin': row[0],\
            'rating': rating
            })
        asindetails = asindetails.append(temp)
        asindetails.to_csv("asinrating.csv")
print ("Job Complete")
'''