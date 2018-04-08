# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:05:21 2018

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


##uncomment if using firefox
## driver=webdriver.firefox()

inpet=input("ENTER LOCATION TO GET WEATHER OF")

driver=webdriver.Chrome()
try:
    driver.get("https://www.google.co.in/search?q=weather+in+%s&rlz=1C1SQJL_enIN788IN788&oq=weather+in+delhi&aqs=chrome..69i57j69i59l2j69i60l3.6675j0j4&sourceid=chrome&ie=UTF-8"%(inpet))
except Exception as e:
    print("UNKNOWN ERROR DURING EXECUTION ")
