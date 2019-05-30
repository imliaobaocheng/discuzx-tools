#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""以服务的形式运行模拟用户操作.
"""

import random
import traceback

import time
from twisted.internet import task, reactor

from discuzx_tools.conf.data_config import forum_session
from discuzx_tools.conf.logger_config import faker_user_status_info
from discuzx_tools.libs.common.scheduler import partial, skip_hours, NoInterval
from discuzx_tools.libs.models.remote import CommonMemberStatus
from discuzx_tools.libs.models.submeter import cache_thread_member
from discuzx_tools.libs.register.factory import FakeVisitor
from discuzx_tools.tools.base import config_setup

print(config_setup)
limits = (5, 10, 15,)
intervals = (20, 30, 40)


@skip_hours
def fake_visitor(gen_data_count=1):
    """虚拟访客状态更新.

        :parameter gen_data_count: 生成数据数量
    """

    try:
        faker_user_status_info.info("=" * 80)

        # 随便从cache里找出uid
        user_ids = [member_status["uid"] for member_status in
                    FakeVisitor().generate(gen_data_count)]

        # 查出uid的会员状态更新数据
        member_status_entities = forum_session.query(
            CommonMemberStatus).filter(
            CommonMemberStatus.__uid.in_(user_ids)).all()

        if not member_status_entities:
            print("Info: No Data.")
            return

        member_status_list = []
        for member_status in member_status_entities:
            member_status.__lastvisit = int(time.time())
            member_status.__lastactivity = int(time.time())
            member_status_list.append(member_status)
            time.sleep(random.randint(5, 100))

        forum_session.add_all(member_status_list)
        forum_session.commit()
    except Exception as ex:
        faker_user_status_info.info(ex)
        traceback.print_exc()
        forum_session.rollback()
    else:
        faker_user_status_info.info(user_ids)
    finally:
        forum_session.close()


def fake_visitor_only(always=False):
    """仅仅访客部分.

        :param always: 是否一直运行
    """

    cache_thread_member()

    if always:
        # 纳入间隔时间后再次执行
        create_data = task.LoopingCall(fake_visitor, limits[0])
        create_data.start(intervals[0])
        reactor.run()
    else:
        cb = partial(fake_visitor, gen_data_count=random.choice(limits))
        NoInterval.demo(cb, intervals=intervals)


if __name__ == '__main__':
    fake_visitor_only()
