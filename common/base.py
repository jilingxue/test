from selenium import webdriver
import os,time
import configparser
from logger import Logger
from file_path import read,write
from screen_shot import screenShot
from read_config import readConfig as rc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = Logger(logName='base').get_log()

def browser(driverType):
    if driverType == 'chrome':
        Browser = webdriver.Chrome()
        Browser.maximize_window()
        return Browser
    elif driverType == 'gecko':
        Browser = webdriver.Firefox()
        Browser.maximize_window()
        return Browser
    else:
        log.info('浏览器类型错误:%s'(driverType))
        raise ('浏览器类型错误')

#获取token，UserInfo
class GetTokenUserInfo():
    def __init__(self,driver):
        self.driver = driver

    def token_userInfo(self):
        dict = {}
        token_js = 'return localStorage.getItem("Token")'
        userInfo_js = 'return localStorage.getItem("UserInfo")'
        token = ''
        userInfo = ''
        number = 0
        while number < 10:
            number += 1
            token = self.driver.execute_script(token_js)
            time.sleep(0.5)
            if token:
                dict['token'] = token
                log.info('token:%s' %(token))
                break
        number = 0
        while number < 10:
            number += 1
            userInfo = self.driver.execute_script(userInfo_js)
            time.sleep(0.5)
            if userInfo:
                dict['UserInfo'] = userInfo
                log.info('UserInfo:%s' %(userInfo))
                break
        if token and userInfo:
            write('token_userInfo.txt',str(dict))
            return dict
        else:
            log.info('Token或UserInfo为空，token:%s,userInfo:%s' %(token,userInfo))



def UiObjectMapPath():
    Path = os.path.dirname(os.path.dirname(__file__))
    Path = os.path.join(Path,'UiObjectMap')
    if not os.path.exists(Path):
        os.mkdir(Path)
        Path = os.path.join(Path,'elements')
        return Path
    else:
        Path = os.path.join(Path,'elements')
        return Path

class ReadUiObjectMap():
    def __init__(self,driver,UiObjectMap=UiObjectMapPath()):
        self.cf = configparser.RawConfigParser()
        self.UiObjectMap = UiObjectMap
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def find_element(self,section,option):
        self.cf.read(self.UiObjectMap,encoding='utf-8')
        locat = self.cf.get(section,option).split(':')
        if locat:
            locatMethod = locat[0]
            locatExpression = locat[1]
            message = '获取定位元素失败，元素名称：'+ option + '定位方式：'+ locatMethod +\
                '定位表达式：' + locatExpression
            try:
                element = self.wait.until(lambda x: x.find_element(locatMethod,locatExpression))
            except:
                screenShot(self.driver,option)
                log.exception(message)
                raise ('获取定位元素失败')
            else:
                return element
        else:
            raise log.info('部分名称：%s，或者参数名称错误：%s'%(section,option))

    def find_elements(self,section,option):
        self.cf.read(self.UiObjectMap)
        locat = self.cf.get(section,option).split(':')
        if locat:
            locatMethod = locat[0]
            locatExpression = locat[1]
            message = '获取定位元素失败,元素名称: ' + option + ' 定位方式: ' + locatMethod + \
                      ' 定位表达式: ' + locatExpression
            try:
                elements = self.wait.until(lambda x: x.find_elements(locatMethod,locatExpression))
            except:
                screenShot(self.driver,option)
            else:
                return elements
        else:
            raise log.info('部分名称：%s，或者参数名称错误：%s'%(section,option))

    def get_result(self,section,option,text):

        try:
            Element = self.wait.until(lambda x: x.find_element(section,option))
            assert text in Element.text
        except AssertionError:
            screenShot(self.driver,text)
            message = '断言失败， 元素文本: %s，判断文本：%s' %(Element.text,text)
            log.exception(message)
        else:
            return True






