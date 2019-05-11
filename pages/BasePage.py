from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-chromedriver', type=str,
                    help='this is the path to chrome driver')

args = parser.parse_args()

class BasePage():
    driver = webdriver.Chrome(args.chromedriver)
    def teardown(self):
        self.driver.close()