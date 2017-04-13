from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/record/index.htm")
def index():
    name = "hello word"
    return render_template('record/index.html', name=name)

if __name__ == '__main__':
    app.run()