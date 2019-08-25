#coding=utf-8

import eagle_lib.database as database
import eagle_lib.printex as printex
import eagle_lib.dict as dictEx

def list(*args,**kwargs):
    sql = "show tables;"
    items = database.runSql(sql)
    if len(items) == 0 :
        printex.printInfo("No Table Found.")
    else :
        printex.printItems("Table List Current Database : ",items,**kwargs)

# ./eagle.py table select -table info -v -where "t = 3" 
def select(*args,**kwargs):
    tableName,where = dictEx.dictMget(kwargs,"table","where")
    if tableName == False:
        printex.printFalt("Table Select Must Have -table field : ")

    sql = "select * from %s " %(tableName)
    if where != False:
        sql = sql + " where " + where
    items = database.runSql(sql)
    if len(items) == 0:
         printex.printInfo("No Items Found.")
    else :
        selectDescriptionString = " %s  Items : \n" % (sql)
        printex.printItems(selectDescriptionString,items,**kwargs)

def delete(*args,**kwargs):
    tableName,where = dictEx.dictMget(kwargs,"table","where")
    if tableName == False or where == False :
        printex.printFalt("Delete Rows Must Have -table and -where field : ")
    sql = "delete from %s where %s " %(tableName,where)
    affectRows = database.runSql(sql,commit=True)
    printex.printInfo("%d Rows Deleted . ",affectRows)

def update(*args,**kwargs):
    tableName,where,upString = dictEx.dictMget(kwargs,"table","where","upstr")
    if tableName == False or where == False or upString == False:
        printex.printFalt("Updaete Rows Must Have -table -where -upstr field : ")
    sql = "update  %s set %s where %s " %(tableName,upString,where)
    affectRows = database.runSql(sql,commit=True)
    printex.printInfo("%d Rows Updated . ",affectRows)

def insert(*args,**kwargs):
    tableName,init_fields,init_values = dictEx.dictMget(kwargs,"table","init_fields","init_values")
    if tableName == False or init_fields == False or init_values == False:
        printex.printFalt("Insert Sql Must Have -talbe -init_fields -init_values Field  \n But , %s , %s , %s",tableName,init_fields,init_values)
    sql = "insert  %s (%s) values (%s) " %(tableName,init_fields,init_values)
    affectRows = database.runSql(sql,commit=True)
    printex.printInfo("%d Rows Inserted . ",affectRows)

def desc(*args,**kwargs):
    table = kwargs.get("table")
    sql = "desc %s" % (table)
    items = database.runSql(sql)
    descText = "Table %s description" % (table)
    printex.printItems(descText,items,**kwargs)  