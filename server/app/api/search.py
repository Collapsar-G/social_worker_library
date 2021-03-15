# coding: utf-8

# @author: Collapsar-G

# @date: 2021.3.12

# @describe: 查询api

import os
import time
import traceback

from flask import Blueprint, request, jsonify, url_for, session

import json
import pymysql

from config import SQL_config, DATABASE

conn = pymysql.connect(**SQL_config)
cur = conn.cursor()
# 使用数据库
cur.execute('use %s' % DATABASE)
# 设置编码格式
cur.execute('SET NAMES utf8;')
cur.execute('SET character_set_connection=utf8;')

# def get_data():


search = Blueprint('search', __name__)


@search.route('/')
def test():
    return "测试成功"


@search.route('/config/', methods=['POST'])
def get_config():
    try:
        f = open('./config.json', 'r')
        content = f.read()
        config = json.loads(content)
        f.close()
    except():
        return jsonify(code='400', msg='服务器连接错误！！！')
    resources_list = {}
    for key in config["resources_list"]:
        resources_list[key] = {}
        resources_list[key]["search_key"] = list(config["resources_list"][key][0].split(sep=',', maxsplit=-1))
        resources_list[key]["result_class"] = list(config["resources_list"][key][1].split(sep=',', maxsplit=-1))
    return jsonify(code='200', msg='Success!', config=resources_list)


@search.route('/search/', methods=['POST'])
def searchdata():
    """
        查询接口
        @param content:数据的查询
        @return code(200=正常返回，400=错误),data
    """
    try:
        param = request.get_json()
        database = param.get('database')
        f = open('./config.json', 'r')
        content = f.read()
        config = json.loads(content)
        f.close()
        content = {}
        if database not in config["resources_list"]:
            return jsonify(code=400, msg='未找到指定数据源')
        else:
            class_data = list(config["resources_list"][database][1].split(sep=',', maxsplit=-1))
            for index in list(config["resources_list"][database][0].split(sep=',', maxsplit=-1)):
                print("!!!!!!!!!!!!!!!!!!!!!!!!", index)
                try:

                    temp = param.get(index)
                except():
                    continue
                if temp is not None:
                    content[index] = temp

            if not content:
                return jsonify(code=400, msg='请正确输入参数')
            else:
                sql = "select * from %s where " % (database)
                for i in range(len(content) - 1):
                    key = list(content.keys())[i]
                    # if content[key] is not None:
                    sql += str(key) + '=' + "'" + str(content[key]) + "'" + " and "
                key = list(content.keys())[len(content) - 1]
                sql += str(key) + '=' + "'" + str(content[key]) + "'"
                print(sql)
                try:
                    print(sql)
                    result = cur.execute(sql)
                    data = cur.fetchall()
                    conn.commit()
                except():
                    return jsonify(code=400, msg="数据读取错误", data=sql)
                if result == 0:
                    return jsonify(code=200, msg="恭喜您，未查询到您的数据！")
                else:
                    print(data)
                    return jsonify(code=200, msg="success", data=data, class_data=class_data)
    except():
        return jsonify(code=400, msg="未知错误")
