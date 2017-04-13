# -*- coding: utf-8 -*-
import time


class TimeUtil:
    @staticmethod
    def stamp_to_date(timestamp):
        sdf = "%Y-%m-%d %H:%M:%S"
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        return time.strftime(sdf, time_local)


