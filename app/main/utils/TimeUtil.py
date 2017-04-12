# -*- coding: utf-8 -*-
import time


class TimeUtil:
    @staticmethod
    def stamp_to_date(timestamp):
        sdf = "%Y年%m月%d日 %H:%M:%S"
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        return time.strftime(sdf.encode('utf-8').decode("utf-8"), time_local)


