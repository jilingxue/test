from logger import Logger
from base import ReadUiObjectMap
from screen_shot import screenShot
from selenium.webdriver import ActionChains
from time import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from file_path import write

log = Logger(logName='page_object').get_log()

class Login():
    def __init__(self,driver):
        self.driver = driver
        self.RU = ReadUiObjectMap(self.driver)

    def userInput(self):
        user = self.RU.find_element('login','user_input')
        return user
    def passInput(self):
        pass_input = self.RU.find_element('login','pass_input')
        return pass_input
    def loginButton(self):
        login_button = self.RU.find_element('login','login_button')
        return login_button

    def login(self,username,password):
        self.userInput().send_keys(username)
        self.passInput().send_keys(password)
        self.loginButton().click()