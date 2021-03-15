from flask import Flask
from config import config_map


def create_app(name):
    """
    创建app实例
    @param name:配置环境的名称，可选 dev， pro
    @return: app实例
    """
    app = Flask(__name__, static_folder='../static')

    # 配置
    app.config.from_object(config_map[name])

    # 接口

    from app.api.search import search

    app.register_blueprint(search, url_prefix='/s')

    return app
