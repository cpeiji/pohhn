import datetime
import threading
from app.main.task.FetchBilibili import FetchBilibili
from app.main.task.FetchDytt import FetchDytt



Lock = threading.Lock()

class FetchTask(object):
    __instance = None

    bilibili = FetchBilibili()
    dytt = FetchDytt()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FetchTask, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance

    def fetch_all(self):
        self.bilibili.fetch_all_video_list_json() #bilibili定时信息抓取
        self.dytt.fetch_new_movie_list()#抓取dytt的数据
        return True;






