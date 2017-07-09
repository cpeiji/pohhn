import requests
from bs4 import BeautifulSoup
from app.main.utils.RequestUtil import RequestUtil
from app.main.utils.TimeUtil import TimeUtil
from app.main.enums.ParamTypeEnum import ParamTypeEnum
from app.main.dao.FetchParamDAO import FetchParamDAO
from app.main.dao.FetchRecordDAO import FetchRecordDAO
from app.main.entity.FetchRecordDO import FetchRecordDO
import re
import threading
import json


Lock = threading.Lock()

##获取电影天堂的类
class FetchDytt(object):
    __instance = None

    fpd = FetchParamDAO()

    frd = FetchRecordDAO()

    gen_link = "http://www.dytt8.net"

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FetchDytt, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance

    def fetch_new_movie_list(self):
        sql = "select * from rss_fetch_param where type = "+str(ParamTypeEnum.movie.value)
        param_list = self.fpd.query_by_sql(sql)
        for param in param_list:
            url = param.link
            payload = param.payload
            headers = param.headers
            f_html = RequestUtil.create_html_requ(url,payload,headers,'gbk')#fetch到的主播视频列表对象
            soup = BeautifulSoup(f_html,"html.parser")
            list = soup.find_all("div", class_="co_content8")[0].find_all(href=re.compile("20"));
            db_list = []
            for item in list:
                soup = BeautifulSoup(str(item),"html.parser")
                movie_name = soup.find_all("a")[0].string
                link = self.gen_link+soup.find_all("a")[0].get('href')
                db_list.append(self.fetch_movie_detail(link,payload,headers,movie_name,link))
            self.frd.insert_list(db_list)

    def fetch_movie_detail(self,url,payload,headers,movie_name,link):
        d_html = RequestUtil.create_html_requ(url, payload, headers, 'gbk')  # fetch到的主播视频列表对象
        soup = BeautifulSoup(d_html,"html.parser")
        content = soup.find_all("div",class_="bd3r")[0]
        post = content.find_all("img")[0].get('src') #海报
        screen_shot = content.find_all("img")[1].get('src') #截图
        download_link = content.find_all("a")[0].get('href') #下载链接
        create_time = content.find_all(text=re.compile("发布时间"))[0].strip().replace("\n", "").split("：")[1]#发布时间
        mid = link.split('/')[7].split('.')[0] ##唯一的项目标志符号
        imdb_score = ""
        douban_score = ""
        try:
            imdb_score = content.find_all(text=re.compile("IMDb"))[0]
        except Exception as e:
            imdb_score = "无imdb评分"
        try:
            douban_score = content.find_all(text=re.compile("豆瓣"))[0]
        except Exception as e:
            douban_score = "无豆瓣评分"
        fetchDO = FetchRecordDO()
        fetchDO.name = "【"+create_time+"】"+movie_name
        fetchDO.desc = imdb_score+"  "+douban_score
        fetchDO.extra = "下载链接："+download_link
        fetchDO.gmt_create = create_time
        fetchDO.mid = mid
        fetchDO.link = link
        fetchDO.pic = post+"#*#"+screen_shot
        fetchDO.type = ParamTypeEnum.movie.value
        return fetchDO




