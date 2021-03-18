import json
from flask import Blueprint, request, jsonify
import networkx as nx
import matplotlib.pyplot as plt
import pymysql
from io import BytesIO
import base64
from config import SQL_config, DATABASE
import simplejson

# SQL_config = {'host': 'localhost',
#               'port': 3306,
#               'user': 'root',
#               'passwd': '8520',
#               'charset': 'utf8mb4',
#               'local_infile': 1
#               }
# DATABASE = 'ssdata'

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

visualization = Blueprint('visualization', __name__)


@visualization.route('/visualization/', methods=['POST'])
def visualizationdata():
    """
        查询接口
        @param content:数据的查询
        @return code(200=正常返回，400=错误),data
    """
    try:
        param = request.get_json()
        key = param.get('key')
        value = param.get('value')
    except:
        return jsonify(code=400, msg='参数错误')
    if key not in ["QQNum", "QunNum"]:
        return jsonify(code=400, msg='参数错误')
    result = result2bs64(key, value, 1)
    if result["code"] == 400:
        return jsonify(code=400, msg='参数错误')
    elif result["code"] == 200:
        return jsonify(code=200, msg='successful!', image=result["image"], id2data=result["id2data"])
    elif result["code"] == 300:
        return jsonify(code=300, msg="未查询到相关数据")
    else:
        return jsonify(code=400, msg='未知错误')


def get_weight(key, value, n):
    f = open('./config.json', 'r')
    content = f.read()
    config = json.loads(content)
    f.close()
    table = "GroupData"
    # print("success")
    SQL = ""
    ls = []
    SQL = "select * from %s where %s= %s " % (table, key, "'"+value+"'")
    # print(SQL)
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
    if key == "QunNum":
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


def result2bs64(key, value, n=1):
    print(key, value, n)
    result = get_weight("QQNum", value, 1)
    if result["code"] == 200:
        G = result["G"]
        pos = nx.spring_layout(G, iterations=1000)
        nx.draw(G, pos, with_labels=True, node_size=20, node_color="#F39A9D", edge_color="#FFEAEC", alpha=1.0,
                font_size=8,
                font_color='#6DB1BF', width=1)
        # plt.show()
        save_file = BytesIO()
        plt.savefig(save_file, format='png')

        # 转换base64并以utf8格式输出
        save_file_base64 = base64.b64encode(save_file.getvalue()).decode('utf8')
        return {"code": 200, "msg": "successful!", "id2data": result["id2data"],
                "image": "data:image/png;base64," + str(save_file_base64)}
    else:
        return result


if __name__ == "__main__":
    # result2bs64("QQNum", "100000", 1)
    print(result2bs64("QunNum", "1000000", 1))
