import json
import pymysql

from server.config import SQL_config, DATABASE

conn = pymysql.connect(**SQL_config)
cur = conn.cursor()
# 使用数据库
cur.execute('use %s' % DATABASE)
# 设置编码格式
cur.execute('SET NAMES utf8;')
cur.execute('SET character_set_connection=utf8;')

# def get_data():


if __name__ == "__main__":
    f = open('./config.json', 'r')
    content = f.read()
    config = json.loads(content)
    f.close()
