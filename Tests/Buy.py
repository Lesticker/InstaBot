import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.alert import Alert
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..","."))
import time
from Pages.loginpage import LoginPage
from Pages.imagessite import ImagesSite
from Pages.app import Application

class BuyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.s = Service(r"C:\Users\Dawid\.wdm\drivers\chromedriver\win32\104\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.maximize_window()
    
    def test_01_login_page(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        home_page = LoginPage(driver)
        home_page.login_to_account()

    def test_02_find(self):
        driver = self.driver
        app = Application(driver)
        app.find_one_hashtag()

    def test_03_like(self):
        driver = self.driver
        liking = ImagesSite(driver)
        # go into first img from DOM
        liking.get_into_img()
        for i in range(10):
            liking.like_photo()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
    
if __name__ =='__main__':
    unittest.main()


#options = webdriver.ChromeOptions()




