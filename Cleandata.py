from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
asins = pd.read_csv('asins.csv')
asindetails = pd.DataFrame(columns=['asin','price'])
driver = webdriver.Chrome()
driver.implicitly_wait(10)
for index, row in asins.iterrows():
    if index >= 3043 and index <= 5000:
        global asindetails
        global asinsfailed
        baseurl = 'https://www.amazon.com/exec/obidos/ASIN/'
        driver.get(baseurl + str(row[0]))
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='priceblock_ourprice']"))
                )
        except: 
            print "Could not find ASIN details. Skipping: ", row[0]
            continue 
        temp = pd.DataFrame({
            'asin': row[0],\
            'price': [driver.find_element_by_xpath("//*[@id='priceblock_ourprice']").text.replace('$','')]
            #'reviews': [driver.find_element_by_xpath("//*[@id='acrCustomerReviewText']").text.replace(' customer reviews','').replace(' customer review','')],\
            #'rating': [driver.find_element_by_xpath("//*[@id='reviewSummary']/div[2]/span/a/span").text.replace(' out of 5 stars','')],\
            #'category': [driver.find_element_by_xpath("//*[@id='wayfinding-breadcrumbs_feature_div']/ul/li[1]/span/a").text]
            })
        asindetails = asindetails.append(temp)
        asindetails.to_csv("asinprice_2745.csv")
print "Job Complete"