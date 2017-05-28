from app.main.utils.SqlUtil import SqlUtil
from app.main.entity.FetchParamDO import FetchParamDO
import threading
import sqlite3 as sqlite
from app.main.enums.DbPathEnum import DbPathEnum


Lock = threading.Lock()
class FetchParamDAO():
    __instance = None

    table_name = "rss_fetch_param"

    db_path = DbPathEnum.db_path.value

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FetchParamDAO, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance

    def query_all(self):
        db = sqlite.connect(self.db_path)
        sql = SqlUtil.query_all_sql(self.table_name)
        cursor = db.execute(sql)
        return self.setParam(cursor)


    def query_by_id(self,id):
        db = sqlite.connect(self.db_path)
        sql = SqlUtil.query_by_id_sql(self.table_name,id)
        cursor = db.execute(sql)
        fetch_param_list = self.setParam(cursor)
        return fetch_param_list[0]

    def query_by_sql(self,sql):
        db = sqlite.connect(self.db_path)
        cursor = db.execute(sql)
        fetch_param_list = self.setParam(cursor)
        return fetch_param_list

##对象注入，直接忽略其存在
    def setParam(self,cursor):
        list = []
        for row in cursor:
            fp = FetchParamDO()
            fp.id = row[0]
            fp.link = row[1]
            fp.headers = row[2]
            fp.payload = row[3]
            fp.memo = row[4]
            fp.type = row[5]
            list.append(fp)
        return list
