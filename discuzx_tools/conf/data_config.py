# !usr/bin/env python
# coding: utf-8

"""任务相关参数的配置.
"""

import functools

import pymongo
from autoloads import ModelHelper
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from discuzx_tools.conf.config import config

echo = False
pool_recycle = 60

forum_engine = create_engine(config.FORUM_DATA_DSN, echo=echo, pool_recycle=pool_recycle)
robot_engine = create_engine(config.ROBOT_DATA_DSN, echo=echo, pool_recycle=pool_recycle)

forum_session = scoped_session(sessionmaker(bind=forum_engine))()
robot_session = scoped_session(sessionmaker(bind=robot_engine))()
Base = declarative_base()

if config.cache_user and config.cache_password:
    cache_host = "mongodb://%s:%s@%s:%s" % (
        config.cache_user, config.cache_password, config.cache_host, config.cache_port)

cache_option = {
    'host': config.cache_host,
    'port': config.cache_port,
    'database': config.cache_database,
}


def mongodb_init(host, port, database, username=None, password=None):
    """mongodb 初始化对象.

        :param host: 主机
        :param port: 端口
        :param database: 数据库
        :param username: 账户
        :param password: 密码
    """
    if username and password:
        connection_string = "mongodb://%s:%s@%s:%d/%s" % (username, password, host, port, database)
        client = pymongo.MongoClient(connection_string)
    else:
        client = pymongo.MongoClient(host, port)
        # client = motor.MotorClient(host, port, max_pool_size=5)
    database = client[database]

    return database


# ===================以下为Redis选项===================

# redis配置项
REDIS_CONFIG = dict(
    redis_host=config.redis_host,
    redis_port=config.redis_port,
    password=config.redis_password
)


def mongodb_init(connection_string, database):
    """mongodb 初始化对象.
    """
    client = pymongo.MongoClient(connection_string)
    return client[database]


def generate_models(session, databases_config, database_name, column_prefix='__'):
    """"从数据库表生成模型.

        :parameter session:             DB Session
        :parameter databases_config:    数据库配置
        :parameter database_name:　     数据库名称
        :parameter column_prefix:       属性(列)前缀
    """
    _tables = databases_config[database_name]
    return ModelHelper.get_models(session, tables=_tables, column_prefix=column_prefix, schema=database_name)


MYSQL_DATABASES_TABLES = {
    config.discus_db: [
        "common_member", "common_member_status", "ucenter_members",
        "forum_thread",
        "forum_post", "forum_attachment", "forum_memberrecommend",
    ]
}

MYSQL_DATABASES_TABLES[config.discus_db] = [
    "%s_%s" % ('iky', i) for i in MYSQL_DATABASES_TABLES[config.discus_db]]

# 增加相关的分表
forum_attachment_list = [
    "%s_forum_attachment_%d" % (config.discus_prefix, i) for i in range(0, 10)]

MYSQL_DATABASES_TABLES[config.discus_db].extend(forum_attachment_list)

generate_models = functools.partial(
    generate_models, forum_session, MYSQL_DATABASES_TABLES)

generate_db_models = generate_models(config.discus_db)
