#!/Users/xingyue/eagle/env/bin/python -u
#coding=utf-8

import click
import logging
import eagle_lib.router as router
from eagle_lib.eagle import EagleInstance
import os

@click.command()
@click.option("-v",is_flag=True,help="Print Debug Message.")    #用来标记详细的日志输出
@click.option("-table",help="Table Name You Want To Operate.",default=False)
@click.option("-upstr",help="Update String In Update Sql",default=False)
@click.option("-init_values",help="Insert Values String ",default=False)
@click.option("-init_fields",help="Init Fields in insert Sql",default=False)
@click.option("-where",help="Where String Pass To Sql , Select , Update , Delete",default=False)
@click.option("-max_rows",help="Max Rows Shown By Pandas Dataframe",type=click.INT)
@click.option("-col_list",help="Columns List Shown By Pandas Dataframe, Default Show All.",default=False)
@click.argument("action",default="help",type=click.Choice(router.actions()) )
@click.argument("def",default="index")
def doCommand(*args,**kwargs):
    EagleInstance.setCliArgs(**kwargs)
    EagleInstance.logInit()
    logging.debug(" eagle.py run with arguments : %s , %s",args,kwargs)
    router.routeCli(*args,**kwargs)

if __name__ == '__main__':
    run_root = os.path.dirname(__file__)
    EagleInstance.setRoot(run_root)
    doCommand()