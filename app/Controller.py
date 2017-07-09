from flask import Flask
from flask import render_template
from flask import json
from flask import jsonify
from flask import request
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from app.main.service.FetchRecordService import FetchRecordService
from app.main.task.FetchTask import FetchTask
from app.main.dao.FetchRecordDAO import FetchRecordDAO
from app.main.enums.ParamTypeEnum import ParamTypeEnum
from app.main.utils.JsonUtil import JsonUtil
from app.main.BizResult import BizResult

app = Flask(__name__)

# #首页
# @app.route("/")
# def index():
#     return render_template('record/index.html')

#一键爬取所有的关注信息
@app.route("/fetchall.json")
def fetchall():
    fetch_all = FetchTask()
    biz_result = BizResult()
    biz_result.success = fetch_all.fetch_all()
    return jsonify(biz_result.__dict__)


@app.route("/getRecord.json",methods=['GET'])
def get_record():
    type = request.args.get('type')
    fetch = FetchRecordService()
    list = JsonUtil.list_obj_dict(fetch.query_new_record(type))
    return jsonify(list)


@app.route("/detail.html")
def detail():

    return render_template()





if __name__ == '__main__':
    app.run()