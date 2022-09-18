from selenium.webdriver.common.by import By

class Locators():
    #Home page objects

    cookie_xpath = (By.XPATH, "/html/body/div[4]/div/div/button[1]")
    username_xpath = (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    password_xpath = (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    login_button = (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
    cookie2_xpath = (By.XPATH, "/html/body/div[7]/div/div/div/div[1]/div/div[3]/div[3]/div/div[3]/div[1]/div[1]/div[2]/div[1]/span")
    not_now = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    disable_notification = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
    search_popup = (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div/div/div/div/div[2]/div")
    search_input = (By.XPATH, "//input[@placeholder='Szukaj']")
    first_img_xpath = (By.XPATH, "(//div[@class='_aabd _aa8k _aanf'])[1]")
    # first_img_xpath = (By.XPATH, "(//div[@class='_aagu'])[1]")
    like = (By.XPATH, "(//*[name()='svg' and @aria-label='Lubię to!' and @width=24])[2]")
    unlike = (By.XPATH, "(//*[name()='svg' and @aria-label='Nie lubię' and @width=24])[2]")
    next_photo = (By.XPATH, "//*[name()='svg' and @aria-label='Dalej']")

