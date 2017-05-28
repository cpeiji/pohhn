from flask import Flask
from flask import render_template
from flask import json
from flask import jsonify
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from app.main.service.FetchRecordService import FetchRecordService
from app.main.task.FetchTask import FetchTask
from app.main.dao.FetchRecordDAO import FetchRecordDAO
from app.main.enums.ParamTypeEnum import ParamTypeEnum
from app.main.BizResult import BizResult

app = Flask(__name__)

#首页
@app.route("/index.html")
def index():
    f = FetchRecordService()
    b_list = f.query_new_record(ParamTypeEnum.bilibili.value)
    dytt_list = f.query_new_record(ParamTypeEnum.dytt.value)
    if b_list is None:
        b_list = []
    if dytt_list is None:
        dytt_list = []


    b_list_lenth = len(b_list)
    dytt_list_length = len(dytt_list)

    return render_template('record/index.html', bList=b_list,dyttList=dytt_list
                           ,bListLenth = b_list_lenth,dyttListLenth = dytt_list_length)

#一键爬取
@app.route("/fetchall.json")
def fetchall():
    fetch_all = FetchTask()
    biz_result = BizResult()
    biz_result.success = fetch_all.fetch_all()
    return jsonify(biz_result.__dict__)

@app.route("/detail.html")
def detail():

    return render_template()





if __name__ == '__main__':
    app.run()