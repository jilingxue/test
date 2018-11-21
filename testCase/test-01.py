from selenium import webdriver
from logger import Logger
from base import browser
from screen_shot import screenShot
from UiObjectMap.page_object import Login
from read_config import readConfig
from base import ReadUiObjectMap
import unittest
from time import sleep
log = Logger('testCase').get_log()

class Physics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser('chrome')
        cls.RU = ReadUiObjectMap(cls.driver)
        cls.url = readConfig('url','student')
    def test_01(self):
        try:
            self.driver.get(self.url)
            title = self.driver.title
            self.assertEqual(title,'智适应教育','页面打开错误')
            size = self.driver.get_window_size()
            log.info('屏幕大小：%s' %(size))
        except:
            log.exception('打开主页失败')
            screenShot(self.driver,'打开主页失败')
            #raise ('打开主页失败')
    def test_02_login(self):
        try:
            Login(self.driver).login('spyx5211wulibayiwuerbasiliu','815383')
            sleep(3)
            page_source = self.driver.page_source
            self.assertTrue('我的课程' in page_source,'登录失败，页面没有‘我的课程’')
        except:
            log.exception('登录失败')
            screenShot(self.driver,'登录失败')
            raise ('登录失败')


if __name__ == '__main__':
    unittest.main()