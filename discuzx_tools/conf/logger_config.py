# !usr/bin/env python
# coding: utf-8
import logging

from discuzx_tools.libs.common.logger import build_logger

level = logging.INFO  # logging.DEBUG

# 注意指定的目录要有权限
redis_data_log = build_logger("redis_data", level)

model_record_log = build_logger("model_record", level)
model_remote_log = build_logger("model_remote", level)

record_info = build_logger("record_info", level)
upload_info = build_logger("upload_info", level)
upload_error = build_logger("upload_error", level)

post_info = build_logger("post_info", level)

faker_post_info = build_logger("faker_post_info", level)
faker_post_error = build_logger("faker_post_error", level)

faker_user_info = build_logger("faker_user_info", level)
faker_recommend_info = build_logger("faker_recommend_info", level)
faker_user_status_info = build_logger("faker_user_status_info", level)

broad_site_info = build_logger("broad_site_info", level)
gateway_debug_log = build_logger("gateway_debug", level)
