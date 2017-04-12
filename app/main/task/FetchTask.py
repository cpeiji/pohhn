import datetime
import threading
from FetchBilibili import FetchBilibili



Lock = threading.Lock()
class FetchTask(object):
    __instance = None
    bilibili = fb()

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
        bilibili = FetchBilibili()




