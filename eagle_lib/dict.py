#coding=utf-8

## 多key 获取对应的dict 参数, 不存在为False
def dictMget(dict,*args):
    r = []
    for n in args:
        r.append(dict.get(n,False))
    return r


if __name__ == '__main__':
    params = {
        "table":"info",
        "init_fields":"t,id",
        "init_values":"1,2",
        "v":True,
        "action":"table",
        "def":"insert",
        "upstr":False,
        "where":False,
        "max_rows":None,
        "col_list":False,
        "eagle_root":"."
    }

    tableName,init_fields,init_values = dictMget(params,"table","init_fields","init_values")
    print(tableName,init_fields)