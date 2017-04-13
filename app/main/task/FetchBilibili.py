import requests
from app.main.utils.RequestUtil import RequestUtil
from app.main.utils.TimeUtil import TimeUtil
from app.main.enums.ParamTypeEnum import ParamTypeEnum
from app.main.dao.FetchParamDAO import FetchParamDAO
from app.main.dao.FetchRecordDAO import FetchRecordDAO
from app.main.entity.FetchRecordDO import FetchRecordDO
import threading
import json


Lock = threading.Lock()

##获取哔哩哔哩信息的类
class FetchBilibili(object):
    __instance = None

    fpd = FetchParamDAO()

    frd = FetchRecordDAO()

    gen_link = "http://www.bilibili.com/video/av"

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
            list = []
            for video in v_list:
                fr = FetchRecordDO()
                fr.mid = video['aid']
                fr.name = video['title']
                fr.desc = video['description']
                fr.is_click = 0
                fr.link = self.gen_link + str(fr.mid);
                fr.pic = video['pic']
                fr.gmt_create = TimeUtil.stamp_to_date(video['created'])
                fr.extra = "时长："+video['length']+" 播放次数："+str(video['play'])+" 评论次数："+str(video['comment'])
                fr.type = ParamTypeEnum.bilibili.value
                list.append(fr)
            self.frd.insert_list(list)







