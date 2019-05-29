#!/usr/bin/env python
# -*- coding: utf-8 -*-

from discuzx_tools.conf.config import config

# 默认100分钟
UNIX_TIME_TTL = 6000

ACCESS_KEY = config.access_key
SECRET_KEY = config.secret_key

# 默认私有空间
BUCKET_NAME = config.bucket_name

# "7xo804.com1.z0.glb.clouddn.com"
BUCKET_DOMAIN = config.bucket_domain or "source.ikuanyu.com"

# 默认公共空间
PUBLIC_BUCKET_NAME = ""
PUBLIC_BUCKET_DOMAIN = ""
