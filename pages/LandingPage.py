from BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import argparse


class LandingPage(BasePage):

    def setUp(self):
        url = 'https://redfin.com'
        self.driver.get(url) 
    
    def inputCityName(self,city):
        try:
            elem1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search-box-input")))
            elem1.clear()
            elem1.send_keys(city)
            elem1.send_keys(Keys.RETURN)
            print "Was able to enter " + city + " into the Search bar"
        except TimeoutException as ex:
            print ex.message
            print "Was not able to enter " + city + " into the Search bar"
    
    def submitSearchCityName(self,XPATH_var):
        try:
            elem2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_var)))
            self.driver.execute_script("arguments[0].click();", elem2)
            print "Was able to click the correct city"
        except TimeoutException as ex:
            print ex.message  
            print "Was not able to click the correct city"   
