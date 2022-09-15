from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators
from Pages.settings import Settings
from selenium.webdriver.common.keys import Keys
import time

class Application():


    def __init__(self, driver):
        self.driver = driver

    def find_one_hashtag(self):
        search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Locators.search_input)))
        time.sleep(1)
        search.send_keys(Settings.hashtag)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)