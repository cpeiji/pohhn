# -*- coding: utf-8 -*-
import time
import datetime

class TimeUtil:
    @staticmethod
    def stamp_to_date(timestamp):
        sdf = "%Y-%m-%d %H:%M:%S"
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        return time.strftime(sdf, time_local)

    @staticmethod
    def get_now_date():
        sdf = "%Y-%m-%d %H:%M:%S"
        # 转换成新的时间格式(2016-05-05 20:28:54)
        return time.strftime(sdf, time.time())

    @staticmethod
    def get_date_yet(days_dis):
        sdf = "%Y-%m-%d %H:%M:%S"
        now_time = datetime.datetime.now()
        four_yet_time = now_time + datetime.timedelta(days=-days_dis)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        return four_yet_time.strftime(sdf)



