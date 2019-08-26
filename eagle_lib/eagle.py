#coding=utf-8

import logging

class Eagle:

    def __init__(self):
        self.Root = ""
        self.CliArgs = {}
        self.ActionDir = self.Root

    def setRoot(self,root):
        self.Root = root
        self.ActionDir = self.Root + "/actions/"

    def setCliArgs(self,**kwargs):
        self.CliArgs = kwargs

    def getCliArg(self,name,default=""):
        return self.CliArgs.get(name,default)

    def logInit(self):
        logFormat = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        dateFormat = '%a, %d %b %Y %H:%M:%S'
        logLevel = logging.INFO
        if self.CliArgs.get("v"):
            logLevel = logging.DEBUG
        logging.basicConfig(level=logLevel,format=logFormat,datefmt=dateFormat)

    def actionFilePath(self,actionName):
        return self.ActionDir + "%s.py" % (actionName)

EagleInstance = Eagle()
