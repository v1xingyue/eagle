#coding=utf-8

#coding=utf-8

import pymysql
import logging

def dbConnection():
    con = pymysql.connect(
        host='172.16.18.135',
        port=3306,
        user='eagle',
        password='123',
        db='eagle',
        charset='utf8'
    )
    return con

"""
usage : database.runSql(" select * from hello where name = %s ",'ark')
"""
def runSql(sql,*args,**kwargs):
    logging.debug("run sql : %s with args:%s  kwargs: %s",sql,args,kwargs)
    con = dbConnection()
    commit = kwargs.get('commit',False)
    params = kwargs.get('params',args)
    cursor = con.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql,args=params)

    if commit :
        con.commit()
        con.close()
        return con.affected_rows()
        
    con.close()
    return cursor.fetchall()