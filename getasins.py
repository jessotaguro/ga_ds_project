import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
from sqlalchemy import update
import datetime 
now = datetime.datetime.now()

data = pd.read_csv('data.csv')
print data.shape

print data.isnull().sum()

#driver = webdriver.Chrome()
#driver.implicitly_wait(30)
#driver.get("https://wanamaker.amazon.com")