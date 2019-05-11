from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import argparse
from pages.LandingPage import LandingPage
from pages.SearchPage import SearchPage
from pages.BasePage import BasePage


def test_SearchWithFilters():
    LandingPage().setUp()
    LandingPage().inputCityName(city='Lake Forest, CA')
    LandingPage().submitSearchCityName(XPATH_var='//a[@href="/city/10039/CA/Lake-Forest"]')
    time.sleep(3)
    SearchPage().clickFilter()
    SearchPage().selectHouseFilter()
    SearchPage().selectBathFilter()
    SearchPage().selectOpenHouseFilter()
    SearchPage().clickApplyFilters()
    SearchPage().verifyFiltersHouseBathOpenHouse()
    BasePage().teardown()



if __name__ == "__main__":
    test_SearchWithFilters()
