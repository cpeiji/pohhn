from app.main.utils.RequestUtil import RequestUtil
from app.main.utils.TimeUtil import TimeUtil
from app.main.enums.ParamTypeEnum import ParamTypeEnum
from app.main.dao.FetchParamDAO import FetchParamDAO
from app.main.dao.FetchRecordDAO import FetchRecordDAO
from app.main.entity.FetchRecordDO import FetchRecordDO
import threading
import json


Lock = threading.Lock()

class FetchRecordService():
    __instance = None

    frd = FetchRecordDAO()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FetchRecordService, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance

    def query_new_record(self,type):
        try:
            days_yet = TimeUtil.get_date_yet(7)#一个礼拜内的数据
            sql = "select * from rss_fetch_record where gmt_create >'"+days_yet+"' and type = "+str(type)+" order by gmt_create DESC "
            list = self.frd.query_by_sql(sql)
            return list
        except Exception as e:
            print(e)


# #TEST CODE
# ss = FetchRecordService()
# ss.query_new_record(1)

