#!/Users/xingyue/eagle/env/bin/python -u
#coding=utf-8

import click
import logging
import eagle_lib.router as router
import os

eagle_root = os.path.dirname(__file__)

# 初始化日志基本输出级别
def logInitConfig(**kwargs):
    logFormat = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    dateFormat = '%a, %d %b %Y %H:%M:%S'
    logLevel = logging.INFO
    if kwargs.get("v"):
        logLevel = logging.DEBUG
    logging.basicConfig(level=logLevel,format=logFormat,datefmt=dateFormat)

@click.command()
@click.option("-v",is_flag=True,help="Print Debug Message.")    #用来标记详细的日志输出
@click.option("-table",help="Table Name You Want To Operate.",default=False)
@click.option("-upstr",help="Update String In Update Sql",default=False)
@click.option("-init_values",help="Insert Values String ",default=False)
@click.option("-init_fields",help="Init Fields in insert Sql",default=False)
@click.option("-where",help="Where String Pass To Sql , Select , Update , Delete",default=False)
@click.option("-max_rows",help="Max Rows Shown By Pandas Dataframe",type=click.INT)
@click.option("-col_list",help="Columns List Shown By Pandas Dataframe, Default Show All.",default=False)
@click.argument("action",default="help",type=click.Choice(router.actions(eagle_root=eagle_root)) )
@click.argument("def",default="index")
def doCommand(*args,**kwargs):
    logInitConfig(**kwargs)
    logging.debug(" eagle.py run with arguments : %s , %s",args,kwargs)
    kwargs["eagle_root"] = eagle_root
    router.routeCli(*args,**kwargs)

if __name__ == '__main__':
    doCommand()