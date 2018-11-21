import configparser
from logger import Logger
import os


log = Logger(logName='read_config').get_log()
def configPath():
    path = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(path,'config')
    path = os.path.join(path,'basicConfig')
    return path

def readConfig(section,option):
    try:
        conf = configparser.RawConfigParser()
        conf.read(configPath(),encoding='utf-8')
        configdata = conf.get(section,option)
        return configdata
    except:
        message = '获取配置文件失败：'+ configPath() + ' section: '+ section + ' option: ' + option
        log.info(message)

#print(readConfig('ur','student'))