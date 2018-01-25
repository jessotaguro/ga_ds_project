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

campaigns = pd.read_csv('GA_NA2017.csv')
print campaigns.ad_campaign_id.nunique()

#campaigns = pd.read_csv('GA_NA2017.csv')
#print campaigns.shape
#print campaigns.ad_campaign_id.nunique()