---
title: 社工库
copyright: true
tags: 'vue,flask,python,mysql'
categories: 学习笔记
abbrlink: 31081
date: 2021-03-17 15:43:34
comments: true
author: Collapsar-G
---

# 社工库

## 项目结构



## 完成过程

> 在完成上参考了《“系统安全”课程项目：一个实用社工库的建设》，加入了一些自己的理解。

### 数据初始化

#### 导出为csv格式

由于拿到手的数据是SQL Server的MDF文件，在解压后多达90G，查询起来有诸多不便，所以将数据统一导出为 .csv 格式，方便进行下一步的项目搭建。

> .csv文件用 `\r`做字段间分隔符，用`\r\n`做行分隔符。在一开始的时候由于考虑不够周全，所以使用`,`做分隔符，结果发现在昵称、群名字、群简介等数据中有`,`的存在会使.csv格式出错。在检查确认文件中不会出现`\r\n`后采用了新的分割方式。（QQ群简介的换行是用`<br>`来实现）

#### 统一csv文件为 UTF-8 编码

由于拿到手的文件编码方式不统一，存在很多乱码，所以需要统一文件格式，决定将文件编码统一为**UTF-8**。但是对每一个csv文件单独设置编码有些麻烦，所以就查询资料发现了**chardet**库，可以获取文件的编码方式，但是在实际使用过程中会发现，这个库识别编码速度奇慢，而且有些文件识别不出来。

> 参考资料：[chardet库：识别文件的编码格式](https://zhuanlan.zhihu.com/p/27188439)

继续查资料，发现了**cchardet**这个库，可以更快更准确地获得文件的编码方式，所以换用**cchardet**来获取文件编码，代码如下：

```python
def get_encoding(filename):
    """
    Returns the file encoding format
    """
    with open(filename, 'rb') as f:
        print(chardet.detect(f.read()))
        return chardet.detect(f.read())['encoding']
    
"""
输出：{'encoding': 'UTF-8', 'confidence': 0.9900000095367432}
"""
```

这样就可以通过遍历文件目录下的所有文件并重新读写来实现目录下所有文件的重新编码：

遍历文件目录代码如下：

```python
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
```

文件统一编码为UTF-8代码如下：

```python
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
```

> 在编码UTF-8时还出现了一些小状况：
>
> ![image-20210317192630802](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210317192630.png)
>
> 会出现一些无法读取的字符（未知原因，大部分编码都是正常的）所以在查询后发现，可以在打开文件时加上一条`errors='ignore'`，如上面代码中所写，这样忽视掉极少数异常编码后终于可以正常运行了。

#### csv文件放入数据库

由于csv文件将同一数据分为了若干表，并且建索引有些繁琐，所以决定批量导入MySQL来建立索引。如果一条一条读写的话速度有些慢，经过查询发现MySQL有语句`LOAD DATA`可以导入csv文件。

在导入过程中，一开始没有设置主键，所以导入速度很快，但是有个缺点是重复数据可以频繁输入，同时查询时速度特别慢，所以决定添加主键。为了之后前端方便，所以将每一个数据表的添加信息放入`config.py`文件中，在添加到数据库完成后写入`config.json`文件,具体代码如下：

```python
resources_add_list = {"GroupData": ["./DATA/GroupData", "QQNum,QunNum", "id,QQNum,Nick,Age,Gender,Auth,QunNum"],
                      "QunInfo": ["./DATA//QunInfo", "QunNum", "id,QunNum,MastQQ,CreateDate,Title,Class,QunText"]}
```

> `resources_add_list`只有要新附加到数据库中的信息，其中，`"GroupData"、"QunInfo"`是数据表的名字，对应列表中第一项是文件目录，第二项是主键（同时也是前端可用于查询的项），第三项是数据表的不同列。

数据写入数据库代码如下：

```python
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
    data_sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY '\\r' LINES TERMINATED BY '\\r\\n' " \
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
```



> 数据初始化完整代码：[点击跳转](https://github.com/Collapsar-G/social_worker_library/blob/main/server/initialization.py)

****

### 后端api搭建

> 后端使用flask框架搭建，计划搭建三个接口：

#### 测试后端连接

**功能描述**：在用户进入页面初始化时掉用，检测api是否正常

**请求链接**：`/s/`

**请求方式**：POST

**参数详情：**无

**返回参数：**

| 参数 |  类型  |                说明                |
| :--: | :----: | :--------------------------------: |
| code | number | 状态码，200表示正常，500服务器异常 |
| msg  | string |              提示信息              |

示例：

```json
{
  "code": 200,
  "msg": "success!"
}
```

#### 获取项目参数

**功能描述：**返回项目的完整参数

**请求链接**：`/s/config/`

**请求方式**：POST

**参数详情：**无

**返回参数：**

|  参数  |  类型  |                      说明                      |
| :----: | :----: | :--------------------------------------------: |
|  code  | number | 状态码，200表示正常，400API异常，500服务器异常 |
|  msg   | string |                    提示信息                    |
| config |  json  |                  项目参数文件                  |

示例：

```json
{
    "code": 200,
    "config": {
        "GroupData": {
            "result_class": {
                "Age": null,
                "Auth": null,
                "Gender": null,
                "Nick": null,
                "QQNum": null,
                "QunNum": null,
                "id": null
            },
            "search_key": {
                "QQNum": "",
                "QunNum": ""
            }
        },
        "QunInfo": {
            "result_class": {
                "Class": null,
                "CreateDate": null,
                "MastQQ": null,
                "QunNum": null,
                "QunText": null,
                "Title": null,
                "id": null
            },
            "search_key": {
                "QunNum": ""
            }
        }
    },
    "msg": "Success!"
}
```

#### 查询接口

**功能描述：**返回项目的完整参数

**请求链接**：`/s/config/`

**请求方式**：POST

**参数详情：**

|   参数   |  类型  |                说明                |
| :------: | :----: | :--------------------------------: |
| database | string |             数据表名称             |
| 其它参数 | string | database数据表对应的主键中任意几个 |

```json
{
    "database":"QunInfo",
    "QunNum":"1000000"
}
```



**返回参数：**

|    参数    |  类型  |                      说明                      |
| :--------: | :----: | :--------------------------------------------: |
|    code    | number | 状态码，200表示正常，400API异常，500服务器异常 |
|    msg     | string |                    提示信息                    |
|    data    |  json  |                 查找的对应结果                 |
| class_data |  json  |          data中每一项数据对应的class           |

示例：

```json
{
    "class_data": [
        "id",
        "QunNum",
        "MastQQ",
        "CreateDate",
        "Title",
        "Class",
        "QunText"
    ],
    "code": 200,
    "data": [
        [
            "355462",
            "1000000",
            "62",
            "2005-01-29",
            "北京怀柔欧曼重卡",
            "2977",
            "☆喜歡..や偷看..ゞě.伱的臉ぐ☆<br/>┊ず..帶着ぺ股.ふ.香甜的氣味..ヅ┊"
        ]
    ],
    "msg": "success"
}
```

### 前端搭建

前端使用vue+Vuetify搭建，本来打算表单可以利用config接口的信息动态生成，每次添加数据不用改动前端，但是在实现过程中遇到了一些问题，索性放弃。

#### 数据查询界面

![image-20210317220313786](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210317220313.png)

<center>初始化界面（网络连接断开时）</center>

![image-20210317220443729](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210317220443.png)<center>正常初始化</center>

![image-20210317220518961](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210317220519.png)

<center>查询结果展示</center>

![image-20210317220558673](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210317220558.png)

<center>未查询到结果</center>

****

### 社交网络可视化界面

> 暂未实现

#### 可视化后端

在一开始打算做动态的可视化，在搜索社交网络可视化过程中，发现一个名为`netwulf`的python库，效果如下：

```python
import networkx as nx
from netwulf import visualize

G = nx.barabasi_albert_graph(100,m=1)
visualize(G)
```

测试效果如下：

![Video_20210318_102322_895](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318195301.gif)

效果不太理想，所以改用`networkx`库来生成静态图像：

![image-20210318172510380](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318172510.png)

<center>效果图(只迭代查询一次)</center>

具体代码如下：

```python
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
    print(SQL)
    try:
        result = cur.execute(SQL)
        print(result)
        data = cur.fetchall()
        print(data)
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
                font_color='#6DB1BF', width=2)
        # plt.show()
        save_file = BytesIO()
        plt.savefig(save_file, format='png')

        # 转换base64并以utf8格式输出
        save_file_base64 = base64.b64encode(save_file.getvalue()).decode('utf8')
        return {"code": 200, "msg": "successful!", "id2data": result["id2data"],
                "image": "data:image/png;base64," + str(save_file_base64)}
    else:
        return result
```

参考资料：[Networkx绘图和整理功能的参数,networkx,画图,函数参数](https://www.pythonf.cn/read/137465)

实现结果：

![image-20210318202415299](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318202415.png)

![image-20210318202538508](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318202538.png)

![image-20210318202626563](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318202626.png)

![image-20210318203004384](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318203004.png)

![image-20210318203017762](https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210318203017.png)

### Docker部署

> windows下Docker安装出现了bug，暂时还没有配置好Docker环境，暂未实现。

## 总结

基本上实现了数据的自动插入数据库，自动建立索引，在插入新数据时，在`config.py`文件中输入要插入的相关参数，后使用`initialization.py`文件可以实现自动化加载到数据库。前端UI中，只需添加几个数据就可以实现前端界面的更改（社交网络可视化部分改动可能较多）。



