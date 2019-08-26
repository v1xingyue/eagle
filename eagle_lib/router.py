#coding=utf-8
import logging
import importlib
import os
from eagle_lib.eagle import EagleInstance

def routeCli():
    logging.debug("route request with params : %s ， %s",args,kwargs)
    actionName = EagleInstance.getCliArg("action")
    defName = EagleInstance.getCliArg("def")
    actionFilePath = EagleInstance.actionFilePath(actionName)
    if os.path.isfile(actionFilePath):
        m = importlib.import_module("actions.%s" % (actionName))
        if not hasattr(m,defName):
            logging.error("Action File %s, def Entry %s Does Not Exist.",actionFilePath,defName) 
        else:
            defEntry = getattr(m,defName)
            defEntry(m,**EagleInstance.CliArgs)
            print("")
    else:
        logging.error("No Action File Found : %s",actionFilePath)
    
def actions(*args,**kwargs):
    actionDir = EagleInstance.ActionDir
    actionFiles = os.listdir(actionDir)
    returnActions = []
    for action in actionFiles:
        if action != "__init__.py" and action != "__pycache__" :
            actionName = action[0:-3]
            returnActions.append(actionName)
    return returnActions