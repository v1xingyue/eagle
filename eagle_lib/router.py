#coding=utf-8
import logging
import importlib
import os

# 根据kwargs 中的action,def 参数 路由请求
def routeCli(*args,**kwargs):
    logging.debug("route request with params : %s ， %s",args,kwargs)
    eagle_root = kwargs.get("eagle_root")
    actionName = kwargs.get("action")
    defName = kwargs.get("def")
    actionFilePath = "%s/actions/%s.py" % (eagle_root,actionName)
    if os.path.isfile(actionFilePath):
        m = importlib.import_module("actions.%s" % (actionName))
        if not hasattr(m,defName):
            logging.error("Action File %s, def Entry %s Does Not Exist.",actionFilePath,defName) 
        else:
            defEntry = getattr(m,defName)
            defEntry(m,*args,**kwargs)
            print("")
    else:
        logging.error("No Action File Found : %s",actionFilePath)
    
def actions(*args,**kwargs):
    actionDir = kwargs.get("eagle_root") + "/actions/"
    actionFiles = os.listdir(actionDir)
    returnActions = []
    for action in actionFiles:
        if action != "__init__.py" and action != "__pycache__" :
            actionName = action[0:-3]
            returnActions.append(actionName)
    return returnActions