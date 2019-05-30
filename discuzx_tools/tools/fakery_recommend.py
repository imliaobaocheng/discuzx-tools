#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""以服务的形式运行模拟用户操作.
"""

import datetime
import random

import time
from twisted.internet import task, reactor

from discuzx_tools.conf.data_config import forum_session
from discuzx_tools.conf.logger_config import faker_recommend_info
from discuzx_tools.libs.common.scheduler import partial, skip_hours, NoInterval
from discuzx_tools.libs.models.remote import ForumThread, ForumMemberRecommend
from discuzx_tools.libs.models.submeter import cache_thread_member
from discuzx_tools.libs.register.factory import FakeRecommend
from discuzx_tools.tools.base import config_setup

print(config_setup)
limits = (1, 2, 3)
intervals = (30, 50, 70, 80)


@skip_hours
def fake_recommend(gen_data_count=1):
    """虚拟对主题顶帖.

        :parameter gen_data_count: 生成数据数量
    """

    for entity in FakeRecommend().generate(gen_data_count):
        print(entity)
        tid = entity["tid"]
        uid = entity["uid"]
        opinion = entity["opinion"]

        print(tid, uid, opinion)

        faker_recommend_info.info("=" * 80)
        faker_recommend_info.info("(%s)正在评帖(%s)" % (uid, tid))

        # 查询是否顶过帖
        recommend_entities = forum_session.query(ForumMemberRecommend).filter(
            ForumMemberRecommend.__tid == tid,
            ForumMemberRecommend.__recommenduid == uid).all()

        if recommend_entities:
            faker_recommend_info.info("返回:之前已评过该帖！")
            continue

        try:
            forum_member_recommend = ForumMemberRecommend(
                __tid=tid,
                __recommenduid=uid,
                __dateline=int(
                    time.time()))
            forum_thread = forum_session.query(ForumThread).filter(
                ForumThread.__tid == tid).first()
            forum_thread.__views += 1  # 查看次数
            forum_thread.__recommends += 1  # 推荐指数
            if opinion < 85:
                forum_thread.__recommend_add += 1  # 支持人数
            else:
                forum_thread.__recommend_sub += 1  # 反对人数

            forum_session.add(forum_member_recommend)
            forum_session.add(forum_thread)
            forum_session.commit()
        except Exception as ex:
            faker_recommend_info.exception(ex)
            faker_recommend_info.info("评帖失败: Error.")
            forum_session.rollback()
        else:
            faker_recommend_info.info("评帖成功: OK.")
        finally:
            forum_session.close()


action_data_config = (
    # 任务, 数据量, 时间间隔
    (fake_recommend, 1, 5.0),
)


def main():
    """事件模拟任务调度.
    """

    cache_thread_member()

    for data_item in action_data_config:
        if type(data_item[0]) == 'function':
            create_data = task.LoopingCall(data_item[0], data_item[1])
            create_data.start(data_item[2])

    reactor.run()


def minor():
    """仅仅顶贴部分.
    """

    cache_thread_member()

    while True:
        print(datetime.datetime.now())
        fake_recommend(1)
        # time.sleep(60)


def fake_recommend_only(always=False):
    """仅仅顶贴部分.

        :param always: 是否一直运行
    """

    cache_thread_member()

    if always:
        # 纳入间隔时间后再次执行
        create_data = task.LoopingCall(fake_recommend, limits[0])
        create_data.start(intervals[0])
        reactor.run()
    else:
        cb = partial(fake_recommend, gen_data_count=random.choice(limits))
        NoInterval.demo(cb, intervals=intervals)


if __name__ == '__main__':
    # main()
    # minor()
    fake_recommend_only()
