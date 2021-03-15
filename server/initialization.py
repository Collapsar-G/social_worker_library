# coding: utf-8

# @author: Collapsar-G

# @date: 2021.3.12

# @describe: The file used to initialize the index
import csv
import os

import cchardet as chardet
from config import resources_add_list, SQL_config, DATABASE
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
import json
import pymysql

conn = pymysql.connect(**SQL_config)
cur = conn.cursor()


def get_encoding(filename):
    """
    Returns the file encoding format
    """
    with open(filename, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def load_csv(csv_file_path, table_name, primary_key, database=DATABASE):
    """
    Load csv into mysql
    """
    print("writing %s into table %s" % (csv_file_path, table_name))
    # 打开csv文件
    file = open(csv_file_path, 'r', encoding=get_encoding(csv_file_path))
    # 读取csv文件第一行字段名，创建表
    reader = file.readline()
    b = reader.split(',')
    colum = ''
    # primary_key = ''
    for a in b:
        colum = colum + a + ' varchar(255),'
        # primary_key = primary_key + a + ','
    # colum = colum[:-1]
    # primary_key = primary_key[:-1]
    # 编写sql，create_sql负责创建表，data_sql负责导入数据
    create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum + 'primary key' + '(' + primary_key + ')' + ')' + ' DEFAULT CHARSET=utf8 '
    # create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum +  ')' + ' DEFAULT CHARSET=utf8'
    data_sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' " \
               "IGNORE 1 LINES" % (csv_file_path, table_name)
    print(data_sql)
    # 使用数据库
    cur.execute('use %s' % database)
    # 设置编码格式
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    # 执行create_sql，创建表
    cur.execute(create_sql)
    # 执行data_sql，导入数据
    cur.execute(data_sql)
    conn.commit()
    # 关闭连接
    # conn.close()
    # cur.close()


def data2mysql(root, table_name, primary_key):
    """
    loat all csv to mysql
    :param root:
    :return:
    """
    for fn in traverseFile(root):
        load_csv(fn, table_name, primary_key)


def traverseFile(root):
    """
    return list with all files in root
    """
    file_list = []
    for f in os.listdir(root):
        f_path = root + '/' + f
        if os.path.isfile(f_path):
            file_list.append(f_path)
        else:
            file_list += traverseFile(f_path)
    return file_list


def to_utf8(root):
    """
    return file with encode utf-8
    """
    print("Start encoding file")
    for fn in traverseFile(root):
        encoding = get_encoding(fn)
        if encoding != "UTF-8":
            with open(fn, 'r', encoding=get_encoding(fn), errors='ignore') as f:
                reader = f.read()
            with open(fn, "w", encoding="utf-8") as csvfile:
                csvfile.write(reader)
            print(fn, "successful")
        else:
            print(fn, " don't need to code")


if __name__ == "__main__":
    f = open('./config.json', 'r')
    content = f.read()
    config = json.loads(content)
    f.close()
    for key in resources_add_list.keys():
        to_utf8(resources_add_list[key][0])
        data2mysql(resources_add_list[key][0], key, resources_add_list[key][1])
        config['resources_list'][key][0] = resources_add_list[key][1]
        config['resources_list'][key][0] = resources_add_list[key][2]
    b = json.dumps(config)
    f2 = open('./config.json', 'w')
    f2.write(b)
    f2.close()
    # 关闭连接
    conn.close()
    cur.close()
