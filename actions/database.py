#coding=utf-8

import eagle_lib.database as database
import eagle_lib.printex as printex

def list(*args,**kwargs):
    sql = "show databases;"
    items = database.runSql(sql)
    printex.printItems("Database List: ",items,**kwargs)
