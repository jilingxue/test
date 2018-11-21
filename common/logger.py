import logging,time,os
from logging.handlers import RotatingFileHandler

def logFile():
    data = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    logFile = os.path.dirname(os.path.dirname(__file__))
    logFile = os.path.join(logFile,'log')
    try:
        if not os.path.exists(logFile):
            os.mkdir(logFile)
        else:
            pass
        fileName = data + '.log'
        logFile = os.path.join(logFile, fileName)
        return logFile
    except:
        print('日志文件创建失败')

class Logger():
    def __init__(self,logName,logLevel='INFO',logFile=logFile()):
        self.log = logging.getLogger(logName)
        self.log.setLevel(logLevel)
        self.fh = logging.FileHandler(logFile)
        self.fh.setLevel(logLevel)
        format = ('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        self.fh = RotatingFileHandler(logFile,mode='a',maxBytes=1024*1024*50,backupCount=20,encoding='utf-8')
        self.fh.setFormatter(logging.Formatter(format))
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logLevel)
        self.ch.setFormatter(logging.Formatter(format))
        self.log.addHandler(self.fh)
        self.log.addHandler(self.ch)

    def get_log(self):
        return self.log

# log = Logger(logName='test').get_log()
# log.info('1233333213')