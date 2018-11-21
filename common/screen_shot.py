import time,os
from logger import Logger

log = Logger(logName='screen_shot').get_log()

def currentDate():
    today = time.strftime('%Y-%m-%d',time.localtime())
    return today

def currentTime():
    currentTime = time.strftime('%H-%M-%S',time.localtime())
    return currentTime

def createDir():
    currentPath = os.path.dirname(os.path.dirname(__file__))
    currentPath = os.path.join(currentPath,'testScreenShot')
    if not  os.path.exists(currentPath):
        os.mkdir(currentPath)
        today = currentDate()
        todayDir = os.path.join(currentPath,today)
        if not os.path.exists(todayDir):
            os.mkdir(todayDir)
            return todayDir
        else:
            return todayDir
    else:
        today = currentDate()
        todayDir = os.path.join(currentPath, today)
        if not os.path.exists(todayDir):
            os.mkdir(todayDir)
            return todayDir
        else:
            return todayDir

def screenShot(driver,pictureName):
    try:
        picDir = createDir()
        picPath = os.path.join(picDir,currentTime()+'-'+str(pictureName)+'.png')
        driver.get_screenshot_as_file(picPath)
    except:
        log.info('截图保存失败')
    else:
        log.info('截图保存成功'+ picPath)

