# coding: utf-8

# @author: Collapsar-G

# @date: 2021.3.18

# @describe: 社交网络可视化-使用AntV
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


def get_json(key, value, n):
    f = open('./config.json', 'r')
    content = f.read()
    config = json.loads(content)
    f.close()
    table = "GroupData"
    # print("success")
    SQL = ""
    ls = []
    print(key, value)
    SQL = "select * from %s where %s= %s " % (table, key, "'" + value + "'")
    print(SQL)
    try:
        result = cur.execute(SQL)
        # print(result)
        data = cur.fetchall()
        # print(data)
        conn.commit()

    except():
        return {"code": 400, "msg": "数据读取错误"}
    if result == 0:
        return {"code": 300, "msg": "未查询到相关数据"}
    qqnum_ls = ["QQNum", "QunNum"]
    qunnum_ls = ["QunNum", "QQNum"]
    ls_label = []
    fill = {"QQNum": '#18ffff', "QunNum": '#ff4081'}
    result_data = {"nodes": [], "edges": []}
    opacity = 0.8,
    type = {"QQNum": 'circle', "QunNum": 'rect'}
    temp_node = {"id": str(key + ":" + value), "key": str(key), "value": str(value), "label": str(key + ":" + value),
                 "type": type[key], "style": {"fill": '#ffff00', "opacity": opacity, },
                 "labelCfg": {"positions": 'center'}}
    result_data["nodes"].append(temp_node)
    ls_label.append(str(key + ":" + value))

    if key == "QQNum":
        # SQL = "select * from %s where %s=%s " % (database, key, value)
        ls = qqnum_ls * n
        ls2 = qunnum_ls * n
        v = [value]

        # print(ls)
        for i in range(len(ls)):
            # print(i)
            temp = []
            for ve in v:
                SQL = "select * from %s where %s=%s " % (table, ls[i], "'" + ve + "'")
                try:
                    result = cur.execute(SQL)
                    data = cur.fetchall()
                    conn.commit()
                except():
                    return {"code": 400, "msg": "数据读取错误"}
                if result == 0:
                    continue
                else:
                    # print(data)
                    for h in data:
                        te = h[list(config["resources_list"][table][1].split(sep=',', maxsplit=-1)).index(ls2[i])]
                        temp.append(te)

                        if str(ls2[i] + ":" + te) in ls_label:
                            # G.add_node(label2id[str(ls2[i] + te)])
                            temp_edge = {"source": str(ls[i] + ":" + ve), "target": str(ls2[i] + ":" + te), "value": 1}
                            result_data["edges"].append(temp_edge)
                        else:
                            temp_node = {"id": str(ls2[i] + ":" + te), "key": str(key), "value": str(value),
                                         "type": type[ls2[i]], "style": {"fill": fill[ls2[i]], "opacity": opacity, },
                                         "label": str(ls2[i] + ":" + te), "labelCfg": {"positions": 'center'}}
                            result_data["nodes"].append(temp_node)

                            ls_label.append(str(ls2[i] + ":" + te))
                            temp_edge = {"source": str(ls[i] + ":" + ve), "target": str(ls2[i] + ":" + te), "value": 1}
                            result_data["edges"].append(temp_edge)

            # print(temp)
            v = temp[:]
        return {"code": 200, "msg": "successful!", "result_data": result_data}
    elif key == "QunNum":
        # SQL = "select * from %s where %s=%s " % (database, key, value)
        ls2 = qqnum_ls * n
        ls1 = qunnum_ls * n
        v = [value]

        # print(ls)
        for i in range(len(ls)):
            # print(i)
            temp = []
            for ve in v:
                SQL = "select * from %s where %s=%s " % (table, ls[i], "'" + ve + "'")
                try:
                    result = cur.execute(SQL)
                    data = cur.fetchall()
                    conn.commit()
                except():
                    return {"code": 400, "msg": "数据读取错误"}
                if result == 0:
                    continue
                else:
                    # print(data)
                    for h in data:
                        te = h[list(config["resources_list"][table][1].split(sep=',', maxsplit=-1)).index(ls2[i])]
                        temp.append(te)

                        if str(ls2[i] + ":" + te) in ls_label:
                            # G.add_node(label2id[str(ls2[i] + te)])
                            temp_edge = {"source": str(ls[i] + ":" + ve), "target": str(ls2[i] + ":" + te), "value": 1}
                            result_data["edges"].append(temp_edge)
                        else:
                            temp_node = {"id": str(ls2[i] + ":" + te), "key": str(key), "value": str(value),
                                         "type": type[ls2[i]], "style": {"fill": fill[ls2[i]], "opacity": opacity, },
                                         "label": str(ls2[i] + ":" + te), "labelCfg": {"positions": 'center'}}
                            result_data["nodes"].append(temp_node)

                            ls_label.append(str(ls2[i] + ":" + te))
                            temp_edge = {"source": str(ls[i] + ":" + ve), "target": str(ls2[i] + ":" + te), "value": 1}
                            result_data["edges"].append(temp_edge)

            # print(temp)
            v = temp[:]
        return {"code": 200, "msg": "successful!", "result_data": result_data}