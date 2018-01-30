from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
asins = pd.read_csv('asins.csv')
asindetails = pd.DataFrame(columns=['asin','category'])
driver = webdriver.Chrome()
driver.implicitly_wait(10)
for index, row in asins.iterrows():
    if index >= 1570:
        global asindetails
        baseurl = 'https://www.amazon.com/exec/obidos/ASIN/'
        driver.get(baseurl + str(row[0]))
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='wayfinding-breadcrumbs_feature_div']/ul/li[1]/span/a"))
                )
        except: 
            continue 
        temp = pd.DataFrame({
            'asin': row[0],\
            'category': [driver.find_element_by_xpath("//*[@id='wayfinding-breadcrumbs_feature_div']/ul/li[1]/span/a").text]
            })
        asindetails = asindetails.append(temp)
        asindetails.to_csv("asincat1570.csv")
print "Job Complete"