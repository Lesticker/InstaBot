from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators
import time
import random

class ImagesSite():

    def __init__(self, driver):
        self.driver = driver

    def get_into_img(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.first_img_xpath))).click()

    def like_photo(self):
        while True:
            try:
                red_heart = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((Locators.like)))
                time.sleep(random.uniform(0.5, 2))
                red_heart.click()
                return False
            except:
                time.sleep(random.uniform(0.5, 1))
                WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((Locators.next_photo))).click()
