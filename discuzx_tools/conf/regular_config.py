# !usr/bin/env python
# coding: utf-8

"""定义规则配置.
"""

from discuzx_tools.libs.common.func import Utils

# 搜索目录
SEEK_DIRECTORY = "/media/uploads/ready"

# 用户映射配置
USER_MAP_CONFIG = dict(
    admin="1|admin@126.com|admin",
)

# 从数据库导出的原版数据
plate_map_string = """
    |2|量化投资
    |38|高频交易
    |39|期权研究
    |40|商品期货CTA
    |41|MatLab
    |42|交易系统开发
    |44|股票投资
    |45|债券投资
    |47|FRM
    |48|宏观经济
    |49|灌水区
    |50|数据下载
    |51|视频教程
    |52|课件书籍
    |53|软件下载
    |54|宽语一期
    |55|有问必答
    |60|廖哥有话说
    |62|Alpha策略
    |65|宽语二期
    |66|谢谢专栏
    |67|超哥量化专区
    |68|张老师的各种回归
    |69|智能算法专区
    |70|邹博士专区
"""

# 计划跳过的文件列表
IGNORE_FILE_LIST = ["readme.txt", "README"]

# 是否要跳过列表文件
SKIP_README_FILE = True

# 是否启用规定的文件夹结构(版块/作者)
ENABLE_FOLDER_RULE = True

# 每次扫描数据数量
MATCH_FILES_LIMIT = 5

# 每次扫描时间间隔, 默认五分钟.
MATCH_FILES_INTERVAL = 1 * 60

# 版块映射配置
PLATE_MAP_CONFIG = Utils.get_plate_map_conf(plate_map_string)
