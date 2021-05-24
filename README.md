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

前端：vue

后端：python-flask

数据库：mysql

## 项目结构

```
social_worker_library
 ├── server  //后端服务
 │   ├── app
 │   │   ├── api   //后端api
 │   │   │   ├── search.py    
 │   │   │   ├── visualization.py
 │   │   │   ├── __init__.py
 │   │   ├── __init__.py
 │   ├── config.json  //参数文件
 │   ├── config.py     //参数文件
 │   ├── DATA      //csv数据目录
 │   ├── initialization.py   //csv数据导入mysql数据库脚本
 │   ├── manage.py     //后端项目入口
 │   ├── requirements.txt
 │   ├── test.py
 │   ├── utils.py
 │   ├── utils2.py
 └── social-worker-library   //前端
```

## 使用

### 数据导入

csv数据文件放在`DATA`目录下，修改`config.py`文件参数，执行：

```bash
cd server
python initialization.py
```

将数据导入mysql数据库中。

### 后端服务

执行：

```bash
cd server
python manage.py runserver --host 127.0.0.1 --port 3268
```

### 前端

执行：

```bash
cd social-worker-library
npm install 
npm run serve
```



## 前端效果

<video id="video" controls="" preload="none" poster="https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210323115310.png">
      <source id="mkv" src="https://cloud.collapsar.online/2021-03-23%2011-48-38.mkv" type="video/mkv">
      </video>

