import requests
from app.main.utils.RequestUtil import RequestUtil
import threading
import json


Lock = threading.Lock()

class FetchBilibili(object):

    __instance = None

    # reqUtil = RequestUtil()

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


    def fetchVideoListJson(self):
        url = "http://space.bilibili.com/ajax/member/getSubmitVideos"
        payload = {'mid': '15834498'}
        f_json = RequestUtil.create_json_requ(url,payload,"")#fetch到的主播视频列表对象
        v_list = f_json['data']['vlist']
        for video in v_list:
            print(video['aid'],video['title'])
        # return content_obj

    


f = FetchBilibili()
f.fetchVideoListJson()





