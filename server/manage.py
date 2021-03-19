# coding: utf-8

# @author: Collapsar-G

# @date: 2021.3.12

# @describe: 项目入口

from app import create_app
from flask_script import Manager
from flask_cors import CORS

app = create_app('pro')
CORS(app)
manager = Manager(app)

"""

python manage.py runserver --host 127.0.0.1 --port 3268  运行服务器
"""

if __name__ == '__main__':
    manager.run()
