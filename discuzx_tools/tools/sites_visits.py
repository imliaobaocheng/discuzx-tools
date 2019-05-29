# !usr/bin/env python
# coding: utf-8

from discuzx_tools.conf.config import config
from discuzx_tools.libs.common.accessor import visited_quit
from discuzx_tools.tools.base import config_setup

print(config_setup)

if __name__ == '__main__':
    visited_quit(config.sites_pages, auth=True)
