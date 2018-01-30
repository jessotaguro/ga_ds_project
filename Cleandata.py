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
    if index <= 5:
        global asindetails
        baseurl = 'https://www.amazon.com/exec/obidos/ASIN/'
        driver.get(baseurl + str(row[0]))
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='acrPopover']/span[1]/a/i[1]/span[class=a-icon-alt]"))
                )
        except: 
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='reviewSummary']/div[1]/a/div/div/div[1]/i/span[class=a-icon-alt]"))
                    )
            except: 
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='reviewSummary']/div[2]/span/a/span[class=arp-rating-out-of-text]"))
                        )
                except:
                    continue
                temp = pd.DataFrame({
                    'asin': row[0],\
                    'rating': [driver.find_element_by_xpath("//*[@id='reviewSummary']/div[2]/span/a/span[class=arp-rating-out-of-text]").text.replace(' out of 5 stars','')]
                    })
                asindetails = asindetails.append(temp)
                asindetails.to_csv("asinrating.csv")
            temp = pd.DataFrame({
                'asin': row[0],\
                'rating': [driver.find_element_by_xpath("//*[@id='reviewSummary']/div[1]/a/div/div/div[1]/i/span[class=a-icon-alt]").text.replace(' out of 5 stars','')]
                })
            asindetails = asindetails.append(temp)
            asindetails.to_csv("asinrating.csv")
        temp = pd.DataFrame({
            'asin': row[0],\
            'rating': [driver.find_element_by_xpath("//*[@id='acrPopover']/span[1]/a/i[1]/span[class=a-icon-alt]").text.replace(' out of 5 stars','')]
            })
        asindetails = asindetails.append(temp)
        asindetails.to_csv("asinrating.csv")
print "Job Complete"