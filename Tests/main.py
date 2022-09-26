import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "."))
from Pages.login_page import LoginPage
from Pages.images_page import ImagesSite
from Pages.main_page import Application
from Pages.settings import settings_data
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BuyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.s = Service(r"../chromedriver/104/chromedriver.exe")
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
        for i in range(settings_data.entered_number_of_likes):
            liking.like_photo()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
