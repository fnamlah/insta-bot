from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

import time
INSTAGRAM_USERNAME = "-"
INSTAGRAM_PASSWORD = "-"

chrome_driver_path = Service("-")


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD)
        time.sleep(5)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(5)

        not_save = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_yn"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        not_save.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/nike/")
        time.sleep(3)

        followers = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_5s"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)

    def follow(self):
        self.driver.get("https://www.instagram.com/nike/followers/")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


instagram = InstaFollower(chrome_driver_path)
instagram.login()
instagram.follow()
time.sleep(1000)