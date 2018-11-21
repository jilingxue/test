import os,time

def resultFile(fileName):
    filePath = os.path.dirname(os.path.dirname(__file__))
    filePath = os.path.join(filePath,'resultFile')
    if not os.path.exists(filePath):
        os.mkdir(filePath)
        resultFilePath = os.path.join(filePath, fileName)
        return resultFilePath
    else:
        resultFilePath = os.path.join(filePath, fileName)
        return resultFilePath
#resultFile('123.txt')

def write(file_name,content,type=''):
    file = resultFile(file_name)
    tmp_type = 'w'
    if len(type.strip()) > 0:
        tmp_type = type
    wf = open(file,tmp_type,encoding='utf-8')
    wf.write(content)
    wf.close()

def read(file_name,type='r'):
    file = resultFile(file_name)
    wf = open(file,type,encoding='utf-8')
    content = wf.read()
    wf.close()
    return content

