#coding=utf-8

import click
import pandas

infoColor = "blue"
faltColor = "red"
## 这个网站可以生成Ascii 的logo，命令行里显示一个带颜色的logo 还是比较酷哒
## http://patorjk.com/software/taag/#p=display&f=Banner3&t=Eagle 
def printLogo():
    logoAscii = """
########    ###     ######   ##       ######## 
##         ## ##   ##    ##  ##       ##       
##        ##   ##  ##        ##       ##       
######   ##     ## ##   #### ##       ######   
##       ######### ##    ##  ##       ##       
##       ##     ## ##    ##  ##       ##       
######## ##     ##  ######   ######## ######## 
"""
    click.secho(logoAscii,fg="green")
    click.secho("Type: --help for More.",fg=infoColor,underline=True)
    click.secho('CopyRight @2019 ark',fg=infoColor,underline=True)
    click.echo("")

## 使用 pandas 输出数据集对象
def printItems(description,items,**kwargs):
    printInfo(description)
    pandas.set_option('display.max_rows',kwargs.get("max_rows",100))
    df = pandas.DataFrame(items)
    if kwargs.get("col_list",False) != False:
        colList = kwargs.get("col_list").strip().split(",")
        df = df[colList]
    print(df)
    
def printInfo(f,*args):
    print("")
    if len(args) != 0:
        f = f % args
    click.secho(f,fg=infoColor)

def printFalt(f,*args):
    if len(args) != 0:
        f = f % args
    click.secho(f,fg=faltColor)
    exit(1)