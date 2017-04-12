import requests
from app.main.utils.RequestUtil import RequestUtil
from app.main.utils.TimeUtil import TimeUtil
from app.main.enums.ParamTypeEnum import ParamTypeEnum
from app.main.dao.FetchParamDAO import FetchParamDAO
import threading
import json


Lock = threading.Lock()

##获取哔哩哔哩信息的类
class FetchBilibili(object):
    __instance = None

    fpd = FetchParamDAO()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FetchBilibili, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance

    def fetch_all_video_list_json(self):
        sql = "select * from rss_fetch_param where type = "+str(ParamTypeEnum.bilibili.value)
        param_list = self.fpd.query_by_sql(sql)
        for param in param_list:
            url = param.link
            payload = param.payload
            headers = param.headers
            f_json = RequestUtil.create_json_requ(url,payload,headers)#fetch到的主播视频列表对象
            v_list = f_json['data']['vlist']

            for video in v_list:
                print(video['aid'],video['title'],video['pic'], TimeUtil.stamp_to_date(video['created']))




FetchBilibili().fetch_all_video_list_json()





