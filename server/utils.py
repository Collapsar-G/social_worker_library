# coding: utf-8

# @author: Collapsar-G

# @date: 2021.3.18

# @describe: 社交网络可视化
from io import BytesIO
import base64
import networkx as nx
import simplejson
import json
import matplotlib.pyplot as plt
import pymysql
from config import SQL_config, DATABASE
## 显示中文,及字体设置
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

conn = pymysql.connect(**SQL_config)
cur = conn.cursor()
# 使用数据库
cur.execute('use %s' % DATABASE)
# 设置编码格式
cur.execute('SET NAMES utf8;')
cur.execute('SET character_set_connection=utf8;')

def get_weight(key, value, n):
    f = open('./config.json', 'r')
    content = f.read()
    config = json.loads(content)
    f.close()
    table = "GroupData"
    # print("success")
    SQL = ""
    ls = []
    # print(key,value)
    SQL = "select * from %s where %s= %s " % (table, key, "'"+value+"'")
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
    label2id = {}
    id2data = {}
    ls_label2id = []
    node = 0

    G = nx.Graph()
    G = nx.Graph()
    G.add_node(node)
    label2id[str(key + ":" + value)] = node
    id2data[node] = str(key + ":" + value)
    ls_label2id.append(str(key + ":" + value))
    node += 1
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
                SQL = "select * from %s where %s=%s " % (table, ls[i], "'"+ve+"'")
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
                        if str(ls2[i] + ":" + te) in ls_label2id:
                            # G.add_node(label2id[str(ls2[i] + te)])
                            G.add_edge(label2id[str(ls[i] + ":" + ve)], label2id[str(ls2[i] + ":" + te)])
                        else:
                            G.add_node(node)

                            ls_label2id.append(str(ls2[i] + ":" + te))
                            label2id[str(ls2[i] + ":" + te)] = node
                            id2data[node] = str(ls2[i] + ":" + te)
                            node += 1
                            G.add_edge(label2id[str(ls[i] + ":" + ve)], label2id[str(ls2[i] + ":" + te)])

            # print(temp)
            v = temp[:]
        return {"code": 200, "msg": "successful!", "G": G, "id2data": id2data}
    elif key == "QunNum":
        # SQL = "select * from %s where %s=%s " % (database, key, value)
        ls2 = qqnum_ls * n
        ls = qunnum_ls * n
        v = [value]

        # print(ls)
        for i in range(len(ls)):
            # print(i)
            temp = []
            for ve in v:
                SQL = "select * from %s where %s=%s " % (table, ls[i], "'"+ve+"'")
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
                        if str(ls2[i] + ":" + te) in ls_label2id:
                            # G.add_node(label2id[str(ls2[i] + te)])
                            G.add_edge(label2id[str(ls[i] + ":" + ve)], label2id[str(ls2[i] + ":" + te)])
                        else:
                            G.add_node(node)

                            ls_label2id.append(str(ls2[i] + ":" + te))
                            label2id[str(ls2[i] + ":" + te)] = node
                            id2data[node] = str(ls2[i] + ":" + te)
                            node += 1
                            G.add_edge(label2id[str(ls[i] + ":" + ve)], label2id[str(ls2[i] + ":" + te)])

            # print(temp)
            v = temp[:]
    return {"code": 200, "msg": "successful!", "G": G, "id2data": id2data}


def result2bs64(key, value, n):
    # print(key, value, n)
    result = get_weight(key, value, n)
    if result["code"] == 200:
        G = result["G"]
        pos = nx.spring_layout(G)
        nx.draw(G, pos,  node_size=30, node_color="#ffa502", edge_color="#70a1ff", alpha=1.0,
                font_size=8,
                font_color='#57606f', width=1)
        # plt.show()
        save_file = BytesIO()
        plt.savefig(save_file, format='png')

        G.clear()

        # 转换base64并以utf8格式输出
        save_file_base64 = base64.b64encode(save_file.getvalue()).decode('utf8')
        save_file.close()
        plt.clf()
        return {"code": 200, "msg": "successful!", "id2data": result["id2data"],
                "image": "data:image/png;base64," + str(save_file_base64)}
    else:
        return result