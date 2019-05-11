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


class SearchPage(BasePage):

    def clickFilter(self):
        try:
            elem1 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span/span[text()='Filters']")))
            elem1.click()
            print "Was able to click filter"
        except TimeoutException as ex:
            print ex.message
            print "Was not able to click Filter"

    def selectHouseFilter(self):
        try:
            elem4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@data-rf-test-name="uipt1"]')))
            self.driver.execute_script("arguments[0].click();", elem4)
            print "Was able to click House option"
        except TimeoutException as ex:
            print ex.message
            print "Wasnt able to click House option"    
    
    def selectBathFilter(self):
        try:
            xpath_baths="//span[contains(@class, 'withFlyout withOptions field select Stepper Select clickable optional baths')]/span[contains(@class, 'input')]/span[contains(@class, 'step-up')]"
            elem7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_baths)))
            self.driver.execute_script("arguments[0].click();", elem7)
            print "Was able to add Bath option"
        except TimeoutException as ex:
            print ex.message
            print "Wasnt able to add Bath option"    
    
    def selectOpenHouseFilter(self):
        try:
            xpath_openhousee = "//div[contains(@class, 'doubleRow flexAlignStart')]/div[1]/div[1]/span[contains(@class, 'field Checkbox styled optional label-right')]/label[contains(@class, 'label')]"
            elem5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_openhousee)))
            self.driver.execute_script("arguments[0].click();", elem5)
            print "Was able to click Open House option"
        except TimeoutException as ex:
            print ex.message
            print "Wasnt able to click Open House optiion"
    
    def clickApplyFilters(self):
        try:
            xpath_apply = "//button[contains(@class, 'button Button primary applyButton buttonBorder')]/span"
            elem8 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_apply)))
            self.driver.execute_script("arguments[0].click();", elem8)
            print "Was able to Apply"
        except TimeoutException as ex:
            print ex.message
            print "Wasnt able to Apply"
    
    def verifyFiltersHouseBathOpenHouse(self):
        try:
            xpath_verify = "//div[text()[contains(.,'1+ baths, house, open house this weekend')]]"
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_verify)))
            print "Verify shows that the filters were submitted correctly"
        except:
            print "Verify shows that the filters submited did not verify to be submited on browser output. Report bug to Redfin"