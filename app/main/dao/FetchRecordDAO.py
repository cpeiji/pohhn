from app.main.utils.SqlUtil import SqlUtil
from app.main.entity.FetchRecordDO import FetchRecordDO
import threading
import sqlite3 as sqlite


Lock = threading.Lock()
class FetchRecordDAO(object):
    __instance = None

    table_name = "rss_fetch_record"

    db_path ="../rss.sqlite"

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FetchRecordDAO, cls).__new__(cls, *args, **kwargs)
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
        fetch_record_list = self.setParam(cursor)
        return fetch_record_list[0]

    def query_by_sql(self,sql):
        db = sqlite.connect(self.db_path)
        cursor = db.execute(sql)
        fetch_record_list = self.setParam(cursor)
        return fetch_record_list

    def insert_list(self,list):
        db = sqlite.connect(self.db_path)
        for fr in list:
            cursor = db.execute("SELECT  * FROM rss_fetch_record WHERE mid = " + str(fr.mid))
            sl = self.setParam(cursor)
            if len(sl) == 0 :
                value = "'"+str(fr.mid)+"','"+fr.name+"','"+fr.desc+"','"+fr.link+"','"+fr.gmt_create+"','"+str(fr.is_click)+"','"+fr.pic+"','"+fr.extra+"','"+str(fr.type)+"'"
                sql = "insert into " + self.table_name + " ('mid','name','desc','link','gmt_create','is_click','pic','extra','type') values ("+value+")"
                db.execute(sql)
                db.commit()



##对象注入，直接忽略其存在
    def setParam(self,cursor):
        list = []
        for row in cursor:
            fr = FetchRecordDO()
            fr.id = row[0]
            fr.mid = row[1]
            fr.name = row[2]
            fr.desc = row[3]
            fr.link = row[4]
            fr.gmt_create = row[5]
            fr.is_click = row[6]
            fr.pic = row[7]
            list.append(fr)
        return list
