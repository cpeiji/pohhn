from flask import Flask
from flask import render_template
from app.main.service.FetchRecordService import FetchRecordService
from app.main.dao.FetchRecordDAO import FetchRecordDAO
from app.main.enums.ParamTypeEnum import ParamTypeEnum
app = Flask(__name__)


@app.route("/record/index.htm")
def index():
    f = FetchRecordService()
    b_List = f.query_new_record(ParamTypeEnum.bilibili.value)

    return render_template('record/index.html', bList=b_List)

if __name__ == '__main__':
    app.run()