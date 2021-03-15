# coding: utf-8

# @author: Collapsar-G

# @date: 2021.3.12

# @describe: Project parameters

resources_add_list = {"GroupData": ["./DATA/GroupData", "QQNum,QunNum", "id,QQNum,Nick,Age,Gender,Auth,QunNum"],
                      "QunInfo": ["./DATA//QunInfo", "QunNum", "id,QunNum,MastQQ,CreateDate,Title,Class,QunText"]}

SQL_config = {'host': 'localhost',
              'port': 3306,
              'user': 'root',
              'passwd': '****',
              'charset': 'utf8mb4',
              'local_infile': 1
              }
DATABASE = 'ssdata'


class DevelopmentConfig():
    """开发者环境配置"""
    DEBUG = True


class ProductionConfig():
    """实际生产环境配置"""
    pass


config_map = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig
}
