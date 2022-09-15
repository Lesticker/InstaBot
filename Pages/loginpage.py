from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators
from Pages.settings import Settings
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    
    def login_to_account(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.cookie_xpath))).click()
        time.sleep(2)
        input1 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.username_xpath)))
        input1.send_keys(Settings.username)
        input2 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.password_xpath)))
        input2.send_keys(Settings.password)
        self.driver.find_element(*Locators.login_button).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.not_now))).click()
        #currently not used in case of pop up returns use below command
        #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.disable_notification))).click()
        

