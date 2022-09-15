# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.alert import Alert
from Pages.locators import Locators
# from selenium.common.exceptions import TimeoutException
import time


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
                red_heart.click()
                time.sleep(1)
                print("lajknal mooooooooooooooooooooooooooooooooo")
                return False
            except:
                time.sleep(2)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((Locators.next_photo))).click()
                print("pominal")
